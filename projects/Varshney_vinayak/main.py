def len_check(passlen):
    if passlen < 12:
        print("Password is too short")
    elif passlen >= 12:
        print("Password is weak")
    elif passlen >= 14:
        print("Password is good")
    elif passlen >= 16:
        print("Password is strong")

def upper_check(password):
    for char in password:
        if char.isupper():
            print("Password is good")
            break

password = input("Enter your password:" )
passlen = len(password)
checking = True
while checking:
    print("""
1- Length check
2- Uppercase check
          """)
    choice = int(input("Enter your choice: "))
    if choice == "1":
        len_check(passlen)
    elif choice == "2":
        upper_check(password)
    else:
        print("Invalid choice")
        break
    ask = int(input("Do you want to continue? (0/1)"))
    if ask == 0:
        checking = False

print("Thank you for using my service")

    