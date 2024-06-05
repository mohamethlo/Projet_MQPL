""" Module du projet """

from datetime import datetime, date
from typing import Optional

from classes_principales.classes_principales import (
    Equipe,
    Tache,
    Membre,
    Risque,
    Jalon,
    Changement,
    List,
)
from notification.notifications import NotificationStrategy, NotificationContext


class Projet:  # pylint: disable=too-many-instance-attributes
    """Classe projet"""

    # pylint: disable=too-few-public-methods
    def __init__(self, nom: str, description: str, date_debut: date, date_fin: date):
        """Methode qui permet d'initialiser la classe projet"""
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.taches: List[Tache] = []
        self.equipe = Equipe()
        self.budget = 0.0
        self.risques: List[Risque] = []
        self.jalons: List[Jalon] = []
        self.version = 0
        self.changements: List[Changement] = []
        self.chemin_critique: List[Tache] = []
        self.notification_context: Optional[NotificationContext] = None

    def set_notification_strategy(self, strategy: NotificationStrategy):
        """Methode qui permet de modifier la strategie de notification"""
        self.notification_context = NotificationContext(strategy)

    def ajouter_tache(self, tache: Tache):
        """Methode qui permet d'ajouter une tache"""
        self.taches.append(tache)

    def ajouter_membre_equipe(self, membre: Membre):
        """Methode qui permet d'ajouter un membre"""
        self.equipe.ajouter_membre(membre)

    def definir_budget(self, budget: float):
        """Methode qui permet de definir un budget"""
        self.budget = budget

    def ajouter_risque(self, risque: Risque):
        """Methode qui permet d'ajouter une risque"""
        self.risques.append(risque)

    def ajouter_jalon(self, jalon: Jalon):
        """Methode qui permet d'ajouter un jalon"""
        self.jalons.append(jalon)

    def enregistrer_changement(self, description: str):
        """Methode qui permet d'enregistrer un changement"""
        self.version += 1
        changement = Changement(description, self.version, datetime.now())
        self.changements.append(changement)

    @property
    def generer_rapport_performance(self):
        """Methode qui permet de generer le rapport de performance"""
        membres_equipe = "\n".join(
            [
                f"- {membre.nom} ({membre.role})"
                for membre in self.equipe.obtenir_membres()
            ]
        )
        tache_a_faire = "\n".join(
            [
                f"- {tache_faire.nom} "
                f"({tache_faire.date_debut} à {tache_faire.date_fin}),"
                f" Responsable: {tache_faire.responsable.nom}, "
                f"Statut: {tache_faire.statut}"
                for tache_faire in self.taches
            ]
        )
        jalon_etat = "\n".join(
            [f"- {jalon.nom} ({jalon.date})" for jalon in self.jalons]
        )
        les_risques = "\n".join(
            [
                f"- {risque.description} "
                f"(Probabilite: {risque.probabilite}, "
                f"Impact: {risque.impact})"
                for risque in self.risques
            ]
        )
        chemin_critique = "\n".join(
            [
                f"- {critique_chemin.nom} "
                f"({critique_chemin.date_debut} à {critique_chemin.date_fin})"
                for critique in self.chemin_critique
                for critique_chemin in critique
            ]
        )
        rapport = (
            f"Rapport d'activités du projet '{self.nom}':\n"
            f"Version: {self.version}\n"
            f"Dates: {self.date_debut} à {self.date_fin}\n"
            f"Budget: {self.budget} Unité Monétaire\n"
            f"Equipes:\n{membres_equipe}\n"
            f"Taches:\n{tache_a_faire}\n"
            f"Jalons:\n{jalon_etat}\n"
            f"Risques:\n{les_risques}\n"
            f"Chemin critique:\n{chemin_critique}\n"
        )

        return rapport

    def calculer_chemin_critique(self):
        """Methode qui permet de calculer le chemin critique"""
        self.chemin_critique.append(self.taches)

    def notifier(self, message: str, destinataires: List[Membre]):
        """Methode qui permet d'envoyer des notification"""
        if self.notification_context:
            self.notification_context.notifier(message, destinataires)
