"""
list_1=["apple" , "banana" , "cherry" , "orange" , "mango"]
print(list_1)
print(list_1[1])
print(list_1[-1])
print(list_1[1:3])

list_1[1]="black currant"
print(list_1)
print(len(list_1))
print(len(list_1[1]))

#list can contain any data type or even a mixture of data type
list_2=["1" , "true" , "adventure"]
print(list_2)
print(type(list_2))
"""

'''
new_list=list(("apple" , "banana" , "cherry" ))
if "apple" in new_list:
    print("yes,apple is in the list")
'''
#changing a range of items in the list
"""
new_list2=["apple" , "banana" , "cherry" , "orange" , "mango"]
print(new_list2)
new_list2[1:4]=["balling" , "curry", "oragano"]
print(new_list2)
new_list2[1:2]=["bailed", "baller"]
print(new_list2)
new_list2[1:5]=["gone"]
print(new_list2)

#adding a item intentionally
new_list2.insert(1,"long")
print(new_list2)
"""
#addting elements to the list using another way aside from insert
#
list1 = ["apple", "banana", "cherry"]
list1.append("orange")
print(list1)

#if done through insert i can place it anywhere
list1 = ["apple", "banana", "cherry"]
list1.insert(1,"orange")
print(list1)

#combining 2 lists

list2=["mango", "pineapple", "papaya"]

list1.extend(list2)
print(list1)

tuple1=("grapefruit" , "beans")
list1.extend(tuple1)
print(list1)