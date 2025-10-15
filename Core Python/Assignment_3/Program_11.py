"""11. Accept age of five people and also per person ticket amount and then
 calculate total
amount to ticket to travel for all of them based on following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount2
c. Others need to pay full."""

ticket_price = float(input("Enter ticket price per person :"))

p1 = int(input("Enter the age of person 1 : "))
p2 = int(input("Enter the age of person 2 : "))
p3 = int(input("Enter the age of person 3 : "))
p4 = int(input("Enter the age of person 4 : "))
p5 = int(input("Enter the age of person 5 : "))

# person 1
if(p1 < 12):
    cost1 = ticket_price * 0.70
elif(p1 > 59):
    cost1 = ticket_price * 0.50
else:
    cost1 = ticket_price

# person 2
if(p2 < 12):
    cost2 = ticket_price * 0.70
elif(p2 > 59):
    cost2 = ticket_price * 0.50
else:
    cost2 = ticket_price

# person 3
if(p3 < 12):
    cost3 = ticket_price * 0.70
elif(p3 > 59):
    cost3 = ticket_price * 0.50
else:
    cost3 = ticket_price

# person 4
if(p4 < 12):
    cost4 = ticket_price * 0.70
elif(p4 > 59):
    cost4 = ticket_price * 0.50
else:
    cost4 = ticket_price

# person 5
if(p5 < 12):
    cost5 = ticket_price * 0.70
elif(p5 > 59):
    cost5 = ticket_price * 0.50
else:
    cost5 = ticket_price
 
total = cost1 + cost2 + cost3 + cost4 + cost5 

print(f"Enter total all cost for 5 pepole : {total} ")



        






