from loan_analyst import Loan
import sys
from time import sleep

#TODO allow user to edit loan parameters
#TODO allow comparison of two loans

def display_menu():
    print("""
    Menu
    -----------------
    1. Start new loan
    2. Show Payment
    3. Show Amortization Table
    4. Show Loan Summary
    5. Plot Balances
    6. Show size of payment to payoff in specific time
    7. Show effect of adding amount to each payment
    8. Quit
    """)

def new_loan(rate, term, pv):
    loan = Loan(rate, term, pv)
    print("Loan initialized")
    sleep(.5)
    return loan

def pmt(loan):
    print(loan.pmt_str)

def amort(loan):
    print(loan.table)    

def summary(loan):
    loan.summary()

def plot(loan):
    loan.plot_balances()

def pay_faster(loan):
    amt = float(input("Enter extra monthly payment: "))
    new_term = loan.pay_early(amt)
    print(f"{new_term} years")

def pay_early(loan):
    years_to_pay = int(input("Enter years to debt free: "))
    result = loan.retire_debt(years_to_pay)
    print(f"Monthly extra: {result[0]:,.2f} \tTotal Payment: {result[1]:,.2f}")    

action = {'1' : new_loan, '2' : pmt,  '3': amort, '4': summary,
          '5': plot, '6': pay_early, '7' : pay_faster}

def main():
    
    
    while True:
        display_menu()
        choice = input("Enter your selection: ")
        if choice == '1':
            rate = float(input("Enter interest rate: "))
            term = int(input("Enter loan term: "))
            pv = float(input("Enter amount borrowed: "))
            loan = Loan(rate, term,pv)    
            print("Loan initialized")
            sleep(.75)
            
        elif choice in '234567':
            action[choice](loan)
            sleep(1)    
        elif choice == '8':
            print("Goodbye")
            sys.exit()
        else:
            print("please enter a valid selection")        



if __name__ == "__main__":
    main()
    