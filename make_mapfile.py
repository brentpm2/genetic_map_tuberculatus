#!/usr/bin/python

in_file_path = "../CHR_combined.imputed.painted.raw.txt"
out_file_path = "../CHR_combined.imputed.painted.raw.txt.mapfile"

in_file = open(in_file_path,"r")
out_file = open(out_file_path,"w")

num = 0
prev_chrom = ""

first = True
for line in in_file:
    if line[0] == "*":
        frags = line.split("\t")
        name = frags[0]
        chrom = name.strip("*").split(".")[0]
        if prev_chrom != chrom:
            num+=1
            prev_chrom = chrom
        if first:
            first = False
        else:
            out_file.write("\n")
        out_file.write("{}\t{}".format(num,name))

in_file.close()
out_file.close()
