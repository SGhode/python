# Append to an existing file called Shivraj Ghode.txt
# it should add data about Shivraj Ghode's Hometown

f = open("Shivraj Ghode.txt", "a")

string = '''
Shivraj Ghode initially lived in Phoenix Arizona. He is a very nice guy
'''
f.write(string)

f.close()