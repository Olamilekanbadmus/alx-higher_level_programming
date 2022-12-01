#!/usr/bin/python3
if _name_ == "_main_":
    from sys import argv
    userin = argv[1:]
    size = len(userin)
    print("{:d} {:s}{:s}".
          format(size,
                 "arguments" if (size) != 1 else "argument",
                 "." if (size) == 0 else ":"))
    for idx, arg in enumerate(userin):
        print("{:d}: {:s}".format(idx + 1, arg))
