import random


def dice():
    roll1 = random.randrange(1, 7)
    roll2 = random.randrange(1, 7)
    return(roll1+roll2)

count = 0

outcome = 11 * [0]

while count < 100001:
    roll = dice()
    outcome[roll-2]+=1
    #print(roll, "\t", outcome)
    count+=1

print(sum(outcome))

for i in outcome:
    print("Dice roll {} \t{} \t{}%.".format(outcome.index(i)+2, i, 
        round((i/sum(outcome)*100), 2)))
