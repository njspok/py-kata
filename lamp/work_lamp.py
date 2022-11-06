from man import LampInterface


class WorkLamp(LampInterface):
    __ON: str = "on"
    __OFF: str = "off"
    __light: str = None

    def __init__(self):
        self.__light = self.__OFF

    def is_lighted(self) -> bool:
        return self.__light == self.__ON

    def switch(self) -> None:
        if self.__light == self.__OFF:
            self.__light = self.__ON
        else:
            self.__light = self.__OFF




