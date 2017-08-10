from Bio import SeqIO
from Bio.SeqUtils import GC

infile = list(SeqIO.parse("/home/maxwell.a.sherman/genomes/human.fa", "fasta"))

# i = 0
# while i < len(infile):
    # if len(infile[i].id) == 4 or len(infile[i].id) == 5:
        # print "Length of", infile[i].id, "is", len(infile[i])
    # i += 1

print "GC content of", infile[0].id, "is", GC(infile[0].seq)