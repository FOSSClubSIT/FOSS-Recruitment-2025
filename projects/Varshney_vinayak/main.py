from sklearn.linear_model import LogisticRegression
import numpy as np

X_train = np.array([
    [8, 0, 0],
    [10, 1, 0],
    [12, 0, 1],
    [14, 1, 1],
    [16, 1, 1],
    [6, 0, 0],
    [18, 1, 1],
    [11, 0, 1],
    [9, 1, 1]
])
y_train = np.array([0, 0, 1, 1, 2, 0, 2, 1, 1])

X_test = np.array([
    [12, 0, 1],
    [14, 1, 1],
    [16, 1, 1],
    [6, 0, 0],
    [18, 1, 1],
    [11, 0, 1],
    [9, 1, 1]
])
y_test = np.array([1, 1, 2, 0, 2, 1, 1])
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

def extract_features(password):
    
    length = len(password)
    has_upper = int(any(c.isupper() for c in password))
    has_digit_or_symbol = int(any(c.isdigit() or not c.isalnum() for c in password))
    return np.array([[length, has_upper, has_digit_or_symbol]])
    #dem features muah

def predict_strength(password):
    features = extract_features(password)
    pred = model.predict(features)[0]
    labels = {0: "Weak", 1: "Good", 2: "Strong"}
    return labels[pred]

def len_check(passlen):
    if passlen < 12:
        print("Password is too short(in length)")
        return 0.1
    elif passlen >= 16:
        print("Password is strong(in length)")
        return 0.4
    elif passlen >= 14:
        print("Password is good(in length)")
        return 0.3
    else:
        print("Password is weak(in length)")
        return 0.2

def upper_check(password):
    for char in password:
        if char.isupper():
            print("Password is good(in case-sensitivity)")
            return 0.2
    else:
        print("Password is weak(in case-sensitivity)")
        return 0.0

def digits_check(password):
    digi_check = False
    symbol_check = False
    for char in password:
        if char.isdigit():
            digi_check = True
        elif not(char.isalnum()):
            symbol_check = True
    if not(digi_check and symbol_check):
        print("there is no digit or symbol")
        return 0.0
    if digi_check and symbol_check:
        print("password is strong with both digits and symbols")
        return 0.4
    if digi_check and not(symbol_check):
        print("password is good and has a digit")
        return 0.2
    if not(digi_check) and symbol_check:
        print("password is good and has a symbol")
        return 0.2

print("Password strength checker with a spice")
password = input("Enter your password:" )
passlen = len(password)
checking = True
while checking:
    print("""
1- Length check
2- Uppercase check
3- Digits and symbols check
4- Password Score (manual)
5- Password Strength (ML)
6- Exit
          """)
    choice = input("Enter your choice: ")
    if choice == "1":
        len_check(passlen)
    elif choice == "2":
        upper_check(password)
    elif choice == "3":
        digits_check(password)
    elif choice == "4":
        score = len_check(passlen) + upper_check(password) + digits_check(password)
        print("Your password score is: ", score)
        if score >= 0.7:
            print("Your password is strong")
        elif score >= 0.4:
            print("Your password is good")
        elif score >= 0.2:
            print("Your password is weak")
        elif score <= 0.1:
            print("Your password is too bad")
    elif choice == "5":
        ml_strength = predict_strength(password)
        print("ML model predicts your password is:", ml_strength)
    elif choice == "6":
        checking = False
    else:
        print("Invalid choice")

print("Thank you for using my service")