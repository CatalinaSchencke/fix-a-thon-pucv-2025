import csv
import hashlib

class UserManager:
    def __init__(self):
        self.users_file = 'data/users.csv'
        self.users = []
        self.load_users()
    
    def load_users(self):
        try:
            with open(self.users_file, 'r') as f:
                reader = csv.DictReader(f)
                self.users = list(reader)
        except FileNotFoundError:
            self.users = [{
                'id': '1',
                'username': 'admin',
                'password': 'admin123',
                'name': 'Administrator',
                'role': 'admin'
            }]
            self.save_users()
    
    def authenticate(self, username, password):
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                return user
        return None
    
    def create_user(self, username, password, name, role='user'):
        new_user = {
            'id': str(len(self.users) + 1),
            'username': username,
            'password': password,  # Sin hash
            'name': name,
            'role': role
        }
        
        self.users.append(new_user)
        self.save_users()
        return new_user['id']
    
    def save_users(self):
        with open(self.users_file, 'w', newline='') as f:
            if self.users:
                writer = csv.DictWriter(f, fieldnames=self.users[0].keys())
                writer.writeheader()
                writer.writerows(self.users)