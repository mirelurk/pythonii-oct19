
rawfile = open('tmpprecip.dat', 'r')

tpdata = []
yearprecip = []

for i in rawfile:
    year = i[4:8]
    precip = i[8:13]
    newrecord = [year, float(precip)]
    tpdata.append(newrecord)

def yearindex(y):
    for i in yearprecip:
        if i[0]==y:
            return(yearprecip.index(i))
        else:
            next
    newrecord = [y, 0.0]
    yearprecip.append(newrecord)
    return(yearprecip.index(newrecord))

for i in tpdata:
   ind = yearindex(i[0])
   yearprecip[ind][1]+=i[1]

yearprecip.sort()
for i in yearprecip:
    print("{}\t".format(i[0]), "{0:2f}".format(i[1]))
