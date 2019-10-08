import string

for i in range(32, 126):
    print("{!r}\t{}".format(chr(i), i))

for i in string.printable:
    print("{}\t{!r}.".format(ord(i), i))
