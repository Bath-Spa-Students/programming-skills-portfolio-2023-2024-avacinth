# Taking the courses marks from the user

course1 = float(input("Course 1 marks: "))
course2 = float(input("Course 2 marks: "))
course3 = float(input("Course 3 marks: "))
course4 = float(input("Course 4 marks: "))
course5 = float(input("Course 5 marks: "))

# Calculating the average of the courses marks

total = course1 + course2 + course3 + course4 + course5
avg = total/5

total_marks = float(input("Total marks: "))
percentage = (avg/total_marks)*100

print("The average mark of all the courses is: ", avg)
print("The percentage of all the student is : ", percentage)