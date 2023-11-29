# Name: V Nguyen
# Prog Purpose: This program finds the cost of movie tickets
#   Price for one ticket: $10.99
#   Sales tax rate: 5.5%

import datetime

#define tax rate and prices
SALES_TAX_RATE = 0.055
PR_TICKET = 10.99

#define global variables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

#define program functions
def main():
    more_tickets = True

    while more_tickets:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno.lower() != "y":
            more_tickets = False
            print("Thank you for your order. Enjoy your movie!")

def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets: "))

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('------------------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighborhood movie house')
    print('------------------------------')
    print('Tickets      $ ' + format(subtotal,'8.2f'))
    print('Sales Tax    $ ' + format(sales_tax,'8.2f'))
    print('Total        $ ' + format(total,'8.2f'))
    print('------------------------------')
    print(str(datetime.datetime.now()))

if __name__ == "__main__":
    main()
