""" Module de notification """
from abc import ABC, abstractmethod
from classes_principales.classes_principales import Membre, List


class NotificationStrategy(ABC):
    """L'interface de notification strategy"""

    # pylint: disable=too-few-public-methods
    @abstractmethod
    def envoyer(self, message: str, destinataire: Membre):
        """Methode abstraite qui permet envoyer des message"""


class EmailNotificationStrategy(NotificationStrategy):
    """Classe d'email de notification"""

    # pylint: disable=too-few-public-methods
    def envoyer(self, message: str, destinataire: Membre):
        print(f"Notification envoyé à {destinataire.nom} par email: {message}")


class SMSNotificationStrategy(NotificationStrategy):
    """Classe qui permet d'envoyer des notification par SMS"""

    # pylint: disable=too-few-public-methods
    def envoyer(self, message: str, destinataire: Membre):
        """Methode qui permet d'envoyer les SMS"""
        print(f"Envoi d'un SMS à {destinataire.nom}: {message}")


class PushNotificationStrategy(NotificationStrategy):
    """Classe qui permet d'envoyer des notification push"""

    # pylint: disable=too-few-public-methods
    def envoyer(self, message: str, destinataire: Membre):
        print(f"Envoi d'une notification push à {destinataire.nom}: {message}")


class NotificationContext:
    """Classe de notification context"""

    # pylint: disable=too-few-public-methods
    def __init__(self, strategy: NotificationStrategy):
        """Methode qui permet d'initialiser les notifications"""
        self.strategy = strategy

    def notifier(self, message: str, destinataires: List[Membre]):
        """Methode qui permet d'envoyer des notification"""
        for destinataire in destinataires:
            self.strategy.envoyer(message, destinataire)
