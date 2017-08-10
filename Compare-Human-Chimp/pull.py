# SUMMARY
# This program exports a hard-coded section of nucleotides
# from a hard-coded genome file into its own file.
#
# The purpose of this program is to separate out a specific gene
# from a genome because genomes are massive and hard to handle.
#
# Maxwell Sherman

from Bio import SeqIO

infile = list(SeqIO.parse("/home/maxwell.a.sherman/genomes/chimp.fa", "fasta"))
outfile = open("chimp-MC1R.txt", "w+")

for chromosome in infile:
    if chromosome.id == "chr16":
        output = str(chromosome.seq[81419616:81421241])
        outfile.write(output)