def len_check(passlen):
    if passlen < 12:
        print("Password is too short")
    elif passlen >= 12:
        print("Password is weak")
    elif passlen >= 14:
        print("Password is good")
    elif passlen >= 16:
        print("Password is strong")


password = input("Enter your password:" )
passlen = len(password)
checking = True
while checking:
    print("""
1- Length check
          """)
    choice = int(input("Enter your choice: "))
    if choice == "1":
        len_check(passlen)
    