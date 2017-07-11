infile = open("states.txt", "r")
states = dict()

for line in infile:
    state = line
    state = state.split()
    stateAbb = state[0]
    if len(state) > 2:
        stateName = state[1] + " " + state[2]
    else:
        stateName = state[1]
    states[stateAbb] = stateName

x = raw_input("x=")
print "State's full name is",
print states[x]