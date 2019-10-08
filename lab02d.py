
rawdata = open('alice_in_wonderland.dat', 'r')

aiw = rawdata.read()
aiw = aiw.lower()

def printdata(word):
    print("Word is ", word)
    print("The location of the first occurence is", aiw.find(word))
    print("The location of the last occurence is", aiw.rfind(word))
    print("The number of occurences is ", aiw.count(word))

printdata("caterpillar")
printdata("gryphon")
printdata("alice")
printdata("cheshire")
rawdata.close()
