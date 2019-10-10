
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

yeardata = {}
#year: [total rainfall, max temp, min temp, count, total temp]

monprecip = {}
#month: [total precip, total temp, count]

months = {}
#month: list of all total from a year

def high(x, y):
    if x > y:
        return(x)
    elif x < y:
        return(y)
    elif x==y:
        return(x)
    else:
        print("Error in high")

def low(x, y):
    if x < y:
        return(x)
    elif x > y:
        return(y)
    elif x==y:
        return(x)
    else:
        print("Error in low")

def add_to_yeardata(y, temp, precip):
    if y in yeardata:
        curr = yeardata[y]
    else:
        yeardata[y] = [0, 0, 1000, 0, 0]
        curr = yeardata[y]
    #print("curr=", curr)
    newdata = [curr[0]+precip,
            high(curr[1], temp),
            low(curr[2], temp),
            curr[3]+1,
            curr[4]+temp]
    yeardata[y] = newdata

def data_by_year():
    for i in initdata: 
        add_to_yeardata(i[2], i[4], i[3])
    printyear()

def printyear():
    for i in yeardata:
        data = yeardata[i]
        year = i
        totalprecip = data[0]
        avgtemp = data[4]/data[3]
        hightemp = data[1]
        lowtemp = data[2]
        print("{:<5}Total Rain:{:.2f} High temp:{:.2f} Low temp:{:.2f} Avg temp:{:.2f}"
                .format(year, totalprecip, hightemp, lowtemp, avgtemp))

def resetmonths():
    for i in range(1,13):
        monprecip[i] = [0, 0, 0]
 

def month_before_1970():
    
    printmonth()
    resetmonths()

#resetmonths()

data_by_year()

"""
data_by_month(0, 2017)
print("To 1970")
data_by_month(0, 1970)
print("Since 1970")
data_by_month(1970, 3000)
"""
