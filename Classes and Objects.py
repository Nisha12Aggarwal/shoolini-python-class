#Question 1


n1=int(input("enter total number of keys: "))
d1={}
for i in range(1,n1+1):
    v=input("enter value of key: ")
    d1[i]=v
l=[]
for j in d1:
    l.append(j)
print("keys of dictionary is: ",l)
#Question 2

nested_dict = {1 : {'name' : 'Kaushal'},
               2: {'Maths' : 100,
                          'Artificial Intelligence' :  100,
                          'Physics': 100,
                          'Micro proccessor': 100}}

print(nested_dict[1]['name'])
print('Marks of maths: ',nested_dict[2]['Maths'])
print('Marks of Artificial Intelligence: ',nested_dict[2]['Artificial Intelligence'])
print('Marks of Physics: ',nested_dict[2]['Physics'])
print('Marks of Micro proccessor: ',nested_dict[2]['Micro proccessor'])



