class Libra:
    def __init__(self):
        self.__left = 0
        self.__right = 0

    def balance(self) -> int:
        return abs(self.__left - self.__right)

    def is_equilibrium(self) -> bool:
        return self.balance() == 0

    def put(self, v: int):
        if v <= 0:
            raise ValueError("must non negative value")

        if self.is_equilibrium():
            self.__put_left(v)
            return
        if self.__is_left_lower():
            self.__put_left(v)
            return
        self.__put_right(v)

    def left(self) -> int:
        return self.__left

    def right(self) -> int:
        return self.__right

    def __put_left(self, v: int):
        self.__left += v

    def __put_right(self, v: int):
        self.__right += v

    def __is_left_lower(self) -> bool:
        return self.__left < self.__right
