# SUMMARY
# This program is a Hidden Markov Model exercise
# that determines when a coin flip probability changes.
# For example, the first coin may be very fair,
# and the second coin may be very biased towards heads. 
# This program detects the most likely place in coin flip data
# where the coin changes. 
# 
# The purpose of this program is to demonstrate how
# genetic sequencing technology makes educated guesses.
# 
# Maxwell Sherman

# Returns the maximum likelihood for any probability
def maxLikelihood(string):
    data = {"H": 0.0, "T": 0.0}
    
    for character in string:
        if character == "H":
            data["H"] += 1
        elif character == "T":
            data["T"] += 1
    
    p = (data["H"] / (data["H"] + data["T"])) # heads probability
    return (p ** data["H"] * (1 - p) ** data["T"])

# Returns likelihoods, filled with the products of the maximum likelihoods for any probability in both halves
def findLikelihoods(string):
    likelihoods = []
    splitLocation = 1
    while splitLocation < len(input):
        likelihoods.append(maxLikelihood(input[:splitLocation]) * maxLikelihood(input[splitLocation:]))
        splitLocation += 1
    return likelihoods

# Returns the split location that gives the highest probability likelihood
def findLocation(likelihoods):
    biggestLikelihood = float("-inf")
    biggestLikelihoodLocation = 0
    i = 0
    while i < len(likelihoods):
        if likelihoods[i] > biggestLikelihood:
            biggestLikelihood = likelihoods[i]
            biggestLikelihoodLocation = i + 1
        i += 1
    return biggestLikelihoodLocation

input = "THHTHHHHHHTHTTHHTHTHHHHHTHTTTTHTHHTHTTHHHTHTTHHTTHHHTTHHTTTHTTTTTHHHTHHTTHTHTTHTHTTHTTTHTTTTHTHTTTTTTTHHTTTTHHHHHHTHTTHTHHHHHHHHHTHHHHHHHHHHHTHHHHHHHHHHHTHHHHHHHHHHHHHHHTHHHHHHHHHHHTHHHHHTHHHHHHHHHHHT"

likelihoods = findLikelihoods(input)
bestLocation = findLocation(likelihoods)

print input[:bestLocation], input[bestLocation:]
print "Location:", bestLocation
