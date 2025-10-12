#3 Write a program to input angles of a triangle and check whether triangle is valid or not.

angle_1 = int(input("Enter Angle1 : "))
angle_2 = int(input("Enter Angle2 : "))
angle_3 = int(input("Enter Angle3 : "))

Total_angle = angle_1+angle_2+angle_3

if Total_angle == 180 :
    print("Angles are valid ")  
else:
    print("Angles are not vaild")
    