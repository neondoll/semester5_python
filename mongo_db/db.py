from pymongo import MongoClient
from mongo_db.env import DB_HOST, DB_PORT


class DB(object):
    def __init__(self, schema):
        # Создание клиента
        self.client = MongoClient(DB_HOST, DB_PORT)
        # Соединение с базой данных
        self.db = self.client[schema]

    def insert(self, collection, data):
        """ Функция для вставки данных в коллекцию и возврата идентификатора данных. """
        return self.db[collection].insert_one(data).inserted_id

    def select(self, collection, elements, multiple=False):
        """ Функция для получения одной или нескольких записей из базы данных. """
        if multiple:
            results = self.db[collection].find(elements)
            return [r for r in results]
        else:
            return self.db[collection].find_one(elements)

    def update(self, collection, query_elements, new_values):
        """ Функция для обновления записей в коллекции. """
        self.db[collection].update(query_elements, {'$set': new_values})

    def delete(self, collection, query):
        """ Функция для удаления записей из коллекции """
        self.db[collection].delete_many(query)
