
class ViewInterface:
    def print(self, report: "Report") -> str:
        pass


class Row:
    def __init__(self, name: str, price: int):
        assert len(name) != 0
        self.__name = name
        self.__price = price

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> int:
        return self.__price

    def __eq__(self, other):
        if not isinstance(other, Row):
            return NotImplemented
        return other.name == self.name and other.price == self.price


class Report:
    def __init__(self):
        self.__rows = []

    def append(self, row: Row):
        self.__rows.append(row)

    def rows(self) -> []:
        return self.__rows

    def count(self) -> int:
        return len(self.__rows)

    def sum(self) -> int:
        result = 0
        for row in self.__rows:
            result += row.price
        return result

    def print(self, view: ViewInterface = None) -> str:
        if view is None:
            return ""
        return view.print(self)
