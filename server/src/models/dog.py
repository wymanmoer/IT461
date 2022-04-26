from flask import g
from db import Db

class Dog():
    def sanitize(self, dogs):
        if not isinstance(dogs, (list, tuple)):
            dogs = [dogs]
        clean_dogs = []
        for dog in dogs:
            if not isinstance(dog, dict):
                continue
            if not ('id' in dog and 'name' in dog):
                continue
            clean_dogs.append(dog)
        return clean_dogs

    def post(self, dogs):
        if not isinstance(dogs, (list, tuple)):
            dogs = [dogs]
        clean_dogs = self.sanitize(dogs)
        if len(dogs) != len(clean_dogs):
            return False
        db = Db()
        connection = db.connect()
        try:
            for dog in clean_dogs:
                sql = "INSERT INTO dogs(name) VALUES(%s)"
                db.execute(sql, dog['name'])
        except:
            connection.rollback()
        else:
            connection.commit()
        connection.close()
        return dogs

    def get(self, filters=None):
        db = Db()
        connection = db.connect()
        if filters is not None:
            if 'id' in filters:
                sql = "SELECT * FROM dogs WHERE id = %s"
                dog = db.fetchone(sql, filters['id'])
                connection.close()
                return dog
            # if another filter
        sql = "SELECT * FROM dogs ORDER BY name"
        dogs = db.fetchall(sql)
        connection.close()
        return dogs

    def put(self, dogs):
        if not isinstance(dogs, (list, tuple)):
            dogs = [dogs]
        clean_dogs = self.sanitize(dogs)
        if len(dogs) != len(clean_dogs):
            return False
        db = Db()
        connection = db.connect()
        try:
            for dog in clean_dogs:
                sql = "UPDATE dogs SET name = %s WHERE id = %s"
                db.execute(sql, (dog['name'], dog['id']))
        except:
            connection.rollback()
        else:
            connection.commit()
        connection.close()
        return dogs

    def delete(self, dogs):
        counter = 0
        if not isinstance(dogs, (list, tuple)):
            dogs = [dogs]
        db = Db()
        connection = db.connect()
        try:
            placeholder = []
            for dog in dogs:
                placeholder.append('%s')
            sql = "DELETE FROM dogs WHERE id IN (" + ", ".join(placeholder) + ")"
            counter = db.execute(sql, dogs)
        except:
            connection.rollback()
        else:
            connection.commit()
        connection.close()
        return counter
