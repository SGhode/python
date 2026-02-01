# Write a file called Shivraj Ghode.txt
# it should contain data about Shivraj Ghode

f = open("Shivraj Ghode.txt", "w")

string = '''
Shivraj Ghode is a software developer
with a passion for coding and technology.
'''
f.write(string)

f.close()