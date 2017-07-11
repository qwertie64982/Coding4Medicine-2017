infile = open("genetic-code.txt", "r")
aminoAcids = {}

for line in infile:
    key = line
    key = key.split()
    inCodon = key[0]
    inAmino = key[1]
    aminoAcids[inCodon] = inAmino 

infile.close()
infile = open("ALDH.txt", "r")

nucleotides = infile.readline()
nucleotides = nucleotides[:-1]
for i in range(0, len(nucleotides), 3):
    translateCodon = nucleotides[i:i + 3]
    print aminoAcids[translateCodon]