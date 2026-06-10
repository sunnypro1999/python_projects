
#this is to play with variables and see how they work.
a = 27  # this is a intergier variable
b = "Chasvinder" #this is a string variable

"""
This is a print statement that will print
both name and age variable 
"""
print (b,'is',a,'years old') 

"""
#Declaring a variable and assigning a data type to it
# declaring the data type in python is know as "casting"

c = str(5) #string variable str() printed 5
d = int(5) #integer variable int() printed 5
e = float(5) #float variable float() printed 5.0
f = float(123456789.123456789) #float variable float() printed 123456789.12345679
g = bool(-5.1235)
h = bool(0)

print(c)
print(type(c))

print(d)
print(type(d))

print(e)
print(type(e))

print(f)
print(type(f))
"""

#implementing of variables and showing what names we can use for variables in python
#it cannot start wih a number but it can start with a letter or a _ underscore
#but u can have numbers in it , but just not in the beggining of naming the variable

myname = "sunny"
_myname = "sunny"
my_name = "sunny"
myname1234 = "sunny"
MyName ="sunny"

#not allowed
#123myname = "sunny"
#my-name = "sunny" only _ underscore is allowed not - hyphen
#my name = "sunny" #space is not allowed in variable names

"""
#many variables can be assigned in one line and here is how to do it
a,b,c ="apple","banana","cherry"

#print the variables
print(a)
print(b)
print(c)

#new sets of variables mixed with different data types
e,f,g = "sunny", 27 , 3.14
print(e)
print(type(e))

print(f)
print((type)(f))

print(g)
print(type(g))

#assigning the same value to mltiple variables in one line

x = y = z ="curry"
print(x)
print(y)
print(z)
"""
"""
#making a list and storing it into a variable and then printing it
FirstList =("apple","banana","cherry")  #this is a tuple because of the ()
print(FirstList)
x,y,z = FirstList
print(x)
print(y)
print(z)
#unpacking is when you have a collection of values in a variable
#you want to assign them to multiple variables in one line.


#SecondList = ["Apple","Banana","Cherry"] #this is a list because of the []
#print(SecondList) 

#ThirdList ={"applE","bananA","cherrY"} #this is a set because of the {} and it will not print in the same order as it is written because sets are unordered collections of unique elements.
#print(ThirdList)

"""


#output variables
#a ="learning"
#print(a)

#printing multiple variables in one print statement
#b = "python"
#c = 'from scratch'
#print(a,b,c)

#print(a+b+c)  # it prints the statement without any spacing between the variables

#with numbers
"""
x= 10
y= 25
print(x+y) # it will print 35 because it is adding the two numbers together 
print(x-y) # it will print -15 because it is subtracting the two numbers
print(x*y)# this will print out the multiplication of the two numbers which is 250
print(x/y) # this will print out the division of the two numbers which is 0.4
print(x%y) # this will print out the modulus of the two numbers which is 10
"""

#when combining a string and a number
aa= "I am "
bb = 27
#print(aa + bb) this will give me an error because you cannot combing a string and a number like this
#but you can do this


#print(aa + str(bb)) 


# this will print "I am 27" because we are converting the number 27 into a string 
#using the str() function so that it can be combined with the string "I am "

#it could also be done like this
#print(aa , bb)


#global variables and local variables
#outside a function if a variable is declared it is then a global variable that can be used anywhere in the code
"""
x = "global variable"

def first_function():
    print(x)

first_function()


#now for a local variable that can onle be used inside tat function

def second_function():
    y = "local variable"
    print(y)

second_function()
#print(y) this will give an error
# that is because 'y' is a local variable and it can't be used outside it's function

"""
"""
x  = "global variable"

def combine_variables():
    y = " Local variable"
    print(x+y)

combine_variables()

"""
# using the same variable name for both a global and local variable

"""
x = "learning python"

def combi_x():
    print("i am" + x)
    print("i am", x)

combi_x()
"""

#Create a variable inside a function, with the same name as the global variable
"""
x = "better at this"

def milti_x():
    x =" I am "
    print (x + "getting better at this")

milti_x()

print("Am I " + x)
"""
#in the function the local variable x is used , while the global variable x is used for the outside function

#creating a global variable inside a function then using it outside
"""
def creating_global():
    global g
    g = "g is now a global variable that will be used outside this function"
creating_global()

print("testing" , g) """

#chaging the value of the global variable from inside a function
"""
x = "first"
print (x)

def changing_global():
    global x
    x = " second "

changing_global()
print(x)
"""


#multiple line string in to one variable
'''
multi_line_string = """ this is a multiple statement string,
second line of the string,
last line of the string"""
print(multi_line_string)

'''


#converstion of data types
#when i convert a data type into another data type it is called "casting"
"""
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))


x=(float(x))
print(x)
print(type(x))

y=(complex(y))
print(y)
print(type(y))


z=(int(z))
print(z)
print(type(z))

#complex number cant be converted into int
#it needs to be a real number first, string  or byte
#cannont convert complex number into anoter number type
#but it can be converted into a string 
z=(str(z))
print(z)
print(type(z))
"""
