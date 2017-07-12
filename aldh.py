# SUMMARY
# This program reads genetic-code.txt into a dictionary
# and uses the dictionary to convert nucleotides from an input file
# into a string of proteins, which is written to protein.txt.
# 
# genetic-code.txt must be formatted such that each line consists of 
# one codon, a whitespace, and its amino acid abbreviation.
# Example: 
# AAA K
# 
# The purpose of this program is to convert raw genetic information
# into chains of amino acids (proteins), which allow better analysis. 
# For example, different species may have different genetic code
# but produce the same proteins. 
# 
# Maxwell Sherman

infile = open("genetic-code.txt", "r")
aminoAcids = {}

for line in infile:
    key = line
    key = key.split()
    inCodon = key[0]
    inAmino = key[1]
    aminoAcids[inCodon] = inAmino 

infile.close()
# infile = open("ALDH.txt", "r")
infile = open("random-gene.txt", "r")
outfile = open("protein.txt", "w+")

nucleotides = infile.readline()
nucleotides = nucleotides[:-1]
for i in range(0, len(nucleotides), 3):
    translateCodon = nucleotides[i:i + 3]
    outfile.write(aminoAcids[translateCodon])
print "Written to protein.txt"