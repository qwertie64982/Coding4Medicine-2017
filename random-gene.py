import random

length = int(raw_input("Length of generated string: "))
if length % 3 == 1:
    length = length - 1
    print "Subtracted 1 to make it divisible by 3."
elif length % 3 == 2:
    length = length - 2
    print "Subtracted 2 to make it divisible by 3."
nucleotideConversion = {0: "A", 1: "T", 2: "C", 3: "G"}

gene = ""
count = 0
while count < length:
    nucleotide = random.randint(0,3)
    nucleotide = nucleotideConversion[nucleotide]
    gene += nucleotide
    count += 1

outfile = open("random-gene.txt", "w+")
outfile.write(gene)
outfile.write("\n")
print "Written to random-gene.txt"