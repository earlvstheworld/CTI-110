# Bobby Williams
# 10/20/2026
# Nested loops 

# Create the variable that controls the while loop
# This value is temporary
run_again = "yes"

while run_again == "yes":
    
    #Get an interger from the user 
    integer = int(input("Enter a number: "))
    
    # Check if integer is positive 
    if integer >= 0:
        # Display multiplication
        for num in range(1,13):
            print(f"{integer} * {num} = {integer * num}")
    # If the number is negative
    else:
        print("Error, no negative numbers allowed!")
    
    print("Program is running")
    # Allow the user to give a new value to run_again
    run_again = input("Run the program again? ").lower()
    
# Loop breaks here 
print("Program ended, goodbye!")