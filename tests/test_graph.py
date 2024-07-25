# tests/test_graph.py

import unittest
from graph import Graph
from user import User

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.user1 = User(1, "Alice")
        self.user2 = User(2, "Bob")

    def test_add_user(self):
        self.graph.add_user(self.user1)
        self.assertIn(self.user1.user_id, self.graph.adjacency_list)

    def test_add_relationship(self):
        self.graph.add_user(self.user1)
        self.graph.add_user(self.user2)
        self.graph.add_relationship(self.user1, self.user2)
        self.assertIn(self.user2.user_id, self.graph.adjacency_list[self.user1.user_id])

if __name__ == "__main__":
    unittest.main()
