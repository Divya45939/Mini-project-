balance = 1000
def deposit():
    amount = int(input("enter the amount: "))
    if amount >0:
        print(f"{amount}/- is credited successfully")
        return amount
    else:
        print("plz enter valid amount") 
        return 0
def withdraw():
    amount = int(input("enter the amount: "))
    if amount <=balance:
        print(f"{amount}/- is debited from your account successsfully")
        return amount
    else:
        print("insuficient balance")
        return 0
def check_balance():
    print(f"your avaliable balance is {balance}/-")

db_pin = 4595
input_pin = int(input("enter your pin: "))
chance = 3
is_correct_pin = False
for i in range(1,chance+1):
    if db_pin == input_pin:
        is_correct_pin = True
        break
    else:
        if chance - i !=0:
            print(f"wrong pin ,  you have {chance - i} chances left")
            input_pin = int(input("enter your pin: "))
        else:
            break
if is_correct_pin:
    while True:
        print("""  
choose 1 to deposit
choose 2 for withdraw
choose 3 to check balance
choose 4 to exit""")  
        choice = int(input("enter your choice: "))
        if choice == 1:
            balance += deposit()
        elif choice == 2:
            balance -= withdraw()
        elif choice == 3:
            check_balance()
        elif choice == 4:
            print("THANK YOU Visit Again") 
            break
    
        
else:
    print("your account has been blocked for 24hrs ")  

choice = int(input("enter your choice"))
if choice == 1:
    balance += deposit()
elif choice == 2:
    balance -= withdraw()
elif choice == 3:
    check_balance()
elif choice == 4:
    print("THANK YOU Visit Again") 




        


 
