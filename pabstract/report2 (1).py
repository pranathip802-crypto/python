from abc import ABC, abstractmethod

class Report(ABC):

    @abstractmethod
    def generate(self):
        pass


class PDFReport(Report):
    def generate(self):
        print("PDF Report generated")


class ExcelReport(Report):
    def generate(self):
        print("Excel Report generated")


class WordReport(Report):
    def generate(self):
        print("Word Report generated")


reports = [PDFReport(), ExcelReport(), WordReport()]

for report in reports:
    report.generate()