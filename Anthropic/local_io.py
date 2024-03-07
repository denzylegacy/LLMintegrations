# -*- coding: utf-8 -*-

import json


class JSONHandler:
    """
    TODO:
    # Ler os dados de um arquivo JSON.
    data = json_handler.read_json('json_options/options.json_options')
    print(data)  # imprime os dados do arquivo JSON

    # Escrevendo os dados num arquivo JSon.
    data_to_write = {"some_key": "some_value"}
    json_handler.write_json('json_options/some_file.json_options', data_to_write)
    """

    @staticmethod
    def read_options_json(file_path):
        """
        TODO:
        - Ler um arquivo JSon e retorna os dados dele
        - Adicionei encoding='utf-8' às funções open() em ambos os métodos.
          Isso garante que o arquivo seja lido e gravado como UTF-8.
        """
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def __init__(self, file_path):
        self.file_path = file_path

    def read_json(self):
        """
        TODO:
        - Ler um arquivo JSon e retorna os dados dele
        - Adicionei encoding='utf-8' às funções open() em ambos os métodos.
          Isso garante que o arquivo seja lido e gravado como UTF-8.
        """
        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def write_json(self, data):
        """
        TODO:
        - Escreve os dados em um arquivo JSON
        - Adicionei ensure_ascii=False ao método json_options.dump().
        - Isso garante que os caracteres não ASCII sejam escritos no arquivo JSON corretamente,
          em vez de serem escapados com sequências.
        - Adicionei encoding='utf-8' às funções open() em ambos os métodos.
          Isso garante que o arquivo seja lido e gravado como UTF-8.
        """
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
