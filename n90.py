from Bio import SeqIO

genome = list(SeqIO.parse("/home/maxwell.a.sherman/genomes/fugu.fa", "fasta"))
sizes = []

for scaffold in genome:
    sizes.append(len(scaffold))

sizes.sort(reverse = True)
target = float(sum(sizes)) * 0.9
total = 0 # running total
score = -1 # keeps track of which size

while total < target:
    score += 1
    total += sizes[score]

print sizes[score]
