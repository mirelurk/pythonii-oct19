from random import randrange as rand

def generateBdays(n):
    birthdays = []
    for i in range(1,n+1):
        newdate = rand(1,366)
        birthdays.append(newdate)
    return(birthdays)

matching = 0
notmatching = 0
    
for i in range(1,100):
    birthdays = generateBdays(23)
    bdaycount = [birthdays.count(i) for i in birthdays]
    count = bdaycount.count(1)        
    if count==23:
        notmatching+=1
    else:
        matching+=1

print("Matching: {}".format(matching))
print("Not matching: {}".format(notmatching))
