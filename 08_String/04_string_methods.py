# name = "Shivraj" # String are immutable
# s = " i love my Car "

# name[0] = "R" # You cannot do this

# a = len(name)
# print(a)

# print(len(s))
# print(s.lower(),s)
# print(s.lower())
# print(s.upper())

# print(s.capitalize()) # capitalize the first letter of the string
# print(s.title()) # capitalize the first letter of each word of string

# text = " I have a Defender "
# print(text.strip()) # Output: "I have a Defender"
# print(text.lstrip()) # Output: "I have a Defender "
# print(text.rstrip()) # Output: " I have a Defender"

# text = "Python is fun is fun is fun"
# print(text.find("is")) # Output: 7
# print(text.replace("fun", "awesome"))

text = "Apples,Bananas,Pineapples"

print(text.split(","))
print(",".join(['Apples', 'Bananas', 'Pineapples']))


text = "Shivraj18"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False


