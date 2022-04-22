dog_list = [
    {'id': 1, 'name': 'Bo'},
    {'id': 2, 'name': 'Blackie'}
]

def sanitize(dogs):
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

def post(dogs):
    if not isinstance(dogs, (list, tuple)):
        dogs = [dogs]
    clean_dogs = sanitize(dogs)
    if len(dogs) != len(clean_dogs):
        return {
            "error": "There are items in your request that are invalid"
        }
    for dog in clean_dogs:
        dog_list.append(dog)
    return dogs

def get(filters=None):
    dogs = dog_list
    if filters is not None:
        if 'id' in filters:
            dogs = None
            for item in dog_list:
                if int(item['id']) == int(filters['id']):
                    dogs = item
                    break
        # if another filter
    return dogs

def put(dogs):
    if not isinstance(dogs, (list, tuple)):
        dogs = [dogs]
    clean_dogs = sanitize(dogs)
    if len(dogs) != len(clean_dogs):
        return {
            "error": "There are items in your request that are invalid" +
            str(len(dogs)) + " " + str(len(clean_dogs))
        }
    for dog in clean_dogs:
        for index, item in enumerate(dog_list):
            if int(item['id']) == int(dog['id']):
                dog_list[index]['name'] = dog['name']
                break
    return dogs

def delete(dogs):
    counter = 0
    if not isinstance(dogs, (list, tuple)):
        dogs = [dogs]
    for dog in dogs:
        for index, item in enumerate(dog_list):
            if int(item['id']) == int(dog):
                del dog_list[index]
                counter += 1
                break
    return counter
