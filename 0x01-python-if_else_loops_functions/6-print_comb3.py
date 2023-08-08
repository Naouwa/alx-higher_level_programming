#!/usr/bin/python3
for digit1 in range(10):
    for digit2 in range(10):
        if digit1 < digit2:
            print("{}{}".format(digit1, digit2), end="")
            if digit1 < 8:
                print(", ", end="")
print()
