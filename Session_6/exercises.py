#Question 1:
groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Coffee": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

total_cost = 0.0

print("Please enter the quantity of each item you would like to purchase.")

for item in groceries:
    quantity = int(input(f"How many {item} do you want? "))
    cost = groceries[item] * quantity
    total_cost += cost

print("Your total is $",total_cost)

#Question 2:
