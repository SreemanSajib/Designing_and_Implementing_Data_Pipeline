
class CoinAcceptor:
    def __init__(self):
        
        self.__amount = 0
        # total coin
        self.__value = 0.0

    def insertCoin(self, coin_value: float) -> None:
        # new coin insert
        self.__amount += 1
        self.__value += coin_value

    def getAmount(self) -> int:
        # total coins 
        return self.__amount

    def getValue(self) -> float:
        # total coins value return
        return self.__value

    def returnCoins(self) -> tuple[int, float]:
       
        returned_amount = self.__amount
        returned_value = self.__value

        
        self.__amount = 0
        self.__value = 0.0

        return returned_amount, returned_value
