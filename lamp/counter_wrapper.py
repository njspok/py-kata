from man import LampInterface


class CounterWrapper(LampInterface):
    def __init__(self, lamp: LampInterface):
        self.__counter = 0
        self.__lamp = lamp

    def count(self) -> int:
        return self.__counter

    def is_lighted(self) -> bool:
        return self.__lamp.is_lighted()

    def switch(self) -> None:
        self.__counter += 1
        self.__lamp.switch()
