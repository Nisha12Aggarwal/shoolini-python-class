#Question 1
b = int(input("Enter the radius: " ))
def areaOfSquare(a):
    area=a*a
    print(area)
    return area       
b=areaOfSquare(b)

#Question 2
l=[]
def perfect(n):
    p=0
    
    for i in range(1,n):
        if n%i==0:
            p=p+i
    if p==n:
        l.append(p)
    return l
for j in range(1,1000):
    a=perfect(j)

print(a)

#Question 3
n = int(input("Enter the number: "))
sum = 0
for i in range(1,n):
    if( n % i == 0):
        sum = sum + i
    if (sum == n):
        print("perfect")
    else:
        print("not perfect")


#Question 4
       
def multiplicationOf_table(n):
    for i in range(1,11):
        table = n*i
        print(n,'*',i,'=',table)
    return multiplicationOf_table
g = int(input("Enter the number of multiplication: "))
multiplicationOf_table(g)

#Questioin 4

def power(base,exp):
    if (exp == 1):
        return(base)
    elif (exp != 1):
        return(base*power(base,exp-1))
    return power
base = int(input("Enter base value: "))
exp = int(input("Enter the exponantial value"))

print("Result: ",power(base,exp))


