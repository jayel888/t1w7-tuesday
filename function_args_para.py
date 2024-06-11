# Greet someone
def greet():
    print("Hello Coder, Jess!!")

greet()

def greet():
    print("Hello Coder, Sharla!!")

greet()

# Generalised coding
def greet(name): # <---- Parameter
    print(f"Hello Coder, {name} ")

greet("Beast")

def greetings(fname, lname):
    print(f"Hello Coder, {fname} {lname}")

greetings("max", "fury")

def subtract(a, b=1):
    difference = a - b
    return difference

result = subtract(a=4, b=7)

print(result)