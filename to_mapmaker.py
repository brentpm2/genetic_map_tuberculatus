#!/usr/bin/python

in_file_path = "../CHR_combined.imputed.painted.vcf"
out_file_path = "../CHR_combined.imputed.painted.raw.txt"

in_file = open(in_file_path,"r")
samples_list = []
markers_list = []
genotypes = []
for line in in_file:
    line = line.strip("\n")
    if line[1] != "#":
        if line[0] == "#":
            samples_list = line.split("\t")[9:]
        else:
            frags = line.split("\t")
            markers_list.append(("{}.{}".format(frags[0],frags[1])))
            genotypes.append(frags[9:])

in_file.close()

out_file = open(out_file_path,"w")

out_file.write("data type F2 intercross\n{} {} {}".format(len(samples_list),len(markers_list),0))

for i in range(len(markers_list)):
    out_file.write("\n*{}\t".format(markers_list[i]))
    for j in range(len(samples_list)):
        out_file.write(genotypes[i][j])

out_file.close()
