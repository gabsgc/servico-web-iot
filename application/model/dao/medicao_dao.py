from datetime import datetime
from application.model.entity.medicao import Medicao
import json
from typing import List

class MedicaoDAO:
    def inserir(self, medicao: Medicao) -> None:
        medicao_list = self.listarTodos()
        medicao.id = len(medicao_list) + 1
        medicao_list.append(medicao)
        medicao_dict_list = []
        for medicao in medicao_dict_list:
            medicao_dict_list.append(medicao.toDict())
        with open('medidas.json', 'w') as file:
            json.dump(medicao_dict_list, file)

    def listarTodos(self) -> List[Medicao]:
        resultado = []
        with open('medidas.json', 'r') as file:
            medicao_dict_list = json.load(file)
            for medicao_dict in medicao_dict_list:
                id = medicao_dict.get('id', None)
                dispositivo_id = medicao_dict.get('dispositivoId', None)
                materia_particulada = medicao_dict.get('materiaParticulada', None)
                gas = medicao_dict.get('gas', None)
                nitrogenio = medicao_dict.get('nitrogenio', None)
                gas_ozonio = medicao_dict.get('gasOzonio', None)
                temperatura = medicao_dict.get('temperatura', None)
                umidade = medicao_dict.get('umidade', None)
                data = medicao_dict.get('data', None)
                medicao = Medicao(id, dispositivo_id, materia_particulada, gas, nitrogenio, gas_ozonio, temperatura, umidade, data)
                resultado.append(medicao)
        return resultado