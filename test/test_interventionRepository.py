from unittest import TestCase
from src.entities import intervention

class TestintervientionRepository(TestCase):
    def test_get_intervetion_by_id(self):
        get_inter = get_by_id(1);
        print(get_inter)
        self.assertEqual(get_inter['piece'],"test01")

    def test_get_all_interventions(self):
        curseur = get_cursor()
        query = "SELECT * FROM intervention"
        interventions = curseur.execute(query).fetchall()
        self.assertEqual(interventions[0],{"idClient": 2,
            "idIntervention": 1,
            "idTechnicien": 1,
            "piece": "test01",
            "probleme": "probleme01"
        })

    def test_insert_intervetion(self):
        intervention01 = intervention(54, 48, 'test02', 'probleme02')
        test_insert = add_intervention(intervention)
        print(test_insert)
        self.assertEqual(test_insert, 1)
