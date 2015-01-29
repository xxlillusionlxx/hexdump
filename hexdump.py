#! user/bin/python3

import sys
import string
import binascii

__author__ = 'jason'

def hexdump():

    if(sys.argv.__len__() < 2):
        print("Enter a filename");
        return

    file = sys.argv[1]

    try:
        fd = open(file, 'rb')
    except IOError as e:
        print(e)

    with open(file, 'rb') as f:
        bCount = 0; # byte count used for later when printing out amount of bytes used in hexadecimal
        while 1:
            bytes = f.read(16)
            bCount += 16;

            if not bytes: # check for end of file; python returns empty string when it reaches eof. this empty string is interpreted as false
                break

            #set up the strings for each part to be joined later in printing
            hexes = ["%02x" %b for b in bytes]
            ascii = ["%02d" % int(str(c)) for c in bytes] # ascii decimal numbers
            byteRep = ["%08.2X" % bCount]

            display(hexes, ascii, byteRep)

def display(hexes, ascii, byteRep):

    letters = '' # hold the ascii chars for each line

    for j in ascii:
        char = int(j)
        if char >= 32 and char < 128: # only allow this range of characters to be printed / concatenated to the string.
            letters += chr(char) + " "
        else:
            letters += ". "

    print(" ".join(byteRep) ,  "  ".join(hexes), " | ", "".join(letters), "|", end='')
    print()

if __name__ == '__main__':
    hexdump()

