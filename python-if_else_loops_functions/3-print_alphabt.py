#!/usr/bin/python3
print("{}".format("".join(
    [chr(c) for c in range(97, 123) if c != 101 and c != 113])), end="")
