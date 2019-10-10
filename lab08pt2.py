import string

rawsplit = open('split.txt', 'rt')

splitread = rawsplit.read()

split = splitread.lower()

uniqueset = set()

for i in string.punctuation:
    split = split.replace(i, ' ')

split = split.split()

for i in split:
    uniqueset.add(i)

print("Total words:", len(split))
print("Unique words:", len(uniqueset))

rawsplit.close()
