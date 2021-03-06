import sqlite3

from entities.intervention import Intervention


class intervientionRepository:

    @staticmethod
    def insertIntervention(inter):
        connexion = sqlite3.connect("maBase.db")
        curseur = connexion.cursor()
        cmd = f"INSERT INTO intervention (id_tec, piece, probleme) VALUES ({inter.id_tec}, '{inter.piece}','{inter.probleme}')"
        curseur.execute(cmd)
        connexion.commit()

    @staticmethod
    def selectIntervention():
        connexion = sqlite3.connect("maBase.db")
        curseur = connexion.cursor()
        cmd = "SELECT * FROM intervention"
        curseur.execute(cmd)
        lstIntervention = []

        print("Les Interventions :")
        for row in curseur:
            lstIntervention.append(Intervention(row[1], row[2], row[3]))

        for elem in lstIntervention:
            print(f"{elem.id_tec} - {elem.piece} - {elem.probleme}")

    @staticmethod
    def createIntervention():
        connexion = sqlite3.connect("maBase.db")
        curseur = connexion.cursor()
        sqlCreateTableIntervention = f"CREATE TABLE IF NOT EXISTS intervention(" \
                                     f" id_int INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE," \
                                     f" id_tec INTEGER," \
                                     f" piece VARCHAR," \
                                     f" probleme VARCHAR)"

        curseur.execute(sqlCreateTableIntervention)
