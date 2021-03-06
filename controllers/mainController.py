import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/api/technicien/all', methods=['GET'])
def test():
    connexion = sqlite3.connect('../DataAccess/maBase.db')
    connexion.row_factory = dict_factory
    curseur = connexion.cursor()
    technicien = curseur.execute('SELECT * FROM technicien;').fetchall()

    return jsonify(technicien)


@app.route(f'/api/technicien', methods=['GET'])
def getOneTechnicien():

    query_parameters = request.args

    id = query_parameters.get('id')

    query = "SELECT * FROM technicien WHERE"
    to_filter = []

    if id:
        query += ' id_tec = ?'
        to_filter.append(id)

    if not id:
        return "Vous avez oubliez de rentrer un id ou soit le technicien n'existe pas"

    conn = sqlite3.connect('../DataAccess/maBase.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)


@app.route(f'/api/technicien/intervention', methods=['GET'])
def getTechnicienIntervention():
    query_parameters = request.args

    id = query_parameters.get('id')

    query = "SELECT * FROM intervention WHERE"
    to_filter = []

    if id:
        query += ' id_tec = ?'
        to_filter.append(id)

    if not id:
        return "Vous avez oubliez de rentrer un id ou soit le technicien n'existe pas"

    conn = sqlite3.connect('../DataAccess/maBase.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()
    print(query)
    return jsonify(results)


@app.route('/api/intervention/all', methods=['GET'])
def getIntervention():
    connexion = sqlite3.connect('../DataAccess/maBase.db')
    connexion.row_factory = dict_factory
    curseur = connexion.cursor()
    intervention = curseur.execute('SELECT * FROM intervention;').fetchall()

    return jsonify(intervention)


@app.route(f'/api/intervention', methods=['GET'])
def getOneIntervention():

    query_parameters = request.args

    id = query_parameters.get('id')

    query = "SELECT * FROM intervention WHERE"
    to_filter = []

    if id:
        query += ' id_int = ?'
        to_filter.append(id)

    if not id:
        return "Vous avez oubliez de rentrer un id ou soit l'intervention est n'existe pas"

    conn = sqlite3.connect('../DataAccess/maBase.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()
    print(query)
    return jsonify(results)


app.run()
