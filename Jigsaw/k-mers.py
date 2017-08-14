from Bio import SeqIO
genome = list(SeqIO.parse("/home/maxwell.a.sherman/genomes/ecoli.fa", "fasta"))
k = raw_input("Lengh of k for k-mers: ")

kmers = {}
for i in range(0, len(genome[0]) - k + 1):
    if str(genome[0].seq[i:i + k]) not in kmers:
        kmers[str(genome[0].seq[i:i + k])] = 0
    else:
        kmers[str(genome[0].seq[i:i + k])] += 1

print kmers