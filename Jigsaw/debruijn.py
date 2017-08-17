from bidict import bidict

pieces = []
kmers = []
debruijn = bidict()

with open("puzzle.txt", "r") as infile:
    for line in infile:
        line = line.strip()
        line = line.split(",")
        for word in line:
            word = word.strip()
            if word != "":
                pieces.append(word)

kSize = 13 # UI later
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
            # print "Testing if %s is %s" % (kmers[i][kSize - overlapSize:], kmers[j][:overlapSize])
            if kmers[i][kSize - overlapSize:] == kmers[j][:overlapSize]:
                # print "%s and %s make %s" % (kmers[i], kmers[j], (kmers[i] + kmers[j][overlapSize - kSize:]))
                debruijn[kmers[i]] = kmers[j]

# assemble from graph
finalString = debruijn.keys()[20]

while finalString[-kSize:] in debruijn.keys(): # build to the right
    finalString = finalString + debruijn[finalString[-kSize:]][overlapSize - kSize:]
# print finalString[-kSize:], "not in", debruijn.keys() # DEBUG
while finalString[:kSize] in debruijn.values(): # build to the left
    finalString = debruijn.inv[finalString[:kSize]][:kSize - overlapSize] + finalString
# print finalString[:kSize], "not in", debruijn.values() # DEBUG
print finalString

outfile = open("puzzle-out.txt", "w+")
outfile.write(finalString + "\n")