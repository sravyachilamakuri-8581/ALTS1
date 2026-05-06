def atm_system():
    # Initializing a starting balance
    balance = 1000.0
    
    print("--- Welcome to the Python ATM ---")
    
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        # Option 1: View current balance
        if choice == '1':
            print(f"Your current balance is: ${balance}")

        # Option 2: Add money to the account
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print(f"${amount} deposited successfully.")
            else:
                print("Invalid amount. Please enter a positive number.")

        # Option 3: Take money out (with logic check)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Transaction Failed: Insufficient funds!")
            elif amount <= 0:
                print("Invalid amount. Please enter a positive number.")
            else:
                balance -= amount
                print(f"${amount} withdrawn successfully.")

        # Option 4: End the program
        elif choice == '4':
            print("Thank you for using our ATM. Goodbye!")
            break

        else:
            print("Invalid selection. Please try again.")

# Run the program
atm_system()
