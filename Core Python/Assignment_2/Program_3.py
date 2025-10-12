#3.Convert distant given in feet and inches into meter and centimeter.

#3.Convert distant given in feet and inches into meter and centimeter.


feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

feet_to_inches = feet * 12
total_inches = feet_to_inches + inches


total_cm = total_inches * 2.54

meters = int(total_cm // 100)
centimeters = total_cm % 100


# Print the result
print(f"\n{feet} feet and {inches} inches is equal to:")
print(f"{meters} meters and {centimeters:.2f} centimeters")
