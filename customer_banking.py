# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    print('Thank you for creating a savings account with us.')
    x=0
    y=0
    z=0
    while True:
        if x==0:
            savings_balance=input('Please enter your starting balance: ')
            x=1
        if y==0:
            savings_interest_rate=input('Please enter you interest rate: ')
            y=1
        if z==0:
            savings_months=input('Please enter how many months you will be saving with us: ')
            z=1
        if savings_balance.isdigit()&savings_interest_rate.isdigit()&savings_months.isdigit():
            savings_balance=float(savings_balance)
            savings_interest_rate=float(savings_interest_rate)
            savings_months=int(savings_months)
            if (savings_balance>0)&(savings_interest_rate>0)&(savings_months>0):
                break
            else:
                if savings_balance<=0:
                    print('You must enter a positive value for your starting balance.')
                    x=0
                if savings_interest_rate<=0:
                    print('You must enter a positive value for your interest rate.')
                    y=0
                if savings_months<=0:
                    print('You must enter a positive value for your months to save.')
                    z=0
        else:
            if savings_balance.isdigit()==False:
                print('You must input a positive number value for your starting balance.')
                x=0
            if savings_interest_rate.isdigit()==False:
                print('You must input a positive number value for your interest rate.')
                y=0
            if savings_months.isdigit()==False:
                print('You must input a positive number value for your months you will be saving with us.')
                z=0


    # # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance,interest_earned=create_savings_account(savings_balance, savings_interest_rate, savings_months)

    # # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # # ADD YOUR CODE HERE
    print(f"""Your balance after {savings_months} months will be ${updated_savings_balance:.2f}, 
          having earned ${interest_earned:.2f} in interest.""")

    # # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # # ADD YOUR CODE HERE
    print('Thank you for creating a CD account with us.')
    x=0
    y=0
    z=0
    while True:
        if x==0:
            cd_balance=input('Please enter your starting balance: ')
            x=1
        if y==0:
            cd_interest_rate=input('Please enter you interest rate: ')
            y=1
        if z==0:
            cd_months=input('Please enter how many months you will be saving with us: ')
            z=1
        if cd_balance.isdigit()&cd_interest_rate.isdigit()&cd_months.isdigit():
            cd_balance=float(cd_balance)
            cd_interest_rate=float(cd_interest_rate)
            cd_months=int(cd_months)
            if (cd_balance>0)&(cd_interest_rate>0)&(cd_months>0):
                break
            else:
                if cd_balance<=0:
                    print('You must enter a positive value for your starting balance.')
                    x=0
                if cd_interest_rate<=0:
                    print('You must enter a positive value for your interest rate.')
                    y=0
                if cd_months<=0:
                    print('You must enter a positive value for your months to save.')
                    z=0
        else:
            if cd_balance.isdigit()==False:
                print('You must input a positive number value for your starting balance.')
                x=0
            if cd_interest_rate.isdigit()==False:
                print('You must input a positive number value for your interest rate.')
                y=0
            if cd_months.isdigit()==False:
                print('You must input a positive number value for your months you will be saving with us.')
                z=0

    # # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance,interest_earned=create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # # ADD YOUR CODE HERE
    print(f"""Your balance after {cd_months} months will be ${updated_cd_balance:.2f}, 
          having earned ${interest_earned:.2f} in interest.""")

if __name__ == "__main__":
    # Call the main function.
    main()