#Question 1
list=input("Enter the element bhai and be quick: ")
print(list)

#Question 2

list2=["google","apple","facebook","microsoft","tesla"]
list2.append(list)
print(list2)

#Question 3

print(len(list2))

#Question 4

num=[2,1,454,6,5,54,543,345,43,6,4345,45,543,56,345,546,43545,534,43]

print(sorted(num))

#Question 5

a=[12,13,15,16,17]
b=[18,19,20,21,24]
c=a+b
print(c)

#Question 6

for i in c:
    if i%2==0:
        print("even number")
    elif i%2==1:
        print("odd number")

#Question 7

tuple=(21,12,12,32,432,"Python", "java")

print(tuple[::-1])

#Question 8

t2=(12,2,45,76,67,3,3,5,6,7,4,234,45,34,6,34,46,35435,434,56,3,657,6,43,355,9)
print("Largest number: ",max(t2),"\nSmallest number: ",min(t2))

#Question 9

u = "Hey i'm here learning python from acadview in shoolini university"
print(u.upper())

n = "21"
print(n.isnumeric())



#Question 10
g="Hello world"
print(g.replace("world","Nisha"))
