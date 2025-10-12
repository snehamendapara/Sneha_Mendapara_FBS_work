#8 Write a program to swap two numbers using third variable.

num_1 = int(input("Enter number 1 : "))
num_2 = int(input("Enter number 2 : "))

temp = num_2
num_2 =  num_1
num_1 = temp


print (f"Number 1 : {num_1}")
print (f"Number 2 : {num_2} ")

