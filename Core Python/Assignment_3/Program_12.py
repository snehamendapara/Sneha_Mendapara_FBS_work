#12 Write a program to check if given 3 digit number is a palindrome or not.
number = int(input("Enter Number : "))

first_digit = number // 100
last_digit = number % 10

if(first_digit == last_digit):
    print("Number is palidrome")
else:
    print("Nuber is not palidrom")



