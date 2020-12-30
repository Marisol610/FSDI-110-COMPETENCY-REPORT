import datetime


# to calculate age
# 1-ask the user for the age
# 2-calculate (aprox) the age of the user

#:year = input() read the input you get a string and that input is parsed to a string

# to calculate tip 
# - tip is always(15%)
#- ask for the total
#-calculaye and show the tip




def calculate_age():

    birth_year = int(input("Enter your birth year:"))

    current_year = datetime.datetime.now().year
    user_age = current_year - birth_year

    
    print('We figured it out...You are %i years old!' % (user_age))

def calculate_tip():
    bill =float(input("Enter bill amount:"))
    tip = float(input("Enter the tip % you would like to tip:"))
    tax = .06
    
    tip_calc = tip/100
    tip_amt = bill * tip_calc
    tot_tax = bill * tax
    total_bill = bill + tip_amt + tot_tax

    print("Your total bill including taxes and tips is " + str(total_bill) + "dollars.")
    print("Thank You and Have a great day!")





#print('[a] Calculate age')
#print('[b] Calculate Tip' (15%))