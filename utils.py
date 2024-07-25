# utils.py

from collections import deque

# Breadth-First Search (BFS) Algorithm 
def bfs(graph, start_user_id):
    visited = set() # Set to keep track of visited nodes
    queue = deque([start_user_id]) # Queue For BFS

    while queue:
        user_id = queue.popleft()
        if user_id not in visited:
            visited.add(user_id)
            queue.extend(set(graph.adjacency_list[user_id]) - visited)

    return visited

def dfs(graph, start_user_id):
    visited = set()
    stack = [start_user_id]

    while stack:
        user_id = stack.pop()
        if user_id not in visited:
            visited.add(user_id)
            stack.extend(set(graph.adjacency_list[user_id]) - visited)

    return visited
# utils.py

import heapq

def dijkstra(graph, start_user_id, end_user_id):
    distances = {user_id: float('infinity') for user_id in graph.adjacency_list}
    distances[start_user_id] = 0
    priority_queue = [(0, start_user_id)]

    while priority_queue:
        current_distance, current_user_id = heapq.heappop(priority_queue)

        if current_distance > distances[current_user_id]:
            continue

        for neighbor in graph.adjacency_list[current_user_id]:
            distance = current_distance + 1  # assuming equal weights for simplicity
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[end_user_id]

# utils.py

def connected_components(graph):
    visited = set()
    components = []

    for user_id in graph.adjacency_list:
        if user_id not in visited:
            component = bfs(graph, user_id)
            components.append(component)
            visited.update(component)

    return components

# utils.py

def merge_sort(users, key=lambda user: user.name):
    if len(users) <= 1:
        return users
    mid = len(users) // 2
    left = merge_sort(users[:mid], key)
    right = merge_sort(users[mid:], key)

    return merge(left, right, key)

def merge(left, right, key):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


# utils.py

def binary_search(users, target, key=lambda user: user.user_id):
    left, right = 0, len(users) - 1
    while left <= right:
        mid = (left + right) // 2
        if key(users[mid]) == target:
            return users[mid]
        elif key(users[mid]) < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


# utils.py

def average_friends(graph):
    total_friends = sum(len(friends) for friends in graph.adjacency_list.values())
    return total_friends / len(graph.adjacency_list)

def network_density(graph):
    total_users = len(graph.adjacency_list)
    total_relationships = sum(len(friends) for friends in graph.adjacency_list.values()) / 2
    return total_relationships / (total_users * (total_users - 1) / 2)


# utils.py

def recommend_friends(graph, user):
    recommendations = set()
    for friend in graph.adjacency_list[user.user_id]:
        for friend_of_friend in graph.adjacency_list[friend]:
            if friend_of_friend != user.user_id and friend_of_friend not in graph.adjacency_list[user.user_id]:
                recommendations.add(friend_of_friend)
    return recommendations
