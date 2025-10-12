#Write a program to enter P, T, R and calculate Compound Interest. 
p = float(input("Enter Principle of interest:"))
r = float(input("Enter rate of interest:"))
t = float(input("Enter time of years :"))

#Perform operration
ci = p * (1 + r / 100) ** t - p

#Display the result
print("Compound Interest :",ci)



