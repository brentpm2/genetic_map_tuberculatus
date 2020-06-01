#!/usr/bin/python

import gzip

in_path = "../CHR_combined.imputed.vcf.vcf.gz"
out_path = "../CHR_combined.imputed.painted.vcf"
R_parent = "CHR_P"
S_parent = "WUS5_P"
R_index = -1
S_index = -1

in_file = gzip.open(in_path,"rb")
out_file = open(out_path,"w")
first = True
for line in in_file:
    line = line.strip("\n")
    if line[1] == "#":
        if first:
            first = False
            out_file.write(line)
        else:
            out_file.write("\n{}".format(line))
    else:
        if line[0] == "#":
            frags = line.split("\t")
            for i in range(len(frags)):
                if frags[i] == R_parent:
                    R_index = i
                if frags[i] == S_parent:
                    S_index = i
            out_file.write("\n{}".format(line))
        else:
            frags = line.split("\t")
            R_alleles = frags[R_index].split("|")
            S_alleles = frags[S_index].split("|")
            first = True
            for i in range(len(frags)):
                if i < 9:
                    if first:
                        first = False
                        out_file.write("\n{}".format(frags[i]))
                    else:
                        out_file.write("\t{}".format(frags[i]))
                else:
                    curr_alleles = frags[i].split("|")
                    if curr_alleles[0] in R_alleles and curr_alleles[1] in R_alleles:
                        out_file.write("\tA")
                    elif curr_alleles[0] in S_alleles and curr_alleles[1] in S_alleles:
                        out_file.write("\tB")
                    else:
                        out_file.write("\tH")

in_file.close()
out_file.close()
