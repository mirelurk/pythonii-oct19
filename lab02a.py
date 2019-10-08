
rawfile = open('alice_in_wonderland.dat', 'rt')

aiw = rawfile.read()

def countletters(text):
    count = 0
    ecount = 0

    for i in text:
        if i>='A' and i<='z':
            count+=1
            if i=='e' or i=='E':
                ecount+=1
    return([count,ecount])

results = countletters(aiw)
percente = round((results[1]/results[0])*100, 1)

print("Total letters: {}".format(results[0]))
print("Total e's: {}".format(results[1]))
print("Percent of e's:", percente, "%")
