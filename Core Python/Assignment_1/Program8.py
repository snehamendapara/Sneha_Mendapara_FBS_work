#Write a program to convert days into years, weeks and days.
days = int(input("Enter Days:"))

#Perform Operation
year = days // 365
week = (days % 365) // 7 
day = (days % 365) % 7

#Display the result
print ( "Year : ",year)
print ( "week : ",week)
print ( "days : ",day) 