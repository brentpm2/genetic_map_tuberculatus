#!/usr/bin/python

import gzip

in_stats_path = "../CHR_combined.sample_contig_opt.stats"
num_sample_cutoff = 102
in_file_path = "../CHR_combined.genotyped.filtered.passed.has_var.par_delim.g.vcf.gz"
out_file_path = "../CHR_combined.genotyped.filtered.passed.has_var.par_delim.contig_filter.g.vcf.gz"

in_stats = open(in_stats_path,"r")
first = True
keep_contigs = {}
keep_samples = {}
for line in in_stats:
    if first:
        first = False
    else:
        line = line.strip("\n")
        frags = line.split("\t")
        if int(frags[2]) == num_sample_cutoff:
            contigs = frags[1].strip("[").strip("]")
            contigs = contigs.split(" ")
            for entry in contigs:
                entry = entry.strip(",").strip("\'")
                keep_contigs[entry] = 1
            samples = frags[3].strip("[").strip("]")
            samples = samples.split(" ")
            for entry in samples:
                entry = entry.strip(",").strip("\'")
                keep_samples[entry] = 1
            break
in_stats.close()

in_file = gzip.open(in_file_path,"rb")
out_file = gzip.open(out_file_path,"wb")
first = True
keep_samples_index = {}

for line in in_file:
    line = line.strip("\n")
    if line[1] == "#":
        if first:
            out_file.write(line)
            first = False
        else:
            out_file.write("\n{}".format(line))
    else:
        if line[0] == "#":
            frags = line.split("\t")
            first = True
            for i in range(len(frags)):
                if i < 9:
                    if first:
                        out_file.write("\n{}".format(frags[i]))
                        first = False
                    else:
                        out_file.write("\t{}".format(frags[i]))
                else:
                    if frags[i] in keep_samples:
                        keep_samples_index[i] = 1
                        out_file.write("\t{}".format(frags[i]))
        else:
            frags = line.split("\t")
            if frags[0] in keep_contigs:
                first = True
                for i in range(len(frags)):
                    if i < 9:
                        if first:
                            first = False
                            out_file.write("\n{}".format(frags[i]))
                        else:
                            out_file.write("\t{}".format(frags[i]))
                    else:
                        if i in keep_samples_index:
                            out_file.write("\t{}".format(frags[i]))

in_file.close()
out_file.close()
