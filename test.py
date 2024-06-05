""" Module test """

import unittest
from notification.notifications import EmailNotificationStrategy
from projet.projet import Projet, Membre, Tache, date, Jalon, Risque


class TestProjet(unittest.TestCase):
    """Classe testProjet"""

    def setUp(self):
        """Methode qui permet de definir des instruction
        qui seront execute avant chaque intruction
        """
        self.projet = Projet(
            "Projet Test", "Description de test", date(2024, 1, 1), date(2024, 12, 31)
        )
        self.membre1 = Membre("Mohameth", "Chef de projet")
        self.tache1 = Tache(
            "Tâche 1",
            "Description de la tâche 1",
            date(2024, 6, 1),
            date(2024, 6, 15),
            self.membre1,
            "En cours",
        )

        self.jalon1 = Jalon("Jalon 1", date(2024, 6, 15))
        self.risque1 = Risque("Problème de ressources", 0.3, "Élevé")

    def test_set_notification_strategy(self):
        """Methode qui permet de tester les notification"""
        email_strategy = EmailNotificationStrategy()
        self.projet.set_notification_strategy(email_strategy)
        self.assertEqual(self.projet.notification_context.strategy, email_strategy)

    def test_ajouter_membre(self):
        """Methode qui permet de tester l'ajout d'un membre"""
        self.projet.ajouter_membre_equipe(self.membre1)
        self.assertIn(self.membre1, self.projet.equipe.obtenir_membres())

    def test_definir_budget(self):
        """Methode qui permet de tester la definition du budget"""
        budget = 100000.0
        self.projet.definir_budget(budget)
        self.assertEqual(self.projet.budget, budget)

    def test_ajouter_tache(self):
        """Methode qui permet de tester l'ajout d'une tache"""
        self.projet.ajouter_tache(self.tache1)
        self.assertIn(self.tache1, self.projet.taches)

    def test_ajouter_jalon(self):
        """Methode qui permet de tester 'ajout d'une jalon"""
        self.projet.ajouter_jalon(self.jalon1)
        self.assertIn(self.jalon1, self.projet.jalons)

    def test_ajouter_risque(self):
        """Methode qui permet de tester l'ajout d'une risque"""
        self.projet.ajouter_risque(self.risque1)
        self.assertIn(self.risque1, self.projet.risques)

    def test_enregistrer_changement(self):
        """Methode qui permet de tester l'enregistrement d'un changement"""
        description_changement = "Modification de la description du projet"
        self.projet.enregistrer_changement(description_changement)

        # Vérifiez que le changement a été enregistré
        self.assertEqual(len(self.projet.changements), 1)
        dernier_changement = self.projet.changements[-1]
        self.assertEqual(dernier_changement.description, description_changement)
        self.assertEqual(dernier_changement.version, 1)

    def test_notifier_email(self):
        """Methode qui permet de tester les notification par email"""
        email_strategy = EmailNotificationStrategy()
        self.projet.set_notification_strategy(email_strategy)
        self.projet.ajouter_membre_equipe(self.membre1)
        self.projet.notifier("Message de test", self.projet.equipe.obtenir_membres())

    def test_generer_rapport_performance(self):
        """Methode qui permet de tester la generation du rapport de performance"""
        self.projet.ajouter_membre_equipe(self.membre1)
        self.projet.ajouter_tache(self.tache1)
        self.projet.ajouter_jalon(self.jalon1)
        self.projet.ajouter_risque(self.risque1)
        rapport = self.projet.generer_rapport_performance
        self.assertIn("Projet Test", rapport)
        self.assertIn("Mohameth (Chef de projet)", rapport)
        self.assertIn("Tâche 1", rapport)
        self.assertIn("Jalon 1", rapport)
        self.assertIn("Problème de ressources", rapport)


if __name__ == "__main__":
    unittest.main()
