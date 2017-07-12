infile = open("genetic-code.txt", "r")
aminoAcids = {}

for line in infile:
    key = line
    key = key.split()
    inCodon = key[0]
    inAmino = key[1]
    aminoAcids[inCodon] = inAmino 

infile.close()
#infile = open("ALDH.txt", "r")
infile = open("random-gene.txt", "r")
outfile = open("protein.txt", "w+")

nucleotides = infile.readline()
nucleotides = nucleotides[:-1]
for i in range(0, len(nucleotides), 3):
    translateCodon = nucleotides[i:i + 3]
    outfile.write(aminoAcids[translateCodon])
print "Written to protein.txt"