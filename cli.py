from graph import Graph
from user import User
# Add functionality to create users and relationships
def display_menu():
    print("1. Add User")
    print("2. Remove User")
    print("3. Add Friendship")
    print("4. Remove Friendship")
    print("5. Display Users")
    print("6. Display Friends")
    print("7. Exit")

def main():
    graph = Graph()
    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == '1':
            user_id = input("Enter user ID: ")
            name = input("Enter name: ")
            user = User(user_id, name)
            graph.add_user(user)
        elif choice == '2':
            user_id = input("Enter user ID: ")
            user = User(user_id, "")
            graph.remove_user(user)
        elif choice == '3':
            user_id1 = input("Enter user 1 ID: ")
            user_id2 = input("Enter user 2 ID: ")
            user1 = User(user_id1, "")
            user2 = User(user_id2, "")
            graph.add_relationship(user1, user2)
        elif choice == '4':
            user_id1 = input("Enter user 1 ID: ")
            user_id2 = input("Enter user 2 ID: ")
            user1 = User(user_id1, "")
            user2 = User(user_id2, "")
            graph.remove_relationship(user1, user2)
        elif choice == '5':
            for user in graph.adjacency_list.keys():
                print(f"User ID: {user}")
        elif choice == '6':
            user_id = input("Enter user ID: ")
            if user_id in graph.adjacency_list:
                print(f"Friends of {user_id}: {graph.adjacency_list[user_id]}")
            else:
                print("User not found.")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
