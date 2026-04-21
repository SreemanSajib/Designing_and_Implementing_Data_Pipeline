
class Counter:
    def __init__(self):
       
        # count 0 at the beggining
        self.__count = 0

    def addCount(self) -> None:
        # count er value er sathe 1 jog korbe
        self.__count += 1

    def getCount(self) -> int:
        # current count er return korche
        return self.__count

    def zeroCount(self) -> None:
        # count 0 agian
        self.__count = 0
