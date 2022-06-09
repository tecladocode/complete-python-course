from database import Database
from admin import Admin
from user import User
from saveable import Saveable

a = Admin('rolf', '1234', 3)
u = User('jose', 'password')

a.save()
u.save()

user = Database.find(lambda x: x['username'] == 'rolf')[0]
user_obj = Admin(**user)
print(user_obj.username)

print(isinstance(user_obj, Saveable))

users_to_save = [a, u]
for u in users_to_save:
    u.save()
