from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        data = []

        if(path.endswith(".csv")):
            data = CsvImporter.import_data(path)

        elif(path.endswith(".json")):
            data = JsonImporter.import_data(path)

        elif(path.endswith(".xml")):
            data = XmlImporter.import_data(path)

        return Inventory.generate_report(data, report_type)

    @staticmethod
    def generate_report(data, report_type):
        if report_type == "simples":
            return SimpleReport.generate(data)

        elif report_type == "completo":
            return CompleteReport.generate(data)
