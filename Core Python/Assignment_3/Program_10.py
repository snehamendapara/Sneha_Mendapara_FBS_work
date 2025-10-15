"""10 Write a program to check if person is eligible to marry or not (male age >=21 and
female age>=18) """

female = int(input("Enter Female age :"))
male = int(input("Enter Male age :"))

if (female >= 18 and male >= 21):
    print(" Both are eligible for marry ")
else :
    print ("Not eligible for marry")