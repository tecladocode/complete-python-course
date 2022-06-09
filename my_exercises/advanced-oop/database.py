class Database:
    content = {'users': []}

    @classmethod
    def insert(cls, data):
        cls.content['users'].append(data)

    @classmethod
    def remove(cls, finder): # lambda x: x['username'] != 'Rolf'
        cls.content['users'] = [user for user in cls.content['users'] if not finder(user)]

    @classmethod
    def find(cls, finder): # lambda x: x['username'] == 'Rolf'
        return [user for user in cls.content['users'] if finder(user)]




