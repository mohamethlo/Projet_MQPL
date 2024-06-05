""" Module classes_principales """

from datetime import date
from typing import List

# vulture: noqa


class Membre:
    """Représente un membre avec un nom et un rôle."""

    # pylint: disable=too-few-public-methods
    def __init__(self, nom: str, role: str):
        """Initialise un membre avec un nom et un rôle."""
        self.nom = nom
        self.role = role


# vulture: noqa


class Tache:
    """Représente une tache avec un nom, une description,
    date de debut, date de fin et la statut .
    """

    def __init__(
        self, nom, description, date_debut, date_fin, responsable, statut
    ):  # pylint: disable=too-many-arguments
        """Représente une tâche avec un nom, une description,
        une date de début et de fin, un responsable, et un statut.
        """
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.responsable = responsable
        self.statut = statut
        self.dependances = []

    def ajouter_dependance(self, tache: "Tache"):
        """Methode qui permet d'ajouter des dependance"""
        self.dependances.append(tache)

    def mettre_a_jour_statut(self, statut: str):
        """Methode qui permet de mettre a jour le status"""
        self.statut = statut


class Jalon:
    """La classe Jalon"""

    # pylint: disable=too-few-public-methods
    def __init__(self, nom: str, date_: date):
        self.nom = nom
        self.date = date_


class Risque:
    """La classe risque"""

    # pylint: disable=too-few-public-methods
    def __init__(self, description: str, probabilite: float, impact: str):
        self.description = description
        self.probabilite = probabilite
        self.impact = impact


class Changement:
    """La classe changement"""

    # pylint: disable=too-few-public-methods
    def __init__(self, description: str, version: int, date_: date):
        self.description = description
        self.version = version
        self.date = date_


class Equipe:
    """La classe equipe"""

    def __init__(self):
        """Methode qui permet d'initialiser la classe"""
        self.membres = []

    def ajouter_membre(self, membre: Membre):
        """Methode qui permet d'ajouter un membre"""
        self.membres.append(membre)

    def obtenir_membres(self) -> List[Membre]:
        """Methode qui permet de recuperer tous les membres"""
        return self.membres
