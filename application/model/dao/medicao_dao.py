from datetime import datetime
from application.model.entity.medicao import Medicao
import json
from typing import List

class MedicaoDAO:
    def __init__(self):
        medicao1 = Medicao(1, 1, 12, 10, 50, 1, 20, 16, '12/06/2021')
        medicao2 = Medicao(2, 2, 21, 10, 43, 1, 19, 36,'18/06/2021')

        self._medicao_list = [medicao1, medicao2]
    

    def inserir(self, medicao: Medicao):
        medicao_list = self.listarTodos()
        medicao.id = len(medicao_list) + 1
        medicao_list.append(medicao)
        medicao_dict_list = []
        for medicao in medicao_dict_list:
            medicao_dict_list.append(medicao.toDict())
        with open('medidas.json') as file:
            json.dump(medicao_dict_list, file)

    def listarTodos(self) -> List[Medicao]:
        return self._medicao_list

"""
    def listarTodos(self) -> List[Medicao]:
        resultado = []
        with open('medidas.json') as file:
            medicao_dict_list = json.load(file)
            for medicao_dict in medicao_dict_list:
                medicao = Medicao()
                medicao._id = medicao_dict.get('id', None)
                medicao._dispositivo_id = medicao_dict.get('dispositivoId', None)
                medicao._gas = medicao_dict.get('gas', None)
                medicao._nitrogenio = medicao_dict('nitrogenio', None)
                medicao._gas_ozonio = medicao_dict('gasOzonio', None)
                medicao._temperatura = medicao_dict('temperatura', None)
                medicao._umidade = medicao_dict('umidade', None)
                medicao._data = medicao_dict.get('data', None)
                resultado.append(medicao)
        return resultado
"""