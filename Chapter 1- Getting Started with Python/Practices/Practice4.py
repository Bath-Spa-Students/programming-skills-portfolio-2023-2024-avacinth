# Computing the area of a triangle

# Integer variable
a = 10  
b = 12  
c = 9  
  
# Calculate the semi-perimeter
s = (a + b + c) / 2
  
# Calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print('The area of the triangle is', area)