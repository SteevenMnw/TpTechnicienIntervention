import flask
from flask import request, jsonify

from entities.intervention import Intervention
from entities.technicien import Technicien
from repositories.technicienRepository import technicienRepository
from repositories.interventionRepository import intervientionRepository

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/technicien/all', methods=['GET'])
def test():
    return jsonify(technicienRepository.selectTechnicien())


@app.route(f'/api/technicien', methods=['GET'])
def getOneTechnicien():

    query_parameters = request.args

    id = query_parameters.get('id')

    if not id:
        return "Vous avez oubliez de rentrer un id ou soit le technicien n'existe pas"

    return jsonify(technicienRepository.selectTechnicienById(id))


@app.route(f'/api/technicien/intervention', methods=['GET'])
def getTechnicienIntervention():
    query_parameters = request.args

    id = query_parameters.get('id')

    if not id:
        return "Vous avez oubliez de rentrer un id ou soit le technicien n'existe pas"

    return jsonify(intervientionRepository.selectInterventionByIdTec(id))


@app.route('/api/intervention/all', methods=['GET'])
def getIntervention():
    return jsonify(intervientionRepository.selectIntervention())


@app.route(f'/api/intervention', methods=['GET'])
def getOneIntervention():

    query_parameters = request.args

    id = query_parameters.get('id')

    if not id:
        return "Vous avez oubliez de rentrer un id ou soit l'intervention est n'existe pas"

    return jsonify(intervientionRepository.selectInterventionById(id))



@app.route(f'/api/intervention', methods=['POST'])
def createIntervention():

    id_tec = request.form.get('id_tec')
    piece = request.form.get('piece')
    probleme = request.form.get('probleme')

    if not id_tec:
        return "Vous avez oubliez de rentrer un id ou soit le technicien n'existe pas"

    if not piece:
        return "Vous avez oubliez de rentrer la piece"

    if not probleme:
        return "Vous avez oubliez de rentrer un probleme"

    intervention = Intervention(id_tec, piece, probleme)
    intervientionRepository.insertIntervention(intervention)

    return "OK"\

@app.route(f'/api/technicien', methods=['POST'])
def createTechnicien():

    nom = request.form.get('nom')
    prenom = request.form.get('prenom')

    if not nom:
        return "Vous avez oubliez de rentrer le nom du technicien"

    if not prenom:
        return "Vous avez oubliez de rentrer le prenom du technicien"

    technicien = Technicien(nom, prenom)
    technicienRepository.insertTechnicien(technicien)

    return "OK"


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Il y a une erreur dans l'url.</p>", 404


app.run()
