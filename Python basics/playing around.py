text="\113\111\114\114 \115\105"
print(text)

txt = "welcome"
print(txt[3:5]) #you dont print the last index, meaning i'm printing character 3 and 4 only not 5 as well
x=txt[3:5]
print(x)
print(len(txt))

check_text = "there is nothing free in this world"
if "nothing" in check_text:
    print("yes,\"nothing\" is present in the statement")

greeting_1="hey there my name"

name_1=("chas")
print(type(name_1))

print("Hey there my name is,", name_1)
print(f"Hey there my name is,{name_1}")


print(bool("hello"))#testing to see if this is the string is 
print(bool(""))#empty string so a false statement will come out
print(bool(" "))# there is a space inside the ""
print(bool())#the bool is empty hence a false will be printed
print(bool(0))#because the value is 0
print(bool(-21))
print(bool(21))
#container() has to be empty for it to be a true false value
print(bool(None))

