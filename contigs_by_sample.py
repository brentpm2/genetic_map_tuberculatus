#!/usr/bin/python

import gzip

in_F2_path = "../CHR_combined.genotyped.filtered.passed.has_var.par_delim.g.vcf.gz"
out_path = "../CHR_combined.sample_contig_opt.stats"

in_F2_file = gzip.open(in_F2_path,"rb")

contig_list = []
sample_list = []
sample_markers = []
marker_list = []
print("Loading in_file")
for line in in_F2_file:
    line = line.strip("\n")
    if line[1] != "#":
        if line[0] == "#":
            #header
            sample_list = line.split("\t")[9:]
        else:
            frags = line.split("\t")
            curr_markers = []
            marker_list.append(frags[0])
            for frag in frags[9:]:
                curr_markers.append(frag.split(":")[0])
            sample_markers.append(curr_markers)

in_F2_file.close()

#make a structure where is samples x contig, where element is number of markers
print("Making counting markers per contigs-sample")
sample_contig_count = {}
for j in range(len(sample_list)):
    num_markers = 0
    curr_contig = marker_list[0]
    temp_list = []
    for i in range(len(marker_list)):
        if curr_contig != marker_list[i]:
            if num_markers > 1:
                temp_list.append(curr_contig)
            num_markers = 0
            curr_contig = marker_list[i]
        if sample_markers[i][j] != "./.":
            num_markers += 1
    sample_contig_count[sample_list[j]] = list(temp_list)
curr_contig = ""
for i in range(len(marker_list)):
    if curr_contig != marker_list[i]:
        curr_contig = marker_list[i]
        contig_list.append(curr_contig)
out_file = open(out_path,"w")
out_file.write("num_contigs\tcontig_list\tnum_samples\tsample_list")
num_samples = 0
sample_list = []

while sample_contig_count:
    best_key = ""
    best_len = -1
    best_list = []
    for key in sample_contig_count:
        curr_list = list(set(contig_list) & set(sample_contig_count[key]))
        curr_len = len(curr_list)
        if curr_len > best_len:
            best_key = key
            best_len = curr_len
            best_list = list(curr_list)
    #best key selected
    num_samples += 1
    sample_list.append(best_key)
    out_file.write("\n{}\t{}\t{}\t{}".format(best_len,best_list,num_samples,sample_list))
    print(best_key)
    print(best_key in sample_contig_count)
    sample_contig_count.pop(best_key)
    contig_list = list(best_list)

out_file.close()
