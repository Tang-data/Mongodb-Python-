from pymongo import MongoClient
client = MongoClient()
db = client["test"]
collection = db["books"]

class Statistics(object) :
    def affichage_stats_db() :
        print("Le nombre de documents total est  : " + str(collection.count_documents({})) )
        
        print("-------------------")
        print("le nombre de document par type est de : " )
        doc_par_type = (collection.aggregate([
            {"$group" : {"_id": "$type", "nb": {"$sum": 1}}}]))
        for i in doc_par_type :
            print(i)

        print("-------------------")
        print("le nombre de document publié chaque année est de  : ")
        nb_doc_annee = collection.aggregate([
            {"$group" : {"_id" : "$year" , "nb" : {"$sum" : 1}}}, {"$sort" : {"nb" : 1}}])
        for i in nb_doc_annee :
            print(i)

        print("-------------------")
        print("liste des 5 auteurs les plus prolifiques ")
        stats =  collection.aggregate([{"$unwind" : "$authors"}, {"$group" : {"_id" : "$authors", "nb" :{"$sum":1}}}, {"$sort" : {"nb" : -1}}, {"$limit" : 5}])
        for i in stats :
            print(i)

        print("-------------------")
        print("Nombre de publications par année et par type ")
        avg_publication_year = collection.aggregate([{'$group': {"_id": {"type" : "$type" , "year" : "$year"}, "nb" : {"$sum" : 1 } }}, {"$sort" : { "_id" : 1 }}])  
        for i in avg_publication_year :
            print(i)