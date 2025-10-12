#5 Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.


side_1 = float(input("Enter first side: "))
side_2 = float(input("Enter second side : "))
side_3 = float(input("Enter third side : "))

if(side_1+side_2 > side_3 ) and (side_1+side_3 > side_2) and (side_2+side_3 > side_1):
    
    if side_1==side_2 or side_1==side_3 or side_2==side_3 :
        print("triangle is Isosceles. ")    
    elif side_1==side_2==side_3 :
            print("triangle is Equilateral. ") 
    else:
            print("triangle is Scalene. ")
            
else:
        print("triangle is not vaild. ")
