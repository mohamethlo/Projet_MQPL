from projet.projet import Projet, Tache, Risque, Jalon, date
from notification.notifications import *

# Création d'un projet
projet = Projet(
    "Projet MQPL", "Description du projet", date(2024, 5, 30), date(2024, 12, 31)
)

# Ajout de membres d'équipe
membre1 = Membre("Bakh Diop", "Chef de projet")
membre2 = Membre("Babacar Gueye", "Développeur")
projet.ajouter_membre_equipe(membre1)
projet.ajouter_membre_equipe(membre2)

# Affichage de notification
email_strategy = EmailNotificationStrategy()
projet.set_notification_strategy(email_strategy)
ajout_notification = f"{membre1.nom} a été ajouté a l'équipe"
projet.notifier(ajout_notification, projet.equipe.obtenir_membres())

ajout_tache_notification = "Nouvelle tâche ajoutée : Analyse des besoins "
projet.notifier(ajout_tache_notification, projet.equipe.obtenir_membres())

ajout_tache_notification1 = "Nouvelle tâche ajoutée : Developpement "
projet.notifier(ajout_tache_notification1, projet.equipe.obtenir_membres())

ajout_budget_notification = "Le budget du projet a été define à 50000 Unité Monétaire"
projet.notifier(ajout_budget_notification, projet.equipe.obtenir_membres())

ajout_risque_notification = "Nouveau risque ajouté: Retard de livraison"
projet.notifier(ajout_risque_notification, projet.equipe.obtenir_membres())

ajout_jalon_notification = "Nouveau jalon ajouté: Phase 1 terminée"
projet.notifier(ajout_jalon_notification, projet.equipe.obtenir_membres())

ajout_changement_notification = (
    "Changement enregistré: Changement de la portée du sujet (version 2)"
)
projet.notifier(ajout_changement_notification, projet.equipe.obtenir_membres())

print(
    "\n########################################################################################################## \n"
)

# Ajout de tâches
tache1 = Tache(
    "Tâche 1",
    "Description de la tâche 1",
    date(2024, 6, 1),
    date(2024, 6, 15),
    membre1,
    "En cours",
)
tache2 = Tache(
    "Tâche 2",
    "Description de la tâche 2",
    date(2024, 6, 10),
    date(2024, 6, 30),
    membre2,
    "En attente",
)
projet.ajouter_tache(tache1)
projet.ajouter_tache(tache2)

# Ajout de chemin critique
projet.calculer_chemin_critique()

# Ajout de jalons
jalon1 = Jalon("Jalon 1", date(2024, 6, 15))
jalon2 = Jalon("Jalon 2", date(2024, 6, 30))
projet.ajouter_jalon(jalon1)
projet.ajouter_jalon(jalon2)

# Ajout de risques
risque1 = Risque("Problème de ressources", 0.3, "Élevé")
risque2 = Risque("Retard dans la livraison", 0.2, "Moyen")
projet.ajouter_risque(risque1)
projet.ajouter_risque(risque2)

# Génération d'un rapport de performance
rapport = projet.generer_rapport_performance
print(rapport)
