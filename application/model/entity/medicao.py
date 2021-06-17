from datetime import datetime

class Medicao:
    def __init__(self, id, dispositivo_id, materia, gas, nitrogenio, ozonio, temp, umidade, data):
        self._id = id
        self._dispositivo_id = dispositivo_id
        self._materia_particulada = materia
        self._gas = gas
        self._nitrogenio = nitrogenio
        self._gas_ozonio = ozonio
        self._temperatura = temp
        self._umidade = umidade
        self._data = data
      
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value:int):
        self._id = value

    @property
    def dispositivoId(self) -> int:
        return self._dispositivo_id
    
    @dispositivoId.setter
    def dispositivoId(self, value:int):
        self._dispositivo_id = value

    @property
    def materiaParticulada(self) -> float:
        return self._valor
    
    @materiaParticulada.setter
    def materiaParticulada(self, value: float):
        self._valor = value

    @property
    def gas(self) -> float:
        return self._gas
    
    @gas.setter
    def gas(self, value: float):
        self._gas = value
    
    @property
    def nitrogenio(self) -> float:
        return self._nitrogenio
    
    @nitrogenio.setter
    def nitrogenio(self, value: float):
        self._nitrogenio = value

    @property
    def gasOzonio(self) -> float:
        return self._gas_ozonio
    
    @gasOzonio.setter
    def gasOzonio(self, value: float):
        self._gas_ozonio = value

    @property
    def temperatura(self) -> float:
        return self._temperatura
    
    @temperatura.setter
    def temperatura(self, value: float):
        self._temperatura = value

    @property
    def umidade(self) -> float:
        return self._umidade
    
    @umidade.setter
    def umidade(self, value: float):
        self._umidade = value

    @property
    def data(self) -> datetime:
        return self._data
    
    @data.setter
    def data(self, value:datetime):
        self._data = value
    
    def toDict(self) -> dict:
        return {
            "id": self._id,
            "dispositivoId": self._dispositivo_id,
            "materiaParticulada": self._materia_particulada,
            "gas": self._gas,
            "nitrogenio": self._nitrogenio,
            "gasOzonio": self._gas_ozonio,
            "temperatura": self._temperatura,
            "umidade": self._umidade,
            "data": self._data
        }

    