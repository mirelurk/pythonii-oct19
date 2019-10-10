
tmpprecipraw = open('tmpprecip.dat', 'rt')

initdata = []

for i in tmpprecipraw:
    month = int(i[:2])
    day = int(i[2:4])
    year = int(i[4:8])
    precip = float(i[8:13])
    temp = float(i[13:])
    newrecord = [month, day, year, precip, temp]
    initdata.append(newrecord)


