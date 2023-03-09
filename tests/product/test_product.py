from inventory_report.inventory.product import Product


def test_cria_produto():
    data = {
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1"
    }

    new_product = Product(
        data["id"],
        data["nome_do_produto"],
        data["nome_da_empresa"],
        data["data_de_fabricacao"],
        data["data_de_validade"],
        data["numero_de_serie"],
        data["instrucoes_de_armazenamento"]
    )

    assert new_product.id == data["id"]
    assert new_product.nome_do_produto == data["nome_do_produto"]
    assert new_product.nome_da_empresa == data["nome_da_empresa"]
    assert new_product.data_de_fabricacao == data["data_de_fabricacao"]
    assert new_product.data_de_validade == data["data_de_validade"]
    assert new_product.numero_de_serie == data["numero_de_serie"]
    assert new_product.instrucoes_de_armazenamento == \
        data["instrucoes_de_armazenamento"]
