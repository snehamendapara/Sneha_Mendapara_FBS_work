#9 Input 5 subject marks from user and display grade(eg.First class,Second class ..)
sub_1 = int(input("Enter Marks : "))
sub_2 = int(input("Enter Marks : "))
sub_3 = int(input("Enter Marks : "))
sub_4 = int(input("Enter Marks : "))
sub_5 = int(input("Enter Marks : "))

grade = (sub_1 + sub_2 + sub_3 + sub_3 + sub_4 + sub_5) / 5 


if(grade >= 90):
    print("First Class")
elif(grade <= 90 and grade >= 60):
    print("Second Class")
elif(grade <= 60 and grade >= 40):
    print("Third Class")
else:
    print("Fail")


