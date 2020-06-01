#!/usr/bin/python

import gzip

in_F2_path = "../CHR_combined.genotyped.filtered.passed.g.vcf.gz"
out_F2_path = "../CHR_combined.genotyped.filtered.passed.has_var.g.vcf.gz"

in_F2 = gzip.open(in_F2_path,"rb")
out_F2 = gzip.open(out_F2_path,"wb")

first = True
counter = 0
for line in in_F2:
    line = line.strip("\n")
    if line[0] == "#":
        if first:
            out_F2.write(line)
            first = False
        else:
            out_F2.write("\n{}".format(line))
    else:
        counter += 1
        if counter % 1000000 == 0:
            print("lines processed: {}".format(counter))
        frags = line.split("\t")
        num_var = 0
        for frag in frags[9:]:
            call = frag.split(":")[0]
            if call != "./.":
                num_var += 1
        if num_var >= 30:
            out_F2.write("\n{}".format(line))

in_F2.close()
out_F2.close()
