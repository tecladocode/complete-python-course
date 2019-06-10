from printer import Printer, PrinterError
from unittest import TestCase


class TestPrinter(TestCase):
    def setUp(self):
        self.printer = Printer(pages_per_s=2.0, capacity=300)

    def test_print_within_capacity(self):
        self.printer.print(25)
