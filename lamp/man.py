class LampInterface:
    def is_lighted(self) -> bool:
        pass

    def switch(self) -> None:
        pass


class LampNotWorkingError(Exception):
    pass


class Man:
    __patience: int = None

    def __init__(self, patience: int):
        assert patience >= 0
        self.__patience = patience

    def light_on(self, lamp: LampInterface) -> None:
        if lamp.is_lighted():
            return
        if self.__try_light_on(lamp):
            return
        if self.__impatient():
            raise LampNotWorkingError()

        for _ in range(self.__patience):
            if self.__try_light_on(lamp):
                return

        raise LampNotWorkingError()

    def __impatient(self) -> bool:
        return self.__patience == 0

    @staticmethod
    def __try_light_on(lamp: LampInterface) -> bool:
        lamp.switch()
        return lamp.is_lighted()

