from collections import Counter
from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(data_list):
        companies = []
        fabrication_dates = []
        validity_dates = []

        for data_dict in data_list:
            companies.append(data_dict["nome_da_empresa"])
            companie_most_common = Counter(companies).most_common(1)[0][0]

            fabrication_dates.append(data_dict["data_de_fabricacao"])

            validity_date = data_dict["data_de_validade"]
            validity_date_form = datetime.strptime(validity_date, "%Y-%m-%d")
            if datetime.now() < validity_date_form:
                validity_dates.append(data_dict["data_de_validade"])

        return (
            f"Data de fabricação mais antiga: {min(fabrication_dates)}\n"
            f"Data de validade mais próxima: {min(validity_dates)}\n"
            f"Empresa com mais produtos: {companie_most_common}"
        )
