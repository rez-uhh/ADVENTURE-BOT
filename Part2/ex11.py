def add_two(x):
    return x + 2
print(add_two(4))
result = add_two(8)
print(result)

def calculate(a, operation, b):     
    if operation == "/":
        return a / b
    if operation == "*":
        return a * b
    if operation == "-":
        return a - b
    if operation == "+":
        return a + b
print(calculate(10, "+", 10))
print(calculate(10, "-", 10))  
print(calculate(10, "*", 10))  
print(calculate(10, "/", 10))  