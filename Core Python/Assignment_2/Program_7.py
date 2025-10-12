#7.Find the sum of three-digit number.
number = int(input("Enter number :"))


hundreds  = number // 100
tens  = number // 10 % 10
units  = number % 10

sum = hundreds + tens + units

print(sum)


