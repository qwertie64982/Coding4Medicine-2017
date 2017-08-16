from Bio import SeqIO
reads = list(SeqIO.parse("/home/maxwell.a.sherman/genomes/ecoli.fa", "fasta"))
genome = str(reads[0].seq)
# k = raw_input("Lengh of k for k-mers: ")

kmers = {}
for k in range(2, 13):
    for i in range(0, len(genome) - k + 1):
        if genome[i:i + k] not in kmers:
            kmers[genome[i:i + k]] = 0
        else:
            kmers[genome[i:i + k]] += 1

print "k-mers found, writing to file."

outfile = open("k-mers.txt", "w+")
for i in range(2, 13):
    for kmer in kmers:
        if len(kmer) == i and kmers[kmer] > 1:
            outfile.write("%s: %d\n" % (kmer, kmers[kmer]))
            # print "%s: %d" % (kmer, kmers[kmer])