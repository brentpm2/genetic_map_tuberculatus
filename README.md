# genetic_map_tuberculatus

Takes output from GATK 4.0 haplotypecaller and creates a set of variants in mapmaker format for genetic map construction. filter_variants_mapping.sh is the pipeline, and other scripts are components of the process. Briefly:

1) marker_in_F2.py - create a subset of all variant sites with at least 10% presence within the dataset.
2) rad_site_in_parent.py - create a subset of all variant sites where the site was also present in a supplied vcf corresponding to the parents of the cross
3) contigs_by_sample.py - creates a list of the largest number of contigs retained for a given sample size, where each retained contig is present in each selected sample.
4) subset_contigs_samples.py - create a subset of samples and contigs based on contigs_by_sample.py output for 100 samples retained (plus the two parents)
5) beagle_imputation.sh - run beagle 4.0 in lowmem mode
6) paint_parent.py - apply parental identity to the imputed SNP/INDEL dataset.
7) to_mapmaker.py - convert the intermediate file from paint_parent.py into a mapmaker format
8) make_mapfile.py - generate a mapfile corresponding to to_mapmaker.py
