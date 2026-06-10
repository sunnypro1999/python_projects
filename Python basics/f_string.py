#using of F string to print out a statement with variables and int
"""
name = "sunnypro1999"
age = 27
#print(f"hello there my name is {name} and i am {age} years old")    
#saving it to a text then printing it out
greeting = f"hello there my name is {name} and i am {age} years old" 
#need to start with f before the inverted commas to use the f string
#we are using f because we are then able to print the value of the variables
print(greeting)
"""
#another practice of using f string to print out a statement with variables and int
"""
price = 17.44
welcome = f"The price of the single entry is {price} dollars"
print(welcome)

#using f string to print out a statement with variables and int and doing math in the f string

total_price = f"Your total price for today's climbing session is {17.44 +5.45} dollars"
print(total_price)


#printing of int number in a f string and displaying 2 decimal places

amount_left= f"I have {10:.2f} dollars left in the bank" 
print(amount_left)

amount_left= f"I have {10:010.2f} dollars left in the bank" 
print(amount_left)
"""

#f string formatting a ratio into a percentage

#ratio_a = 0.6767
#print(f"{ratio_a:.2%}")

n = int(input())
    
while n in range(0, n):
    print(n**2)
    n += 1
print(n**2)