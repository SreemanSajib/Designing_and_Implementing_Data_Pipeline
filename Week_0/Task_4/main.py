
# CoinAcceptor class import 
from coin_acceptor import CoinAcceptor

print("Program starting.")
print("Welcome to coin acceptor program.")

# CoinAcceptor object
coin_acceptor = CoinAcceptor()

print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)")

# loop will continue until user input -1
while True:
    # user inpunting coin value
    coin = float(input("Insert coin(0 return, -1 exit): "))

    if coin == -1:
        # program exit
        print("Exiting program.")
        break

    elif coin == 0:
        # coins return
        print("Returning coins...")
        amount, value = coin_acceptor.returnCoins()
        print(f"{amount} coins with {value}€ value returned.")
        print(f"Inserted coins = {coin_acceptor.getAmount()}, value = {coin_acceptor.getValue()}€")

    else:
        # coin insert 
        print("Inserting...")
        coin_acceptor.insertCoin(coin)
        print(
            f"Inserted coins = {coin_acceptor.getAmount()}, "
            f"value = {coin_acceptor.getValue()}€"
        )

print("Program ending.")
