# Computing the area of a circle 

# Integer variable
a = 10
b = 5
c = 7

# Calculating the semi-perimeter
s=(a+b+c)/2

# Calculating the area
area = (s*(s-a)*(s-b)*(s-c))**0.5

print('The area of the triangle is', area)