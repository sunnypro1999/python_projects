
#forcig the statement to be in upper and lower cases then removing spaces
a="Hello, World!"
print(a.upper())

b="HELLO, WORLD!"
print(b.lower())

c=" Hello, World! " # this is a string with spaces at the beginning and end
print(c)
print(c.strip()) 

#replacing a word/letter in a string
d="welcome to the game of dead by sunlight"
print(d.replace("sunlight", "daylight"))

print(d.replace("e", 'a'))


#splitting a string into a list of strings
d="welcome to the game of, dead by sunlight"
print(d.split()) # this will split the string into a list of strings based on the space character

print(d.split(","))

#making the first letter of each word in a string to be capitalized
e="welcome to the game of dead by sunlight"
print(e.capitalize())

#making every letter aside from the first letter of each word in a string to be capitalized
e="welcome to the game of dead by sunlight"
print(e.title())

#making every letter that is not the first letter of each word in a string to be capitalized
f="Welcome To The Game Of Dead By Daylight"
print(f.swapcase())

e="welcome to the game of dead by daylight test 2"
e=e.title()
print(e.swapcase())