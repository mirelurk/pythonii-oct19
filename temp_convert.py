"""Temperature Conversion

This program converts one temperature from fahrenheit to centigrade
(in a void or fruitless function) and prints the results. 
Change it to handle a variable number of temperatures to covert and
print in the function.
"""

def fahrenheit_to_centigrade(*xtmp):
    for i in xtmp:
        if isinstance(i, (int, float)):
            nutmp = 5.0 / 9.0 * (i - 32)
            print('{0:.1f} degrees Fahrenheit is {1:.1f} degrees Centigrade'.format(
                i, nutmp))
        else:
            print("Enter a number ya dang hooligan!")
    

fahrenheit_to_centigrade(72, 89, 65, 'a', '%', 8.0)
    

