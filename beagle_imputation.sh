#!/bin/bash

J8=~/Programs/jdk1.8.0_201/bin/java
BEAGLE=~/Programs/beagle.27Jan18.7e1.jar

${J8} -Xmx60g -jar ${BEAGLE} gt=../CHR_combined.genotyped.filtered.passed.has_var.par_delim.contig_filter.g.vcf.gz out=../CHR_combined.imputed.vcf lowmem=true
