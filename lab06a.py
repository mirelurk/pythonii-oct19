import string

rawfile = open('alice_in_wonderland.dat', 'r')

aiw = rawfile.read()

characters = {}

total = 0

for i in aiw:
    if i in string.whitespace:
        continue
    elif i in characters:
        characters[i]+=1
        total+=1
    elif i not in characters:
        characters[i]=1
        total+=1
    else:
        print("Something went wrong")

print(characters)

sortedcharacters = sorted(characters.items(), key=lambda x : x[1])

for i in sortedcharacters[-1:-31:-1]:
    print("{} appeared {} times, {}% of the total characters.".format(i[0],
        i[1], (i[1]/total)*100))
