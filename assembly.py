def isOverlap(word1, word2, wordLength, sampleSize):
    # print "Comparing %s and %s" % (word1, word2) # DEBUG
    i = 0
    foundMatch = 0
    if word1 != word2:
        while i < (wordLength - sampleSize) and not foundMatch:
            j = 0
            while j < (wordLength - sampleSize) and not foundMatch:
                if word1[i:i + sampleSize] == word2[j:j + sampleSize]:
                    foundMatch = 1
                    # print "Found match: %s and %s" % (word1[i:i+4], word2[j:j+4]) # DEBUG
                j += 1
            i += 1
    return foundMatch

def createOverlapsDict(pieces, overlaps, sampleSize):
    i = 0
    while i < len(pieces): # Creates table of overlapping words
        j = i # not 0 so that it never looks at things already compared
        while j < len(pieces):
            if isOverlap(pieces[i], pieces[j], wordLength, sampleSize):
                overlaps[pieces[i]] = pieces[j]
            j += 1
        i += 1

def join(word1, word2, wordLength):
    overlapSection = biggestOverlap(word1, word2, wordLength)
    
    i = 0 # remove overlap from word1
    joinComplete = 0
    joinedWord = "0"
    while i < (wordLength - len(overlapSection)) and not joinComplete:
        if word1[i:i + len(overlapSection)] == overlapSection:
            if i == 0: # if overlap is at the start of word1
                word1 = word1[i + len(overlapSection) - 1:len(word1)] # cut out overlap
                joinedWord = word2 + word1
            else: #elif (i + len(overlapSection)) == len(word1): # if overlap is at the end of word1
                word1 = word1[0:i] # cut out overlap
                joinedWord = word1 + word2
            # else:
                # print "ERROR: Cannot handle substrings"
                # print word1, word2
                # joinedWord = "0"
            joinComplete = 1
        i += 1
    return joinedWord

def biggestOverlap(word1, word2, wordLength):
    i = wordLength - 1
    while i >= 4:
        x = 0
        while x < (wordLength - i):
            if word1[x:x + i] in word2:
                return word1[x:x + i]
            x += 1
        i -= 1
    print "ERROR: Words compared have no overlap of 4 or greater"
    return "0"

pieces = []
biggerPieces = []
overlaps = {}
sampleSize = 4

with open("puzzle2.txt", "r") as infile:
    for line in infile:
        line = line.strip()
        line = line.split(",")
        for word in line:
            word = word.strip()
            if word != "":
                pieces.append(word)
wordLength = len(pieces[0])

# MAIN
# while len(pieces) > 1:
    # createOverlapsDict(pieces, overlaps, sampleSize)
    
    # for key in overlaps:
        # newWord = join(key, overlaps[key], wordLength)
        # biggerPieces.append(newWord)
    
    # pieces = biggerPieces
    # biggerPieces = []
    
    # print pieces

# print pieces

createOverlapsDict(pieces, overlaps, sampleSize)
print overlaps

for key in overlaps:
    newWord = join(key, overlaps[key], wordLength)
    print "%s + %s = %s" % (key, overlaps[key], newWord)
    biggerPieces.append(newWord)

pieces = biggerPieces
biggerPieces = []

createOverlapsDict(pieces, overlaps, sampleSize)

for key in overlaps:
    newWord = join(key, overlaps[key], wordLength)
    print "%s + %s = %s" % (key, overlaps[key], newWord)
    biggerPieces.append(newWord)

pieces = biggerPieces
biggerPieces = []

outfile = open("puzzle-out.txt", "w+")
outfile.write(pieces[0])
outfile.close()