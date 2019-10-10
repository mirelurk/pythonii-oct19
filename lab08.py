
rawgdp = open('gdp.txt', 'rt')

gdp = rawgdp.read().split('\n')
#gdp is now a list containing strings in the format 'country,population,gdp'

gdpperson = []
#a 2d list with each item being a list in format [gdp per person, country]

for i in gdp:
    data = i.split(',')
    #print("Data = ", data)
    #list containing [country name, population, gdp]
    try:
        gdppp = (1000000*int(data[2]))/int(data[1])
        newrecord = [gdppp, data[0]]
        gdpperson.append(newrecord)
    except IndexError:
        continue

gdpperson.sort()
gdpperson.reverse()
print("Country\tGDP per person")

for i in gdpperson:
    print("{:}\t\t{:15.2f}".format(i[1],i[0]))

rawgdp.close()
