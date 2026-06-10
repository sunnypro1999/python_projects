
#prompting the user name then printing it out
"""
print("What is your name?")
name = input() #name is the variable that will store what the user inputs 
print("Hello", name + " nice to meet you!")
print(f"hello there {name}") #this is a f string and it is a way to format strings in python and it is a more efficient way to format strings than using the + operator
#print(f "Hello there (name) ")
#print(f "Hello there [name] ")
#both outputs will give an error
#because the variable name is not being recognized as a variable but as a string
"""



#prompting the userfor multiple inputs and then printing them out
"""
print("What is your name?")
input_name =input()
print("what is your age?")
input_age = input()
print("What is your favorite color?")
input_color = input()

print("Hello", input_name, "nice to meet you!")
print("Oh WOW you are", input_age, "years old!")
print("lovely, your favorite color is", input_color)

print(f"hello there {input_name} , nice to meet you! you are{input_age} year old and wow your favorite color is {input_color}")
"""
# i can also get a input and print out my prompt in the same line like this
"""
name = input("what is your name?")
age  = input("what is your age")

print("Hey there", name , "nice to meet you",end=" ")
print("Oh you are", age,"Years old")

print(f"Hey there {name}, nice to meet you! Wow you are {age} years old, the same as me")
"""
# after i key in the word print and place an open bracket then use "f" i dont need to put another braket


#inputing number then printing it out
#when i prompt the user for a inpite it will be always be stored as a string 
#so i need to convert it into a number through using int() for whole numbers
#and float() for decimal numbers
#so when i try to do math will work only if i convert the data type of the input into a number

import math


x_1 = input("Give me a whole number")
print(x_1)
print(type(x_1))
#doing math i will convert the data type of the input into a number and find the square of the number
y= math.sqrt(float(x_1))
print(type(y))
print(y)

print(f"the quare root of {x_1} is {y}")

x_1 = int(x_1)
#square the number
print(x_1**2)

#square root of the number
print(x_1**0.5)


"""
x_2 = input("Give me a decimal number")
print(x_2)
print(type(x_2))
x_2 = float(x_2) #converting the data type of the input into a decimal number
print(type(x_2))
#square the number
print(x_2**2)
#square root of the number
print(x_2**0.5)
"""

