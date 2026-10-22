# Bobby Williams    
#10/22/2026
# P4HW2
# Use a loop to calculate pay for ALL employees 

# Request employee information 


name = input("Enter employee's name: ")

# Create Accumulator Variables for ovetime pay, regular pay, gross pay and employee count

total_employees = 0
total_overtimepay = 0
total_regularpay = 0
total_grosspay = 0



while name != "done":

    
    hoursWorked = float(input("Enter number of hours worked: "))

    payRate = float(input("Enter employee's pay rate: "))

    #evalute overtime

    if hoursWorked >40 :

        #calculate overtime
        overtimeHours = hoursWorked - 40
        #Calculate overPay
        overPay = overtimeHours * (payRate * 1.5)

        #calculate salary for reg hours

        regPay = 40 * payRate

        # calculate gross pay

        grossPay = regPay + overPay
    else:

        overPay = 0
        overtimeHours = 0

        regPay = hoursWorked * payRate
        grossPay = regPay

    # Display output

    print("-------------------------------------")
    print("Employee name:  ",name,"\n")

    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
    print('--------------------------------------------------------------------------------------------------')
    print(f'{hoursWorked:<15}{payRate:<12}{overtimeHours:<12}{overPay:<20}{"$"}{regPay:<20.2f}{"$"}{grossPay:.2f}')
    
    # Ask the user for the next employee or done
    name =input("Enter another employee or Done to quit: ").lower()

# Loop breaks here. Display your totals below
    # Add to total values
    total_overtimepay += overPay
    total_regularpay += regPay
    total_grosspay += grossPay

    total_employees += 1

print("Total number of employess entered: ", total_employees)
print("Total amount paid for overtime: $", format(total_overtimepay, ',.2f'))
print("Total amount paid for regular time: $", format(total_regularpay, ',.2f'))
print("Total amount paid for gross pay: $", format(total_grosspay, ',.2f'))


