l = float(input("Enter the lenght of wall:"))
b= float(input("Enter the breadth of wall:"))

area_of_one_wall= l * b
area_of_interior= l * b
area_of_exterior= l * b

print("Area of one wall : ",area_of_one_wall)
print("Area of interior: ",area_of_interior)
print("Area of exterior : ",area_of_exterior)

cost_of_interior= int(input("Enter the cost of interior:"))
cost_of_exterior= int(input("Enter the cose of exterior:"))

cost_of_painting= cost_of_interior + cost_of_exterior + (area_of_one_wall * 8)

print("Cost of painting for wall is ",cost_of_painting)


