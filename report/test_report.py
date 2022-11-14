import unittest

from report import Report, Row
from views import TotalView, SimpleView


class TestReport(unittest.TestCase):

    def test_print_empty_view(self):
        report = Report()
        out = report.print(None)
        self.assertEqual("", out)

    def test_total_view(self):
        report = Report()
        report.append(Row("drive", 111))
        report.append(Row("wheels", 999))
        out = report.print(TotalView())
        self.assertEqual("Total: 1110", out)

    def test_simple_view(self):
        report = Report()
        report.append(Row("drive", 111))
        report.append(Row("wheels", 999))
        out = report.print(SimpleView())
        self.assertEqual("drive 111\nwheels 999", out)

    def test_append_rows(self):
        report = Report()
        self.assertEqual(0, report.count())
        self.assertEqual([], report.rows())
        self.assertEqual(0, report.sum())

        report.append(Row("drive", 1111))
        report.append(Row("wheels", 999))

        self.assertEqual(2, report.count())
        self.assertListEqual([
            Row("drive", 1111),
            Row("wheels", 999)
        ], report.rows())
        self.assertEqual(2110, report.sum())
