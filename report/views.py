from report import ViewInterface, Report


class TotalView(ViewInterface):
    def print(self, report: Report) -> str:
        return f'Total: {report.sum()}'


class SimpleView(ViewInterface):
    def __init__(self, sep="\n"):
        self.__sep = sep

    def print(self, report: Report) -> str:
        lines = []
        for row in report.rows():
            lines.append(f'{row.name} {row.price}')
        return self.__sep.join(lines)
