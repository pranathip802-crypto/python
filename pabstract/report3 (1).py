from abc import ABC, abstractmethod

class Report(ABC):

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def generate(self):
        pass

    def display_report_info(self):
        print("Report:", self.title)


class PDFReport(Report):

    def generate(self):
        print("PDF Report generated")


report = PDFReport("Monthly Report")

report.generate()
report.display_report_info()