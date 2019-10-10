import numpy as np

rawdata = open('tmpprecip.dat', 'rt')

initdata = []

for i in rawdata:
    month = int(i[:2])
    day = int(i[2:4])
    year = int(i[4:8])
    precip = float(i[8:13])
    temp = float(i[13:])
    newrecord = [month, day, year, precip, temp]
    initdata.append(newrecord)

tmpprecip = np.array(initdata)

yearindex = []

for i in tmpprecip:
    
