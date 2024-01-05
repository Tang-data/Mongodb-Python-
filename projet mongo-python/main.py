import recherche
from stat_db import Statistics
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

def rechercher_livre():
    print('-------------------------')
    print("1 pour rechercher par type")
    print("2 pour rechercher par titre")
    print("3 pour rechercher par année de publication")
    print("4 pour rechercher par nom d'auteur")
    print("5 pour revenir au menu précédent")
    print('-------------------------')
    choix = input(("Entrez votre choix : ")) 
    match choix :
        case "1" : 
            recherche.recherche_livre(input("Saisissez le type d'oeuvre à rechercher : ") , choix)
        case "2" : 
            recherche.recherche_livre(input("Saississez le titre de l'oeuvre à rechercher : "), choix)
        case "3" : 
            recherche.recherche_livre(input("Saisissez l'année de la publication que vous recherchez : "), choix)
        case "4" : 
            recherche.recherche_livre(input("Saississez le nom de l'auteur : "), choix)
        case "5" :
            pass
        case _ : 
            print(Fore.RED + "mauvaise saisie")

def menu_utilisateur_base():
    print('-------------------------')
    print("1 pour rechercher une oeuvre")
    print("2 pour ajouter une oeuvre")
    print("3 pour supprimer une oeuvre en utilisant son identifiant")
    print("4 supprimer plusieurs oeuvres en utilisant le nom d'un auteur")
    print("5 pour obtenir les statistiques de la base de donnée")
    print('-------------------------')
    choix = input(("Entrez votre choix : "))
    match choix:
        case "1": 
            rechercher_livre()
        case "2": 
            Oeuvre.creer_nouveau_document()
        case "3": 
            Oeuvre.suppression_livre()
        case "4":
            Oeuvre.suppression_livre_multiple()
        case "5":
            Statistics.affichage_stats_db()
        case _: 
            print(Fore.RED + "mauvaise saisie")          
        
while True :
    menu_utilisateur_base() 
