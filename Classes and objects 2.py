#Question 1
pi=3.14
class Circle:
    def area_of_circle(r):
        area = pi*r*r
        print(area)
        return area
    def circumference_of_circle(r):
        circumference = 2*pi*r
        print(circumference)
        return circumference
radius = float(input("Enter the radius: "))
ob= Circle
ob.area_of_circle(radius)
ob.circumference_of_circle(radius)
print("work done")

print('*'*25)
#Question 2

class Student:
    def display(name,roll_no):
        print("Name of the student: ",str(name),'\n''Roll number of student: ',roll_no)
        return
    def setAge(age):
        print("Age of the student: ",age)
        return
    def setMarks(marks):
        print("Makrs of student in percentage(%): ",marks)
        return
ob=Student
ob.display('Ayush',150253)
ob.setAge(20)
ob.setMarks("89%")
print("**** Displaying the available student info ****")

#Question 3

class Temprature:
    def convertCelsius(c):
        fahrenheit = (c * 9/5) + 32
        print(fahrenheit)
        return fahrenheit
    def convertFahrenheit(f):
        celsius = (f - 32)*5/9
        print(celsius)
        return celsius
temp = Temprature
x = float(input("Enter the celsius: "))
y = float(input("Enter the fahrenheit: "))
temp.convertCelsius(x)
temp.convertFahrenheit(y)
print("Showing the conversion")


#Question 4

class MovieDetails:
    def display(artist_name,movie_name,year_of_release,rating):
        print("artist_name: ",str(artist_name),'\n'"movie_name",str(movie_name),'\n'"Releasing date : ",str(year_of_release),'\n'"rating out of 10: ",str(rating))
        return
    def add(Director_name):
        print("Director_name: ",str(Director_name))
        return
md = MovieDetails
md.display("Deepak Kaushal(The number one Daku)",'Avengers: Infinity War','27 April 2018 (India)','8.6/10')
md.add("Anthony Russo, Joe Russo")


#Question 6
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())


print("Output: " "A B",'\n''\t'"A B")
