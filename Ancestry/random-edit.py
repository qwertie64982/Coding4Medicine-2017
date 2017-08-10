# SUMMARY
#
# This program opens a gene file and alters the user-defined
# number of genes. It writes the changed gene to another file.
#
# The purpose of this program is to aid in an experiment where
# one must segregate people by ancestry by analyzing their genes.
# 
# Maxwell Sherman

from random import randint

file = open("south-america", "r")
gene = list(file.readline())
howManyEdits = int(raw_input("How many edits: "))
nucleotideConversion = {0: "A", 1: "T", 2: "C", 3: "G"}

i = 0
while i < howManyEdits:
    geneLocation = randint(0, len(gene) - 1)
    currentNucleotide = gene[geneLocation]
    gene[geneLocation] = nucleotideConversion[randint(0, 3)]
    if gene[geneLocation] == currentNucleotide:
        continue
    i += 1
file.close()

file = open("person1", "w")
output = ''.join(gene)
file.write(output)