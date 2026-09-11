# Bobby Williams
# 09/10/2026
# P1HW2    
# Create a travel budget

print("------------Travel Budget------------")
print("Enter Budget")
budget = int(input())
print("Enter Destination")
travel_destination = input()
print("How much do you think you will spend on gas?")
gas_expense = int(input())
print("How much do you think you will spend on accommodation?")
accommodation_expense = int(input())
print("How much do you think you will spend on food?")
food_expense = int(input())

total_expense = gas_expense + accommodation_expense + food_expense
print("------------Travel Expenses------------")
print("Destination:", travel_destination)
print("Initial Budget:", budget)
print("Gas:", gas_expense)
print("Accommodation:", accommodation_expense)
print("Food:", food_expense)
print("Remaining Budget:", budget - total_expense)