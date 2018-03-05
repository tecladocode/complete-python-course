from database import Database
from admin import Admin

a = Admin('paco', 'perez', 2)
b = Admin('rolf', 'smith', 1)

a.save()
b.save()

user = Database.find(lambda x: x['username'] == 'paco')[0]
user_obj = Admin(**user)
print(user_obj.username)