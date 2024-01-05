import pandas as pd
from pymongo import MongoClient
from colorama import Fore, Back, Style
from colorama import init
# from enum import Enum
init(autoreset=True)
client = MongoClient()
db = client["test"]
collection = db["books"]
choix_recherche = 0

# type_recherche = Enum("Type recherche",["TYPE","TITLE","YEAR","AUTHORS"])

def recherche_livre (type_a_rechercher, choix) :

    if choix == "1" :
        match_choix = {"type" : type_a_rechercher }
        pagination = {"$sort" : {"year" : 1}}
        limite = {"$limit" : 5}
        match = [{"$match" : match_choix},pagination, limite]
    elif choix == "2" :
        match_choix = {"title" :{"$regex" : type_a_rechercher , "$options" : "i" }}
        match = [{"$match" : match_choix}, {"$limit" : 5}]
    elif choix == "3" :
        match_choix = {"year" : int(type_a_rechercher) }
        match = [{"$match" : match_choix},{"$limit" : 5}]
    elif choix == "4" :
        match_choix = {"authors" : {"$regex" : type_a_rechercher , "$options" : "i" }}
        match = [{"$match" : match_choix},{"$limit" : 5}]
    else :
        pass
    search = collection.aggregate(match)
    df = pd.DataFrame(search , columns = ["title", "authors", "year", "type", "_id"])
    df.insert(0,"index",range(1, len(df)+1))
    df.set_index("index", inplace=True)
    index_to_start = 1
    nb_doc_trouves = collection.count_documents(match_choix)
    if  nb_doc_trouves > 0 :
        print(Fore.YELLOW + Style.DIM + str(df))
        print('-------------------------')
        print("Il existe " + str(nb_doc_trouves) + " documents correspondant à votre recherche")
    if  nb_doc_trouves == 0 :
        print("Il n'existe pas de document correpondant à votre recherche")
    if  nb_doc_trouves > 5 :
        i = 5
        while i <  nb_doc_trouves :
            print('-------------------------')
            choix = input(Fore.BLACK + Style.DIM + Back.WHITE +"souhaitez vous voir plus de résultats : Y/N " + Style.RESET_ALL + " ")
            match choix:
                case "Y": 
                    index_to_start += 5
                    search = collection.aggregate(match)
                    i += 5
                    df = pd.DataFrame(search,columns = ["title", "authors", "year", "type", "_id"])
                    df.insert(0,"index",range(index_to_start, index_to_start+5))
                    df.set_index("index", inplace=True)
                    print(Fore.YELLOW + Style.DIM + str(df))
                case "N": 
                    break
                case _: 
                    print('-------------------------')
                    print(Fore.RED + "mauvaise saisie")
    else : 
        pass