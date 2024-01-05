# from colorama import init, Fore, Back, Style
# # essential for Windows environment
# init()
# # all available foreground colors
# FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
# # all available background colors
# BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
# # brightness values
# BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]

# def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
#     """Utility function wrapping the regular `print()` function 
#     but with colors and brightness"""
#     print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)


# # printing all available foreground colors with different brightness
# for fore in FORES:
#     for brightness in BRIGHTNESS:
#         print_with_color("Hello world!", color=fore, brightness=brightness)

# print(Fore.BLACK + Style.DIM + Back.WHITE + "Souhaitez vous.....")

# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')



# import pandas as pd 
# data = pd.read_json("C:/Users/lord_/package python mongo etc/projet python mongodb/projet mongo-python2-1-24/projet mongo-python/books.json")
# # print(data.head()) 
# print("------------")

# # print (data.shape)
# # print(data.dtypes)
# # print(data["isbn"])
# variables = ["type", "_id", "year", "authors", "title"]
# print(data[variables])
# print("------------")


# from terminaltables import AsciiTable

# table_data = [
#     ['Heading1', 'Heading2'],
#     ['row1 column1', 'row1 column2'],
#     ['row2 column1', 'row2 column2'],
#     ['row3 column1', 'row3 column2']
# ]
# table = AsciiTable(table_data)
# print(table.table)

# import pandas as pd
# from random import randint
# df = pd.DataFrame(columns=['A','B','C','D','E'])
# for i in range(5): #add 5 rows of data
#     df.loc[i, ['A']] = randint(0,99)
#     df.loc[i, ['B']] = randint(0,99)
#     df.loc[i, ['C']] = randint(0,99)
#     df.loc[i, ['D']] = randint(0,99)
#     df.loc[i, ['E']] = randint(0,99)
# print(df)
 
# from pymongo import MongoClient
# client = MongoClient()
# db = client["test"]
# collection = db["books"]
# print("-------------------")
# print("Le nombre de documents total est  : " + str(db.books.count_documents({})) )


# print("-------------------")
# print("le nombre de document par type est de : " )
# doc_par_type = (db.books.aggregate([
#     {"$group" : {"_id": "$type", "nb": {"$sum": 1}}}]))
# for i in doc_par_type :
#     print(i)

# print("-------------------")
# print("le nombre de document publié chaque année est de  : ")
# nb_doc_annee = db.books.aggregate([
#     {"$group" : {"_id" : "$year" , "nb" : {"$sum" : 1}}}])
# for i in nb_doc_annee :
#     print(i)

# from pymongo import MongoClient
# client = MongoClient()
# db = client["test"]
# collection = db["books"]
# # print("-------------------")
# # print("liste des articles triés par longueur ")
# # stats =  db.books.aggregate([{"$unwind" : "$authors"}, {"$group" : {"_id" : "$authors", "nb" :{"$sum":1}}}, {"$sort" : {"nb" : -1}}, {"$limit" : 5}])
# # for i in stats :
# #     print(i)

# liste_doc = (db.books.aggregate([{"$group" : {"_id" : "$type"}}]))
# for i in liste_doc :
#     print(i)

# from pymongo import MongoClient
# client = MongoClient()
# db = client["test"]
# collection = db["books"]

# recherche = [{"$match" : {"authors" : {"$regex" : "falcone" , "$options" : "i" }}},{"$limit" : 5}]
# print(recherche)
# search = collection.aggregate(recherche)
# for i in search :
#     print(i)

# df = pd.DataFrame(search,columns = ["title", "authors", "year", "type", "_id", ])
# df.set_index("index", inplace=True)
# print(df)

match_choix = {"type" : "type_a_rechercher" }
print(match_choix)