class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    # Add method to add users in the graph class 
    def add_user(self, user): 
        if user.user_id not in self.adjacency_list:
            self.adjacency_list[user.user_id] = []

    # Add method to remove users from the network
    def remove_user(self, user):
        if user.user_id in self.adjacency_list:
            del self.adjacency_list[user.user_id]
            for user_list in self.adjacency_list.values():
                if user.user_id in user_list:
                    user_list.remove(user.user_id)

    # Implement method to add relationships between users
    def add_relationship(self, user1, user2):
        if user1.user_id in self.adjacency_list and user2.user_id in self.adjacency_list:
            self.adjacency_list[user1.user_id].append(user2.user_id)
            self.adjacency_list[user2.user_id].append(user1.user_id)

    # Implement method to remove relationships between users
    def remove_relationship(self, user1, user2):
        if user1.user_id in self.adjacency_list and user2.user_id in self.adjacency_list:
            self.adjacency_list[user1.user_id].remove(user2.user_id)
            self.adjacency_list[user2.user_id].remove(user1.user_id)
