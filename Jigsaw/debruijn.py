# DOCUMENTATION (explain args too)

from bidict import bidict
import sys

pieces = []
kmers = []
debruijn = bidict()

# filename = raw_input("Filename: ")
filename = sys.argv[1]
if filename[-4:] == ".csv":
    with open(filename, "r") as infile:
        for line in infile:
            line = line.strip()
            line = line.split(",")
            for word in line:
                word = word.strip()
                if word != "":
                    pieces.append(word)
elif filename[-4:] == ".txt":
    with open(filename, "r") as infile:
        for line in infile:
            line = line.strip()
            pieces.append(line)
else:
    print "Unsupported filetype."
    exit(0)

# kSize = int(raw_input("k-size: "))
kSize = int(sys.argv[2]) # 13 is good for puzzle.csv
overlapSize = kSize - 1
leftover = kSize - overlapSize

# make kmers
for piece in pieces:
    for i in range(0, len(piece) - kSize + 1):
        # if piece[i:i + kSize] not in kmers:
        kmers.append(piece[i:i + kSize])

# build debruijn graph
for i in range(0, len(kmers)):
    for j in range(0, len(kmers)):
        if i != j: # don't look at itself
            # print "Testing if %s is %s" % (kmers[i][leftover:], kmers[j][:overlapSize])
            if kmers[i][leftover:] == kmers[j][:overlapSize]:
                # print "%s and %s make %s" % (kmers[i], kmers[j], (kmers[i] + kmers[j][-leftover:]))
                debruijn[kmers[i]] = kmers[j]

# assemble from graph
finalString = debruijn.keys()[20] # just picked a random number, no puzzle will ever have < 20 pieces

while finalString[-kSize:] in debruijn.keys(): # build to the right
    finalString = finalString + debruijn[finalString[-kSize:]][-leftover:]
# print finalString[-kSize:], "not in", debruijn.keys() # DEBUG
while finalString[:kSize] in debruijn.values(): # build to the left
    finalString = debruijn.inv[finalString[:kSize]][:leftover] + finalString
# print finalString[:kSize], "not in", debruijn.values() # DEBUG
print finalString

outfile = open("puzzle-out.txt", "w+")
outfile.write(finalString + "\n")