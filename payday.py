"""payday.py

This program processes the two-dimensional list containing the day
of the week and the hours worked for that day.  It recognizes that
Saturday hours are paid at time and a half and Sunday hours are
paid at double time.  It prints the total of the results.
"""

pay_rate = 27
week = [['Sunday', 2],
        ['Monday', 8.5],
        ['Tuesday', 6.75],
        ['Wednesday', 9],
        ['Thursday', 9.25],
        ['Friday', 7.75],
        ['Saturday', 7.5]]

def isWeekday(s):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    for i in weekdays:
        if s==i:
            return(True)
        else:
            continue
    return(False)

totalpay = 0.0

for i in week:
    weekdayflag = isWeekday(i[0])
    if weekdayflag==True:
        weekdaypay = 27.0*i[1]
        totalpay+=weekdaypay
        print(i[0], "   \t", weekdaypay)
    elif i[0]=='Sunday':
        sundaypay = 27.0*2.0*i[1]
        totalpay+=sundaypay
        print(i[0], "  \t", sundaypay)
    elif i[0]=='Saturday':
        saturdaypay = 27.0*1.5*i[1]
        totalpay+=saturdaypay
        print(i[0], "\t", saturdaypay)
        
    else:
        print("You can't just make up a day of the week! Who do you think you are?")

print("Your total pay for the week is ${}".format(totalpay))
