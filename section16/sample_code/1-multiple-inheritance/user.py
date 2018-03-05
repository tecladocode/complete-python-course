class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        return 'Logged in!'
    
    def __repr__(self):
        return f'<User {self.username}>'