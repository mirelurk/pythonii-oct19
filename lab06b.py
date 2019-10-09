from random import randrange as rand

matching = 0
notmatching = 0

for i in range(1,100):
    birthdays = [rand(0,366) for i in range(0,23)]
    birthdays = set(birthdays)
    if len(birthdays)==23:
        notmatching+=1
    elif len(birthdays) < 23:
        matching+=1
    else:
        print("I dunno, whatever.")
    
print("Matching: {}".format(matching))
print("Not matching: {}".format(notmatching))
