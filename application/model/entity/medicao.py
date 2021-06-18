from datetime import datetime

class Medicao:
    def __init__(self, id, dispositivoId, materiaParticulada, gas, nitrogenio, gasOzonio, temperatura, umidade, data):
        self._id = id
        self._dispositivoId = dispositivoId
        self._materiaParticulada = materiaParticulada
        self._gas = gas
        self._nitrogenio = nitrogenio
        self._gasOzonio = gasOzonio
        self._temperatura = temperatura
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
        return self._dispositivoId
    
    @dispositivoId.setter
    def dispositivoId(self, value:int):
        self._dispositivoId = value

    @property
    def materiaParticulada(self) -> float:
        return self._materiaParticulada
    
    @materiaParticulada.setter
    def materiaParticulada(self, value: float):
        self._materiaParticulada = value

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
        return self._gasOzonio
    
    @gasOzonio.setter
    def gasOzonio(self, value: float):
        self._gasOzonio = value

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
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value
    
    def toDict(self) -> dict:
        return {
            "id": self._id,
            "dispositivoId": self._dispositivoId,
            "materiaParticulada": self._materiaParticulada,
            "gas": self._gas,
            "nitrogenio": self._nitrogenio,
            "gasOzonio": self._gasOzonio,
            "temperatura": self._temperatura,
            "umidade": self._umidade,
            "data": self._data
        }

    