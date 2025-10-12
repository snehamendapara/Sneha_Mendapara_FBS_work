#4 Write a program to input all sides of a triangle and check whether triangle is valid or not

 
side_1 = float(input("Enter first side: "))
side_2 = float(input("Enter second side : "))
side_3 = float(input("Enter third side : "))

if(side_1+side_2 > side_3 ) and (side_1+side_3 > side_2) and (side_2+side_3 > side_1):
    print("Triangle is valid.")
    
else:
    print("Triangle is not vaild.")