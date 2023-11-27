from pymongo import MongoClient

def connectDataBase():
    DB_HOST = 'localhost:27017'
    try:
        client = MongoClient(host=[DB_HOST])
        db = client.CSParser
        return db
    except:
        print("Database not connected")

def insertPage(col, url, html):
    col.insert_one({"url": url, "html": html})


