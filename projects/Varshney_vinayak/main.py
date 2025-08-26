def len_check(passlen):
    if passlen < 12:
        print("Password is too short")
        return 0.1
    elif passlen >= 12:
        print("Password is weak")
        return 0.2
    elif passlen >= 14:
        print("Password is good")
        return 0.3
    elif passlen >= 16:
        print("Password is strong")
        return 0.4

def upper_check(password):
    for char in password:
        if char.isupper():
            print("Password is good")
            return 0.2

def digits_check(password):
    digi_check = False
    symbol_check = False
    for char in password:
        if char.isdigit():
            digi_check = True
        elif not(char.isdigit()):
            symbol_check = True
            print("password has a digit")
        elif not(char.isalnum()):
            print("password has a special character")
    if not(digi_check and symbol_check):
        print("there is no digit or symbol")
        return 0.0
    if digi_check and symbol_check:
        print("password is strong")
        return 0.4
    if digi_check and not(symbol_check):
        print("password is good")
        return 0.2
    if not(digi_check) and symbol_check:
        print("password is good")
        return 0.2


password = input("Enter your password:" )
passlen = len(password)
checking = True
while checking:
    print("""
1- Length check
2- Uppercase check
3- Digits and symbols check

          """)
    choice = int(input("Enter your choice: "))
    if choice == "1":
        len_check(passlen)
    elif choice == "2":
        upper_check(password)
    elif choice == "3":
        digits_check(password)
    else:
        print("Invalid choice")
        break
    ask = int(input("Do you want to continue? (0/1)"))
    if ask == 0:
        checking = False

print("Thank you for using my service")

    