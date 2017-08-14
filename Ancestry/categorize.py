# SUMMARY
# This program segregates genomes by region. 
# Differences in genomes are larger between regions than between the people within them. 
# Thus, it is possible to determine categorize genomes by large vs. small differences. 
# 
# The purpose of this program is to demonstrate basically how
# procedures like Geographical Population Structure (GPS) work.
# 
# Maxwell Sherman


def score(allGenes, i, j):
    gene1 = allGenes[i]
    gene2 = allGenes[j]
    score = 0
    
    for m in range(0, len(gene1)):
        if gene1[m] != gene2[m]: # count polymorphisms
            score += 1
    return score

def allScores(allGenes):
    scores = {}
    
    for i in range(0, len(allGenes)):
        for j in range(0, len(allGenes)):
            if i != j:
                scores[str(i) + "," + str(j)] = score(allGenes, i, j)
    return scores

def correlate(allGenes):
    groups = []
    
    for key in scores:
        if scores[key] < 300: # threshold for matching people (magic numbers > non-static global variables)
            people = map(int, key.split(","))
            group = 0
            hasNotAppended = True
            while group < len(groups) and hasNotAppended:
                if people[0] in groups[group] or people[1] in groups[group]:
                    groups[group].append(people[0])
                    groups[group].append(people[1])
                    hasNotAppended = False
                group += 1
            if hasNotAppended:
                groups.append([people[0]])
                groups[-1].append(people[1])
    
    fixedRepeats, fixedOverlaps = True, True
    while fixedRepeats or fixedOverlaps:
        groups, fixedRepeats = removeRepeats(groups, False)
        groups, fixedOverlaps = removeOverlaps(groups, False)
    
    return groups

def removeOverlaps(groups, fixedOverlaps):
    fixedOverlaps = False
    
    for i in range(0, len(groups)):                         # for each population
        # print "Comparing to:", groups[i] # DEBUG
        for j in range(0, len(groups)):                     # look at all the other populations
            if groups[i] != groups[j]:                      # (not itself).
                for person in groups[j]:                    # for each person in the each other population
                    if person in groups[i]:                 # if he's also in the initial population
                        for otherPerson in groups[j]:       # take the whole other population
                            # print otherPerson # DEBUG
                            groups[i].append(otherPerson)   # and add it to the first
                        groups[j] = []                      # then get rid of where the other population used to be
                        fixedOverlaps = True
    return groups, fixedOverlaps

def removeRepeats(groups, fixedRepeats):
    # print groups # DEBUG
    fixedRepeats = False
    for i in range(0, len(groups)):
        contents = []
        for person in groups[i]:
            if person not in contents:
                contents.append(person)
            else:
                fixedRepeats = True
        groups[i] = contents
        # print contents # DEBUG
    return groups, fixedRepeats

def format(groups):
    for i in range(len(groups)):
        groups[i].sort()
    for i in range(len(groups)): # This had to be in a separate loop because removing elements changes the test case
        if groups[i] == []:
            del groups[i]
    groups.sort()
    return groups

# MAIN

infile = open("/share/data/ancestry/figure-out2.txt", "r")
allGenes = infile.readlines()

scores = allScores(allGenes)
# print scores # DEBUG

groups = correlate(allGenes)

groups = format(groups)

# print groups
for population in groups:
    print population
