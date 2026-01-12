def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multi(n1, n2):
    return n1 * n2

operations = { 
    "+" : add, 
    "-" : subtract, 
    "/" : divide, 
    "*" : multi
}

print(operations["+"](4, 3))