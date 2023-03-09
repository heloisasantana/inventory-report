from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data_list):
        companies = []
        for data_dict in data_list:
            companies.append(data_dict["nome_da_empresa"])

        companies_counter = Counter(companies)
        stock_report = ""
        for company in companies_counter:
            stock_report += f"- {company}: {companies_counter[company]}\n"

        return (
            f"{SimpleReport.generate(data_list)}\n"
            f"Produtos estocados por empresa:\n"
            f"{stock_report}"
        )
