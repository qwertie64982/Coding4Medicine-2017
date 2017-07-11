infile = open("states.txt", "r")
states = dict()

for line in infile:
    state = line
    stateAbb = state.rsplit()[0]
    stateName = state.rsplit()[1]
    states[stateAbb] = stateName

x = raw_input("x=")
print "State's full name is",
print states[x]