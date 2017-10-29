#!/usr/bin/env python3
import sys, random
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Please specify an input file and a count of points")
        exit(1)
    filename = sys.argv[1]
    count = int(sys.argv[2])
    with open(filename, 'w+') as f:
        for _ in range(count):
            val = str(random.randint(0, 9)) + " " + str(random.randint(0, 9)) + "\n"
            f.write(val)
    f.close()