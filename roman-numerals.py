#! /usr/bin/python

import sys

L = "IVXLCDM "

def int2roman( num ):
    ma = (int(len(str(num)))-1)*2
    th = int(str(num)[0])

    return "%s%s%s%s" % (L[ma]*(th%5 == 4),\
        L[ma+(2 if th==9 else 1)]*(th >= 4),\
        L[ma]*(th%5)*(th%5 <= 3),\
        int2roman(str(num)[1:]) if ma > 1 else '')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        for i in range(1, 101):
            print "%d: %s" % (i, int2roman(i))
    else:
        if sys.argv[1] > 8999:
            print "Numbers greater than 8999 is not defined in roman numerals."
        print int2roman(sys.argv[1])

