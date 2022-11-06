import builtins

from man import LampInterface
from work_lamp import WorkLamp


class BrokenLamp(LampInterface):
    __counter: int = 0
    __attempts: int = 0
    __lamp: WorkLamp = None

    def __init__(self, attempts: int):
        assert attempts >= 0
        self.__attempts = attempts
        self.__counter = 0
        self.__lamp = WorkLamp()

    def is_lighted(self) -> bool:
        return self.__lamp.is_lighted()

    def switch(self) -> None:
        if self.__hopelessly():
            return
        if self.__working():
            self.__lamp.switch()
            return

        self.__counter += 1

        if self.__counter == self.__attempts:
            # turn on
            self.__lamp.switch()
            return

        if self.__counter > self.__attempts:
            # turn off
            self.__lamp.switch()
            self.__counter = 1

    def __hopelessly(self) -> bool:
        return self.__attempts == 0

    def __working(self) -> bool:
        return self.__attempts == 1
