import tkinter as tk 
 # imported the tkinter as tk library
from graph import Graph
from user import User
 
class App:
    def __init__(self, root):
        self.graph = Graph()
        self.root = root
        self.root.title("Social Network")
 
        self.user_id_label = tk.Label(root, text="User ID")
        self.user_id_label.pack()
 
        self.user_id_entry = tk.Entry(root)
        self.user_id_entry.pack()
 
        self.name_label = tk.Label(root, text="Name")
        self.name_label.pack()
 
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
 
        self.add_user_button = tk.Button(root, text="Add User", command=self.add_user)
        self.add_user_button.pack()
 
        self.users_listbox = tk.Listbox(root)
        self.users_listbox.pack()
 
    def add_user(self):
        user_id = self.user_id_entry.get()
        name = self.name_entry.get()
         # Check if both fields are filled
        if user_id and name: 
            user = User(user_id, name)
            self.graph.add_user(user)
            self.users_listbox.insert(tk.END, f"User ID: {user_id}, Name: {name}")
            self.user_id_entry.delete(0, tk.END)  # Clear the entry after adding
            self.name_entry.delete(0, tk.END)  # Clear the entry after adding
        else:
            tk.messagebox.showwarning("Input Error", "Please enter both User ID and Name")  # Show warning if fields are empty
 
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()