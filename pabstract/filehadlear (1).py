from abc import ABC, abstractmethod

class FileHandler(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


class PDFFile(FileHandler):

    def read(self):
        print("Reading PDF file")

    def write(self):
        print("Writing PDF file")


class CSVFile(FileHandler):

    def read(self):
        print("Reading CSV file")

    def write(self):
        print("Writing CSV file")


class ExcelFile(FileHandler):

    def read(self):
        print("Reading Excel file")

    def write(self):
        print("Writing Excel file")


pdf = PDFFile()
csv = CSVFile()
excel = ExcelFile()

pdf.read()
pdf.write()

csv.read()
csv.write()

excel.read()
excel.write()