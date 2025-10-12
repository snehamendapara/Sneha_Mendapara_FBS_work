#Write a program to enter P, T, R and calculate simple Interest.
p = float(input("Enter Principle of interest:"))
r = float(input("Enter rate of interest:"))
t = float(input("Enter time of years :"))

#perform Operation
si = (p* r * t) / 100

#Display the result
print(f"simple interest :",si)




