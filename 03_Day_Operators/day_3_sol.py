age = 20
height = 5.0
complex_num = 2+ 3j

base = float(input('Enter base:'))
height = float(input('Enter height:'))
area = 0.5* base * height
print('Area of triangle=',area)

side_a = float(input('Enter side a:'))
side_b = float(input('Enter side b:'))
side_c = float(input('Enter side c:'))
perimeter = side_a+side_b+side_c
print('Perimeter of triangle:', perimeter)

length = float(input('Enter length:'))
width = float(input('Enter width:'))
area = length*width
perimeter = 2*(length + width)
print('Area of rectangle:', area)
print('Perimeter of rectangle:', perimeter)

radius = float(input('Enter radius:'))
area = 3.14 * radius * radius
circumference = 2* 3.14 * radius
print('Area of Circle:',area)
print('Circumference of circle:', circumference)

slope1 = 2
x_intercept = 1
y_intercept = -2
print("Slope =", slope1)
print("x-intercept = (", x_intercept, ", 0)")
print("y-intercept = (0,", y_intercept, ")")

import math
slope2 =(10-2)/(6-2)
distance = math.sqrt((6-2)**2 + (10-2)**2)
print('Slope:',slope2)
print('Distance:',distance)

print(slope1 == slope2)

x = -3
y = x**2 + 6*x + 9
print("y =", y)

print(len("python") != len("dragon"))

print('on' in 'python' and 'on' in 'dragon')

sentence = "I hope this course is not full of jargon"
print("jargon" in sentence)

print("on" not in "python" and "on" not in "dragon")

length = len("python")
float_length = float(length)
string_length = str(float_length)

num = int(input('Enter a number:'))
print(num%2==0)

print((7//3) == (int(2.7)))

print(type("10") == type(10))

print(int(float('9.8'))==10)

hour = int(input('Enter hours worked :'))
rate = int(input('Enter rate per hour :'))
print("Earning = ",hour*rate)

years = int(input('Enter number of years you have lived: '))
seconds = years * 365 * 24 * 60 * 60
print('You have lived for', seconds, 'seconds.')

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)