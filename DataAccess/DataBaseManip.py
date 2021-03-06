import sqlite3
import os
from entities.intervention import Intervention
from entities.technicien import Technicien
from repositories.technicienRepository import technicienRepository
from repositories.interventionRepository import intervientionRepository

try:
    # Connexion BDD ----------------------------------------------------------

    os.remove("maBase.db")
    connexion = sqlite3.connect("maBase.db")
    curseur = connexion.cursor()

    # Create Table ----------------------------------------------------------

    intervientionRepository.createIntervention()
    technicienRepository.createTechnicien()

    # InsertToTable ----------------------------------------------------------

    inter1 = Intervention(1, "test", "test")
    inter2 = Intervention(1, "test2", "test2")
    inter3 = Intervention(2, "test3", "test3")
    inter4 = Intervention(2, "test3", "test3")
    inter5 = Intervention(3, "test3", "test3")

    list(map(intervientionRepository.insertIntervention, (inter1, inter2, inter3, inter4, inter5)))

    tec1 = Technicien("Michel", "Dupont")
    tec2 = Technicien("Paul", "Antoine")
    tec3 = Technicien("test", "test")

    list(map(technicienRepository.insertTechnicien, (tec1, tec2, tec3)))

    # SelectToTable ----------------------------------------------------------

    intervientionRepository.selectIntervention()

    technicienRepository.selectTechnicien()

except Exception as exc:
    print(exc)
