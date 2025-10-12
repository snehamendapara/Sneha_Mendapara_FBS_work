#Program to Find the Roots of a Quadratic Equation
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

#Perform operation
d = (b**2) - 4*a*c
d1 = d ** 0.5

#Display the result
r1 = (-b + d1)/(2*a)
r2 = (-b - d1)/(2*a)

print("The First Value",round(r1,2))
print("The Second Value",round(r2,2))

