#6 Write a program to calculate profit or loss.
cp = float(input("Enter cp value : "))
sp = float(input("Enter sp value : "))

if(sp > cp):
    profit = sp - cp
    print(f"profit of {profit}")
elif(cp < sp):
    loss = cp - sp
    print(f"Loss of {loss}")
else:
    print("no profit no loss")






