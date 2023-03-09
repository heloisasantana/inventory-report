from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        data = []

        if(path.endswith(".csv")):
            data = Inventory.reader_csv(path)

        elif(path.endswith(".json")):
            data = Inventory.reader_json(path)

        elif(path.endswith(".xml")):
            data = Inventory.reader_xml(path)

        return Inventory.generate_report(data, report_type)

    @staticmethod
    def reader_csv(path):
        with open(path, "r") as file:
            return [row for row in csv.DictReader(file)]

    @staticmethod
    def reader_json(path):
        with open(path, "r") as file:
            return json.loads(file.read())

    @staticmethod
    def reader_xml(path):
        with open(path, "r") as file:
            return xmltodict.parse(file.read())["dataset"]["record"]

    @staticmethod
    def generate_report(data, report_type):
        if report_type == "simples":
            return SimpleReport.generate(data)

        elif report_type == "completo":
            return CompleteReport.generate(data)
