inSeq = open("puzzle-out.txt", "r")
sequence = inSeq.readline()

pieces = []
with open("puzzle.txt", "r") as infile:
    for line in infile:
        line = line.strip()
        line = line.split(",")
        for word in line:
            word = word.strip()
            if word != "":
                pieces.append(word)

isCorrect = True
for piece in pieces:
    if piece not in sequence:
        isCorrect = False
        break

print "Correct:", isCorrect