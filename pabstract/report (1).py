from abc import ABC, abstractmethod

class Report(ABC):

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def export(self):
        pass


class PDFReport(Report):

    def generate(self):
        print("PDF Report generated")

    def export(self):
        print("PDF Report exported")


class ExcelReport(Report):

    def generate(self):
        print("Excel Report generated")

    def export(self):
        print("Excel Report exported")


pdf = PDFReport()
excel = ExcelReport()

pdf.generate()
pdf.export()

excel.generate()
excel.export()