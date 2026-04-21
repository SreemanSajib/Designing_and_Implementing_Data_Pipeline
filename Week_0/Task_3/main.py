
# coin_acceptor.py theke CoinAcceptor class import korteche
from coin_acceptor import CoinAcceptor

print("Program starting.")

# CoinAcceptor er obejct banacche
coin_acceptor = CoinAcceptor()

# showing menu
while True:
    print("\n1 - Insert coin")
    print("2 - Show coins")
    print("3 - Return coins")
    print("0 - Exit program")

    # user choice
    choice = input("Your choice: ")

    if choice == "1":
        # coin insert 
        coin_acceptor.insertCoin()

    elif choice == "2":
        # current coins show 
        print(f"Currently '{coin_acceptor.getAmount()}' coins in coin acceptor")

    elif choice == "3":
        # coins return 
        returned = coin_acceptor.returnCoins()
        print(f"Coin acceptor returned '{returned}' coins.")

    elif choice == "0":
        # program closeing
        print("Program ending.")
        break

    else:
        # for wront option
        print("Invalid choice, try again.")
