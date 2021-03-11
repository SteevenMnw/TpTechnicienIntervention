import sqlite3

from definitions import DB_PATH
from repositories.utils import dict_factory


class technicienRepository:

    @staticmethod
    def insertTechnicien(tec):
        connexion = sqlite3.connect(DB_PATH)
        curseur = connexion.cursor()
        cmd = f"INSERT INTO technicien (nom, prenom) VALUES (?, ?)"
        curseur.execute(cmd, [tec.nom, tec.prenom])
        connexion.commit()

    @staticmethod
    def selectTechnicien():
        connexion = sqlite3.connect(DB_PATH)
        connexion.row_factory = dict_factory
        curseur = connexion.cursor()
        cmd = "SELECT * FROM technicien"
        return curseur.execute(cmd).fetchall()

    @staticmethod
    def selectTechnicienById(id):
        connexion = sqlite3.connect(DB_PATH)
        connexion.row_factory = dict_factory
        curseur = connexion.cursor()
        cmd = " SELECT * FROM technicien WHERE id_tec = ?"
        return curseur.execute(cmd, [id]).fetchall()


    @staticmethod
    def createTechnicien():
        connexion = sqlite3.connect(DB_PATH)
        curseur = connexion.cursor()
        sqlCreateTableTechnicien = f"CREATE TABLE IF NOT EXISTS technicien(" \
                                   f" id_tec INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE," \
                                   f" nom VARCHAR," \
                                   f" prenom VARCHAR)"

        curseur.execute(sqlCreateTableTechnicien)
