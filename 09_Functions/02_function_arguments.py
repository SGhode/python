def add(a, b, plus=0):
    x = a + b + plus
    return x


c = add(3, 5, 2)
print(c)

c1 = add(b=5, a=3)


# Default Arguments:

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet()) # Output: Hello, Guest!

# Keyword Arguments:

def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=20, name="Bob")
    











