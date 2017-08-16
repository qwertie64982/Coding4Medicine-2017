# sitting = [[0,0,0,0,1,0,0,0,0],
           # [0,0,1,0,0,1,0,0,0],
           # [0,1,0,0,0,1,0,0,0],
           # [0,0,0,0,0,0,0,0,1],
           # [1,0,0,0,0,0,0,0,0],
           # [0,1,1,0,0,0,0,0,0],
           # [0,0,0,0,0,0,0,1,0],
           # [0,0,0,0,0,0,1,0,0],
           # [0,0,0,1,0,0,0,0,0]]

sitting = [[0,1,1,1,1,1,1,1,1],
           [1,0,1,1,1,1,1,1,1],
           [1,1,0,1,1,1,1,1,1],
           [1,1,1,0,1,1,1,1,1],
           [1,1,1,1,0,1,1,1,1],
           [1,1,1,1,1,0,1,1,1],
           [1,1,1,1,1,1,0,1,1],
           [1,1,1,1,1,1,1,0,1],
           [1,1,1,1,1,1,1,1,0]]


people1 = {"Alex"    : 0,
           "Adithi"  : 1,
           "Brianna" : 2,
           "Amir"    : 3,
           "Max"     : 4,
           "Luca"    : 5,
           "Jared"   : 6,
           "Sid"     : 7,
           "Nithish" : 8}

people2 = {0: "Alex",
           1: "Adithi",
           2: "Brianna",
           3: "Amir",
           4: "Max",
           5: "Luca",
           6: "Jared",
           7: "Sid",
           8: "Nithish"}

target = raw_input("Enter name: ")
output = []

for i in range(0, len(sitting[people1[target]])):
    if sitting[people1[target]][i] == 1:
        output.append(people2[i])

print output