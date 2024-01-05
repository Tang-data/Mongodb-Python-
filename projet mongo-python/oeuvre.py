import pprint
import pandas as pd
from pymongo import MongoClient
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)
client = MongoClient()
db = client["test"]
collection = db["books"]

class Oeuvre(object):

    def recherche_livre_type (self:str) :
        index_to_start = 1
        type_livre = collection.aggregate([
            {"$match" : {"type" : self }},{"$sort" : {"year" : 1}},{"$limit" : 5}])
        df = pd.DataFrame(type_livre,columns = ["title", "authors", "year", "type", "_id", ])
        df.insert(0,"index",range(1, len(df)+1))
        df.set_index("index", inplace=True)
        if len(df) >0 :
            print(Fore.YELLOW + Style.DIM + str(df))
            print('-------------------------')
            print("Il existe " + str(collection.count_documents({"type" : self })) + " documents de ce type")
        if len(df) == 0 :
            types_existants = collection.aggregate([{"$group" :{"_id" : "$type"}}])
            print("les types de documents existants sont : ")
            for i in types_existants :
                print(Fore.MAGENTA + Style.BRIGHT + str(i) + Style.RESET_ALL) 
        if collection.count_documents({"type" : self }) > 5 :
            i = 5
            while i < collection.count_documents({"type" : self }) :
                print('-------------------------')
                choix = input(Fore.BLACK + Style.DIM + Back.WHITE +"souhaitez vous voir plus de résultats : Y/N " + Style.RESET_ALL + " ")
                match choix:
                    case "Y": 
                        index_to_start += 5
                        type_livre = collection.aggregate([
                        {"$match" : {"type" : self }},{"$sort" : {"year" : 1}},{"$skip" : i}, {"$limit" : 5}])
                        i += 5
                        df = pd.DataFrame(type_livre,columns = ["title", "authors", "year", "type", "_id"])
                        df.insert(0,"index",range(index_to_start, len(df)+index_to_start))
                        df.set_index("index", inplace=True)
                        print(Fore.YELLOW + Style.DIM + str(df))
                    case "N": 
                        break
                    case _: 
                        print('-------------------------')
                        print(Fore.RED + "mauvaise saisie")
        else : 
            pass
                
    def recherche_livre_titre (self:str) :
        index_to_start = 1 
        titre_livre = collection.aggregate([
        {"$match" : {"title" :{"$regex" : self , "$options" : "i" }}}, {"$limit" : 5}])
        df = pd.DataFrame(titre_livre,columns = ["title", "authors", "year", "type", "_id"])
        df.insert(0,"index",range(1, len(df)+1))
        df.set_index("index", inplace=True)
        if len(df) >0 :
            print(Fore.YELLOW + Style.DIM + str(df))
        print('-------------------------')
        print("Il existe " + str(collection.count_documents({"title" :{"$regex" : self , "$options" : "i" }})) + " documents contenant ce terme dans leur titre")
        if collection.count_documents({"title" :{"$regex" : self , "$options" : "i" }}) > 5 :
            i = 5
            while i < collection.count_documents({"title" :{"$regex" : self , "$options" : "i" }}) :
                print('-------------------------')
                choix = input(Fore.BLACK + Style.DIM + Back.WHITE +"souhaitez vous voir plus de résultats : Y/N " + Style.RESET_ALL + " ")
                match choix:
                    case "Y":
                        index_to_start += 5
                        titre_livre = collection.aggregate([
                        {"$match" : {"title" :{"$regex" : self , "$options" : "i" }}}, {"$skip" : i}, {"$limit" : 5}])
                        df = pd.DataFrame(titre_livre, columns = ["title", "authors", "year", "type", "_id"])
                        df.insert(0,"index",range(index_to_start, len(df)+index_to_start))
                        df.set_index("index", inplace=True)
                        print(Fore.YELLOW + Style.DIM + str(df))
                        i += 5
                    case "N": 
                        break
                    case _: 
                        print('-------------------------')
                        print(Fore.RED + "mauvaise saisie")
        else : 
            pass

    def recherche_livre_annee () :
        index_to_start = 1
        try :
            self = int(input("Entrez l'année de publication recherchée : "))
        except :
            print('-------------------------')
            print("Votre entrée ne correspond pas a une année")
            return
        annee_livre = collection.aggregate([
        {"$match" : {"year" : self }},{"$limit" : 5}])
        df = pd.DataFrame(annee_livre, columns = ["title", "authors", "year", "type", "_id"])
        df.insert(0,"index",range(1, len(df)+1))
        df.set_index("index", inplace=True)
        if len(df) >0 :
            print(Fore.YELLOW + Style.DIM + str(df))
        print('-------------------------')
        print("Il existe " + str(collection.count_documents({"year" : self })) + " documents publiés à cette date")
        if collection.count_documents({"year" : self }) >5 :
            i = 5
            while i < collection.count_documents({"year" : self }) :
                choix = input(Fore.BLACK + Style.DIM + Back.WHITE +"souhaitez vous voir plus de résultats : Y/N " + Style.RESET_ALL + " ")
                print('-------------------------')
                match choix:
                    case "Y":
                        index_to_start += 5 
                        annee_livre = collection.aggregate([
                        {"$match" : {"year" : self }}, {"$skip" : i}, {"$limit" : 5}])
                        df = pd.DataFrame(annee_livre, columns = ["title", "authors", "year", "type", "_id"])
                        df.insert(0,"index",range(index_to_start, len(df)+index_to_start))
                        df.set_index("index", inplace=True)
                        print(Fore.YELLOW + Style.DIM + str(df))
                        i += 5
                    case "N": 
                        break
                    case _: 
                        print('-------------------------')
                        print(Fore.RED + "mauvaise saisie")
        else :
            pass
    
    def recherche_livre_nom_auteur (self:str) :
        index_to_start = 1
        auteur_livre = collection.aggregate([
        {"$match" : {"authors" : {"$regex" : self , "$options" : "i" }}},{"$limit" : 5}])
        df = pd.DataFrame(auteur_livre, columns = ["title", "authors", "year", "type", "_id"])
        df.insert(0,"index",range(1, len(df)+1))
        df.set_index("index", inplace=True)
        if len(df) >0 :
            print(Fore.YELLOW + Style.DIM + str(df))
        print('-------------------------')
        print("Il existe " + str(collection.count_documents({"authors" : {"$regex" : self , "$options" : "i" }})) + " documents de cet auteur")
        if collection.count_documents({"authors" : {"$regex" : self , "$options" : "i" }}) > 5 :
            i = 5
            while i < collection.count_documents({"authors" : {"$regex" : self , "$options" : "i" }}) :
                print('-------------------------')
                choix = input(Fore.BLACK + Style.DIM + Back.WHITE + "souhaitez vous voir plus de résultats : Y/N " + Style.RESET_ALL + " ")
                match choix:
                    case "Y":
                        index_to_start += 5
                        auteur_livre = collection.aggregate([
                        {"$match" : {"authors" :{"$regex" : self , "$options" : "i" }}}, {"$skip" : i}, {"$limit" : 5}])
                        df = pd.DataFrame(auteur_livre, columns = ["title", "authors", "year", "type", "_id"])
                        df.insert(0,"index",range(index_to_start, len(df)+index_to_start))
                        df.set_index("index", inplace=True)
                        print(Fore.YELLOW + Style.DIM + str(df))
                        i += 5
                    case "N": 
                        break
                    case _: 
                        print('-------------------------')
                        print(Fore.RED + "mauvaise saisie")
        else : 
            pass
        print('-------------------------')
        choix_2 = input("Souhaitez ajouter un filtre en fonction du type de document ? : Y/N ")
        match choix_2:
            case "Y":
                print('-------------------------')
                choix_3 = input("Saisisser le type d'oeuvre à conserver : ")
                auteur_type_livre = collection.aggregate([
            {"$match" : {"$and" :[{"type" : choix_3 },{"authors" :{"$regex" : self , "$options" : "i" }}]}}
            ])
                df = pd.DataFrame(auteur_type_livre, columns = ["title", "authors", "year", "type", "_id"])
                df.insert(0,"index",range(index_to_start, len(df)+index_to_start))
                df.set_index("index", inplace=True)
                if len(df) >0 :
                    print(Fore.YELLOW + Style.DIM + str(df))
                print('-------------------------')
                print("Il n'existe plus que " + str(collection.count_documents({"$and" :[{"type" : choix_3 },{"authors" :{"$regex" : self , "$options" : "i" }}]}
            )) + " documents correspondant à la recherche")
            case "N":
                pass
            case _:
                print('-------------------------')
                print(Fore.RED + "mauvaise saisie")

    def suppression_livre () :
        print('-------------------------')
        livre_a_supprimer = input("Entrez l'identifiant _id du document a supprimer : ")
        print('-------------------------')
        result = collection.delete_one({"_id" : (livre_a_supprimer)})
        if result.deleted_count > 0 :
            print('-------------------------')
            print(str(result.deleted_count) + " document a bien été supprimé")
        else :
            print('-------------------------')
            print("aucun document n'a pas pu être trouvé avec cet identifiant")

    def suppression_livre_multiple() :
        print('-------------------------')
        livres_a_supprimer = input ("Entrez le nom exact de l'auteur dont vous souhaitez supprimer les ouvrages : ")
        resultat_suppr_multiple = collection.delete_many({"authors" : livres_a_supprimer})
        if resultat_suppr_multiple.deleted_count >0 :
            print('-------------------------')
            print(str(resultat_suppr_multiple.deleted_count) + " documents ont bien été supprimés")
        else :
            print('-------------------------')
            print("aucun document n'a pas pu être trouvé avec ce nom d'auteur")

    def creer_nouveau_document():
        print('-------------------------')
        type = input("Entrez le type de document à ajouter : ")
        title = input("Entrez le titre de votre document à ajouter : ")
        year = int(input("Entrez l'année de parution de votre document : "))
        _id = str(type)+str(title)+str(year)
        collection.insert_one({"type" : type,
                             "title" : title,
                             "year" : year,
                             "_id" : _id}) 
        print('-------------------------')
        print("Voici le document nouvellement créé : ")
        pprint.pprint(collection.find_one({"$and" : [{"type" : type},
                                         {"title" : title},
                                         {"year" : year}
                                         ]}))     
        

        