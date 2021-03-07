import sqlite3
import os
import json

from definitions import DB_PATH
from entities.intervention import Intervention
from entities.technicien import Technicien
from repositories.technicienRepository import technicienRepository
from repositories.interventionRepository import intervientionRepository


def CreationBDD():
    try:
        # Connexion BDD ----------------------------------------------------------

        os.remove(DB_PATH)
        connexion = sqlite3.connect(DB_PATH)
        curseur = connexion.cursor()

        # Create Table ----------------------------------------------------------

        intervientionRepository.createIntervention()
        technicienRepository.createTechnicien()

        # InsertToTable ----------------------------------------------------------

        inter1 = Intervention(1, "test", "test")
        inter2 = Intervention(1, "test2", "test2")
        inter3 = Intervention(2, "test3", "test3")
        inter4 = Intervention(2, "test4", "test4")
        inter5 = Intervention(3, "test5", "test5")
        inter6 = Intervention(3, "test6", "test6")

        list(map(intervientionRepository.insertIntervention, (inter1, inter2, inter3, inter4, inter5, inter6)))

        tec1 = Technicien("Michel", "Dupont")
        tec2 = Technicien("Paul", "Antoine")
        tec3 = Technicien("test", "test")

        list(map(technicienRepository.insertTechnicien, (tec1, tec2, tec3)))

        # SelectToTable ----------------------------------------------------------

        resIntervention = intervientionRepository.selectIntervention()
        print(json.dumps(resIntervention))

        resTechnicien = technicienRepository.selectTechnicien()
        print(json.dumps(resTechnicien))

    except Exception as exc:
        print(exc)


CreationBDD()