# Bobby Williams
# 09/10/2026
# P1HW2    
# Create float variables for the travel expenses 


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


# Create float variables for the adoption costs
total_expense = gas_expense + accommodation_expense + food_expense
print("------------Travel Expenses------------")
print(f"{'Location:':<16}{travel_destination:<17}")
print(f"{'Initial Budget:':<16}${budget:<17,.2f}")
print(f"{'Fuel:':<16}${gas_expense:<17,.2f}")
print(f"{'Accomodation:':<16}${accommodation_expense:<17,.2f}")
print(f"{'Food:':<16}${food_expense:<17,.2f}")
print("-"* 50)
print(f"{'Remaining Budget:':<16}${budget - total_expense:<17,.2f}")