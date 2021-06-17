from application.model.entity.medicao import Medicao
from application.model.dao.medicao_dao import MedicaoDAO
import datetime
from application import app
from flask import jsonify, request

medicao_list = MedicaoDAO().listarTodos()

@app.route('/medicao', methods=['GET'])
def listarMedicao():
    medicao_dict = []
    for medicao in medicao_list:
        medicao_dict.append(medicao.toDict())
    return jsonify(medicao_dict)

@app.route('/medicao', methods=['POST'])
def addMedicao():
    id = len(medicao_list) + 1
    dispositivoId = request.json.get('dispositivoId', None)
    materia_particulada = float(request.json.get('materiaParticulada', None))
    gas = float(request.json.get('gas', None))
    nitrogenio = float(request.json.get('nitrogenio', None))
    gas_ozonio = float(request.json.get('gasOzonio', None))
    temperatura = float(request.json.get('temperatura', None))
    umidade = float(request.json.get('umidade', None))
    data = datetime(request.json.get('data', None))
    medicao = Medicao(id, dispositivoId, materia_particulada, gas, nitrogenio, gas_ozonio, temperatura, umidade, data)
    MedicaoDAO().inserir(medicao)
    return medicao.toDict(), 201

@app.route('/medicao/dispositivo/<int:id>', methods=['GET'])
def buscarMedicaoDispositivo(id):
    medicao_dispositivo = []
    for medicao in medicao_list:
        if id == medicao._dispositivo_id:
            medicao_dispositivo.append(medicao.toDict())
    return jsonify(medicao_dispositivo)

@app.route('/medicao/data/<int:data>', methods=['GET'])
def buscarMedicaoData(data):
    medicao_data = []
    for medicao in medicao_list:
        if data == medicao._data:
            medicao_data.append(medicao.toDict())
    return jsonify(medicao_data)