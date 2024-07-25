#defining a User class that represents a user in a social network or similar application. The class includes attributes for storing user information and methods for managing friendships. The User class has an initializer that sets the user ID and name, and it maintains a list of friends. The class provides methods to add and remove friends, retrieve the list of friends, and a string representation of the user

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    def remove_friend(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)

    def get_friends(self):
        return self.friends

    def __str__(self):
        return f'User({self.user_id}, {self.name})'

    