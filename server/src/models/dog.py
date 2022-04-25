from flask import g
from db import Db

class Dog():
    dog_list = [
        {'id': 1, 'name': 'Bo'},
        {'id': 2, 'name': 'Blackie'}
    ]

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
        db.connect()
        for dog in clean_dogs:
            sql = "INSERT INTO dogs(name) VALUES(%s)"
            print(sql)
            db.query(sql, dog['name'])
            self.dog_list.append(dog)
        return dogs

    def get(self, filters=None):
        dogs = self.dog_list
        if filters is not None:
            if 'id' in filters:
                dogs = None
                for item in self.dog_list:
                    if int(item['id']) == int(filters['id']):
                        dogs = item
                        break
            # if another filter
        return dogs

    def put(self, dogs):
        if not isinstance(dogs, (list, tuple)):
            dogs = [dogs]
        clean_dogs = self.sanitize(dogs)
        if len(dogs) != len(clean_dogs):
            return False
        for dog in clean_dogs:
            for index, item in enumerate(self.dog_list):
                if int(item['id']) == int(dog['id']):
                    self.dog_list[index]['name'] = dog['name']
                    break
        return dogs

    def delete(self, dogs):
        counter = 0
        if not isinstance(dogs, (list, tuple)):
            dogs = [dogs]
        for dog in dogs:
            for index, item in enumerate(self.dog_list):
                if int(item['id']) == int(dog):
                    del self.dog_list[index]
                    counter += 1
                    break
        return counter
