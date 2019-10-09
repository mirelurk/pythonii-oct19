
rawdata = open('tmpprecip.dat', 'r')

tmpdata = []

for i in rawdata:
    day = int(i[0:2])
    mon = int(i[2:4])
    year = int(i[4:8])
    precip = float(i[8:13])
    temp = int(i[13:])
    newrecord = [day, mon, year, precip, temp]
    tmpdata.append(newrecord)

"""
record reference for months list:

0 - month
1 - total temp
2 - count temp
3 - max temp
4 - min temp
"""

"""
record reference for tmpdata:
0 - month
1 - day
2 - year
3 - precip
4 - temp
"""

months = []

for i in range(0,13):
    months.append([i,0,0,0,1000])

def monthindex(m):
    #input integer of month
    #output index reference within month list
    for i in months:
        if m==i[0]:
            return(months.index(i))
        else:
            next
    return(-1)

for i in tmpdata:
    monind = monthindex(i[0])
    months[monind][1]+=i[4] #add to total temp
    months[monind][2]+=1 #adding one to temp count
    if months[monind][3] < i[4]: #checking and setting max temp
        months[monind][3] = i[4]
    if months[monind][4] > i[4]: #checking and setting min temp
        months[monind][4] = i[4]

for i in months:
    try:
        print("Month {} \t {} high temp \t {} low temp \t {} avg temp".format(i[0], i[3], i[4],
            round((i[1]/i[2]),2)))
    except ZeroDivisionError:
        continue
