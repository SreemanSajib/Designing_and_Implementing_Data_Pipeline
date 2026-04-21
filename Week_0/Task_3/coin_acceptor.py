
class CoinAcceptor:
    def __init__(self):
       
        # amount coins 
        self.__amount = 0
        # for value future 
        self.__value = 0.0

    def insertCoin(self) -> None:
        # add 1
        self.__amount += 1

    def getAmount(self) -> int:
        
        return self.__amount

    def returnCoins(self) -> int:
       
        returned = self.__amount
        
        self.__amount = 0
        return returned
