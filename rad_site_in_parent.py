#!/usr/bin/python

import gzip

in_F2_path = "../CHR_combined.genotyped.filtered.passed.has_var.g.vcf.gz"
in_parent_path = "../CHR_parents.genotyped.filtered.all_var.par_delim.g.vcf.gz"
out_F2_path = "../CHR_combined.genotyped.filtered.passed.has_var.par_delim.g.vcf.gz"

in_parent = gzip.open(in_parent_path,"rb")

variants_dict = {}

print("Making variant dictionary")
counter = 0

for line in in_parent:
    if line[0] not in "#":
        counter += 1
        if counter % 100000 == 0:
            print("Variants added: {}".format(counter))
        frags = line.split("\t")
        if frags[0] not in variants_dict:
            variants_dict[frags[0]] = {}
        variants_dict[frags[0]][frags[1]] = 1

in_parent.close()
in_F2 = gzip.open(in_F2_path,"rb")
out_F2 = gzip.open(out_F2_path,"wb")
first = True

print("Parsing F2 file")
counter = 0

for line in in_F2:
    line = line.strip('\n')
    if line[0] == "#":
        if first:
            out_F2.write(line)
            first = False
        else:
            out_F2.write("\n{}".format(line))
    else:
        counter += 1
        if counter % 100000 == 0:
            print("Variants processed: {}".format(counter))
        frags = line.split("\t")
        if frags[0] in variants_dict:
            if frags[1] in variants_dict[frags[0]]:
                out_F2.write("\n{}".format(line))

in_F2.close()
out_F2.close()
