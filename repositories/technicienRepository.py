import sqlite3

from entities.technicien import Technicien


class technicienRepository:

    @staticmethod
    def insertTechnicien(tec):
        connexion = sqlite3.connect("maBase.db")
        curseur = connexion.cursor()
        cmd = f"INSERT INTO technicien (nom, prenom) VALUES ('{tec.nom}','{tec.prenom}')"
        curseur.execute(cmd)
        connexion.commit()

    @staticmethod
    def selectTechnicien():
        connexion = sqlite3.connect("maBase.db")
        curseur = connexion.cursor()
        cmd = "SELECT * FROM technicien"
        curseur.execute(cmd)
        lstTechnicien = []

        print()
        print("Les Techniciens :")
        for row in curseur:
            lstTechnicien.append(Technicien(row[1], row[2]))

        for elem in lstTechnicien:
            print(f"{elem.nom} - {elem.prenom}")

    @staticmethod
    def createTechnicien():
        connexion = sqlite3.connect("maBase.db")
        curseur = connexion.cursor()
        sqlCreateTableTechnicien = f"CREATE TABLE IF NOT EXISTS technicien(" \
                                   f" id_tec INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE," \
                                   f" nom INTEGER," \
                                   f" prenom VARCHAR)"

        curseur.execute(sqlCreateTableTechnicien)