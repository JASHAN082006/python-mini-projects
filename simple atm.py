print("--- Simple ATM ---")
balance = 5000
pin = "1234"
entered_pin = input("Enter your 4-digit PIN: ")
if entered_pin == pin:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    choice = input("Choose an option (1, 2, or 3): ")
    if choice == "1":
        print(f"Balance: ₹{balance}")
    elif choice == "2":
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount
        print(f"New Balance: ₹{balance}")
    elif choice == "3":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance = balance - amount
            print(f"New Balance: ₹{balance}")