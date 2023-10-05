class User:

    def __init__(self, id_num, username):
        self.id = id_num
        self.username = username
        self.followers = 0

    def change_id(self):
        new = int(input('What is the new id'))
        self.id = new
        print(self.id)


user = User('10', 'ah kok')

print(user.id)
print(user.username)
print(user.followers)

user.change_id()