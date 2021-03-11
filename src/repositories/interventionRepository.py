import sqlite3

from definitions import DB_PATH
from repositories.utils import dict_factory


class intervientionRepository:

    @staticmethod
    def insertIntervention(inter):
        connexion = sqlite3.connect(DB_PATH)
        curseur = connexion.cursor()
        cmd = f"INSERT INTO intervention (id_tec, piece, probleme) VALUES (?, ?, ?)"
        curseur.execute(cmd, [inter.id_tec, inter.piece, inter.probleme])
        connexion.commit()

    @staticmethod
    def selectIntervention():
        connexion = sqlite3.connect(DB_PATH)
        connexion.row_factory = dict_factory
        curseur = connexion.cursor()
        cmd = "SELECT * FROM intervention"
        return curseur.execute(cmd).fetchall()


    @staticmethod
    def selectInterventionById(id):
        connexion = sqlite3.connect(DB_PATH)
        connexion.row_factory = dict_factory
        curseur = connexion.cursor()
        cmd = " SELECT * FROM intervention WHERE id_int = ?"
        return curseur.execute(cmd, [id]).fetchall()

    @staticmethod
    def selectInterventionByIdTec(id_tec):
        connexion = sqlite3.connect(DB_PATH)
        connexion.row_factory = dict_factory
        curseur = connexion.cursor()
        cmd = " SELECT * FROM intervention WHERE id_tec = ?"
        return curseur.execute(cmd, [id_tec]).fetchall()



    @staticmethod
    def createIntervention():
        connexion = sqlite3.connect(DB_PATH)
        curseur = connexion.cursor()
        sqlCreateTableIntervention = f"CREATE TABLE IF NOT EXISTS intervention(" \
                                     f" id_int INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE," \
                                     f" id_tec INTEGER," \
                                     f" piece VARCHAR," \
                                     f" probleme VARCHAR)"

        curseur.execute(sqlCreateTableIntervention)
