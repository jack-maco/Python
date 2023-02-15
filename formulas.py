import sys

def add (values):
    sum = 0
    for x in values:
        sum = sum + x
    return sum

def subtract(values):
    dif = values[0]*2
    for x in values:
        dif = dif - x
    return dif

def multiply(values):
    prod = 1
    for x in values:
        prod = prod * x
    return prod

def divide(values):
    quo = values[0]
    if values[0] == 0:
        quo = 0
    else:
        for x in values[1:]:
            if x == 0:
                sys.exit("Cannot divide by 0")
            quo = quo / x
    return quo
