#!/usr/bin/env python3
import sys
from random import randrange

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Not enough paramaters")
        exit(1)

    N = sys.argv[1]
    with open(N + ".txt", "w+") as f:
        for _ in range(int(N)):
            f.write(str(randrange(int(N))) + "\n")
        f.close()
