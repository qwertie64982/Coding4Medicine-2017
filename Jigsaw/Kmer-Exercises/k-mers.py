from Bio import SeqIO
import os

reads = list(SeqIO.parse("/home/maxwell.a.sherman/genomes/ecoli.fa", "fasta"))
stringInput = raw_input("Enter range of k-mer sizes, [x, y) : ")
kSizes = map(int, stringInput.split(", "))
kmers = {}

# Find all k-mers of genome
genome1 = str(reads[0].seq)
for k in range(kSizes[0], kSizes[1]):
    for i in range(0, len(genome1) - k + 1):
        if genome1[i:i + k] not in kmers:
            kmers[genome1[i:i + k]] = 1
        else:
            kmers[genome1[i:i + k]] += 1

# Find all k-mers of genome reverse compliment
genome2 = str(reads[0].seq.reverse_complement())
for k in range(kSizes[0], kSizes[1]):
    for i in range(0, len(genome2) - k + 1):
        if genome2[i:i + k] not in kmers:
            kmers[genome2[i:i + k]] = 1
        else:
            kmers[genome2[i:i + k]] += 1

print "k-mers found, writing to file."

outfile = open("k-mers.txt", "w+")
for i in range(kSizes[0], kSizes[1]):
    for kmer in kmers:
        if len(kmer) == i and kmers[kmer] > 1:
            outfile.write("%s: %d\n" % (kmer, kmers[kmer]))

print "Successfully written to k-mers.txt."

os.system("sort -k 2 -n -r k-mers.txt -o k-mers.txt")
print "Sorted."