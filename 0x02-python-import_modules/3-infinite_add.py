#!/usr/bin/python3

import sys

length = len(sys.argv)
sum = 0
if __name__ == "__main__":
    if length == 1:
        sum = 0

    else:
        for i in range(1, length):
            sum += int(sys.argv[i])
    print("{:d}".format(sum))        
