# num = int(input("enter the number: "))
# if num > 0:
#     print("Positive")
# else:
#     print("Not Positive")
    
# Login system
# username = input("Enter name: ")
# password = input("Enter password: ")
# if username ==  "admin":
#     if password == "1234":
#         print("Login successfully")        
#     else:
#         print("worng password")
# else:
#     print("User not found")

# Movie ticket
# age = int(input("Enter the age: "))
# has_ticket = input("do  you have ticket: ")
# if age >= 18:
#     if has_ticket == "yes":
#         print("You may enter")
#     else:
#         print("Buy a ticker first")
# else:
#     print("Your are not allowed to enter")
    
# Atm withdrawal
# balance = int(input("Enter you balance: "))
# withdraw_amount = int (input("Enter your withdrawal ammount: "))
# if balance >= withdraw_amount:
#     if withdraw_amount > 0:
#         print("Transaction successful")
#     else:
#         print("Invalid amount")
# else:
#     print("Insufficien balance")

# scolership eligibility
# marks = int(input("Enter your mark: "))
# family_income = int(input ("Enter the amount: "))
# if marks >= 80:
#     if family_income <= 50000:
#         print("Scholership approved")
#     else:
#         print("Marks are good, but income is too high.")
# else:
#     print("Not Eligible")

# chalange harder
username = input("Enter the name: ")
password = input("Enter the password: ")
otp = int(input("The otp is: "))
if username == "Bappy":
    if password == "py123":
        if otp == "9876":
            print("Login successful")
        else:
            print("Invalid OTP")
    else:
        print("Wrong Password")
else:
    print("User not found")