l = float(input("Enter the Length : "))

b = float(input("Enter the Breadth : "))

r = float(input("Enter the Radius : "))

PI = 3.14


area_rectangle = l * b
area_semicircle = 0.5 * PI * r * r
total_area = area_rectangle + area_semicircle


rectangle_perimeter = 2 * l + b
semicircle_perimeter = PI * r
total_perimeter = rectangle_perimeter + semicircle_perimeter


print("Area : ",round(total_area,2))
print("Perimeter : ",round(total_perimeter,2))

