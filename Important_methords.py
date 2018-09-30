l = [10,20,60,"python", "java",'perl']
l.reverse()
print(l)


def only_upper(s):
    upper_chars = ""
    for char in s:
        if char.isupper():
            upper_chars += char
    return upper_chars

print(only_upper("HeLLo WorLD"))

s =input("Enter the element: ")
print(s.split(","))

s = input("Enter the string: ")
if s==s[::-1]:
    print("palindrom")
else:
    print("not a palindrom")

import copy
List=[12,14,15,54,"Python","Java"]
list2=List
list3 = copy.deepcopy(List)
print("Shallowcopy: ",List,id(List))
print("Shallowcopy: ",list2,id(list2))
print("Deepcopy: ",list3,id(list3))









