#!/usr/bin/python3
def add_integer(c, b=98):
    if not isinstance(c, int) and not isinstance(c, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(c, float):
        c = int(c)
    if isinstance(b, float):
        b = int(b)
    return (c + b)

