#11 Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

amount = int(input("Enter the amount: "))

n2000 = amount // 2000
amount = amount % 2000

n500 = amount // 500
amount = amount % 500

n200 = amount // 200
amount = amount % 200

n100 = amount // 100
amount = amount % 100

n50 = amount // 50
amount = amount % 50

n20 = amount // 20
amount = amount % 20

n10 = amount // 10
amount = amount % 10

n5 = amount // 5
amount = amount % 5

n2 = amount // 2
amount = amount % 2

n1 = amount // 1
amount = amount % 1

print("Minimum number of notes:")
print("2000:", n2000)
print("500 :", n500)
print("200 :", n200)
print("100 :", n100)
print("50  :", n50)
print("20  :", n20)
print("10  :", n10)
print("5   :", n5)
print("2   :", n2)
print("1   :", n1)
