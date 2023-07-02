#Compulsory task one
#Capstone project
import math

# user input calculation choice
calculation_type = input("Enter either 'investment' or 'bond' from the menu below: ").lower()

# calculation for investment
if calculation_type == 'investment':
    # Obtain user input for investment calculation
    deposit_amount = float(input("Enter the amount you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as percentage): "))
    investment_years = int(input("Enter the number of years you plan on investing: "))
    interest = input("Do you want 'simple' or 'compound' investing? ").lower()

    # calculate the investment value based on the interest type
    if interest == 'simple':
        investment_value =  deposit_amount * (1 + (interest_rate / 100) * investment_years)
    elif interest == 'compound':
        investment_value = deposit_amount * math.pow((1 + interest_rate / 100), investment_years)
    else:
        print("Error: interest type input is not valid")
        investment_value = None

     # display result
    if investment_value:
        print("Your investment will be equivalent to R{} after {} years.".format(round(investment_value, 2), investment_years))

# Calculation for Bond
elif calculation_type == 'bond':
 # obtain user input for bond calculation
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate: "))
    number_of_months = int(input("Enter the number of months to take to repay the bond: "))

 # calcuate the amount for the bond repayment
    repayment_per_month = (interest_rate / 100 / 12 * present_value) / (1 - (1 + (interest_rate / 100 / 12) ** (-number_of_months)))

 # display result
    print("Your bond repayment per month will be R{}.".format(round(repayment_per_month, 2)))

# wrong input
else:
    print("Error: input for calculation type is incorrect. ")

# I waited till i attended all the lectures on lecture on variables and control structures to solve this
# I referred to the pdf document on dropbox and watched youtube videos to better understand the instructions
# An example of how to use the program created
# Enter either 'investment' or 'bond' from the menu below: investment
# Enter the amount you are depositing: 90000
# Enter the interest rate (as percentage): 14
# Enter the number of years you plan on investing: 5
# Do you want 'simple' or 'compound' investing? simple
# Your investment will be equivalent to R153000.0 after 5 years.
