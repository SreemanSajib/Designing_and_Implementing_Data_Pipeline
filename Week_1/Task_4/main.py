
from wallet import CryptoWallet # importing class


wallets = {}

while True:
    print("\n--- Crypto Wallet Menu ---")
    print("1 - Create Wallet")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Check Balance")
    print("5 - Transaction History")
    print("0 - Exit")

    choice = input("Select an option: ")

    try:
        if choice == '1':
           
            w_id = input("Enter a unique Wallet ID: ")
            if w_id in wallets:
                print("Error: Wallet ID already existsPlease choose another one.")
            else:
                new_wallet = CryptoWallet(wallet_id=w_id)
                wallets[w_id] = new_wallet
                print(f"Wallet '{w_id}' has been created successfully.")

        elif choice == '2':
            
            w_id = input("Enter Wallet ID: ")
            if w_id in wallets:
                amount = float(input("Enter amount to deposit: "))
                wallets[w_id].deposit(amount)
            else:
                print("Error: Wallet not found.")

        elif choice == '3':
           
            w_id = input("Enter Wallet ID: ")
            if w_id in wallets:
                amount = float(input("Enter amount to withdraw: "))
                wallets[w_id].withdraw(amount)
            else:
                print("Error: Wallet not found.")

        elif choice == '4':
           
            w_id = input("Enter Wallet ID: ")
            if w_id in wallets:
                wallets[w_id].check_balance()
            else:
                print("Error: Wallet not found.")

        elif choice == '5':
            
            w_id = input("Enter Wallet ID: ")
            if w_id in wallets:
                wallets[w_id].generate_history()
            else:
                print("Error: Wallet not found.")

        elif choice == '0':
            
            print("Exiting Crypto Wallet System. Goodbye!")
            break

        else:
            \
            print("Invalid selection. Please try again.")

    except ValueError:
        
        print("Error: Invalid input format. Please enter numeric values where required.")
    except Exception as e:
        
        print(f"An unexpected error occurred: {e}")
