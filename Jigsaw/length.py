from Bio import SeqIO
genome = list(SeqIO.parse("/home/maxwell.a.sherman/genomes/ecoli.fa", "fasta"))

print len(genome[0])