import heapq

def a_star_search(graph, start, goal, heuristics):
    frontier = [(0 + heuristics[start], start, [start], 0)]
    visited = set()

    while frontier:
        _, current, path, current_cost = heapq.heappop(frontier)

        if current == goal:
            return path, current_cost

        if current not in visited:
            visited.add(current)
            
            for neighbor, weight in graph.get(current, {}).items():
                if neighbor not in visited:
                    new_cost = current_cost + weight
                    f_score = new_cost + heuristics.get(neighbor, 0)
                    heapq.heappush(frontier, (f_score, neighbor, path + [neighbor], new_cost))
    return None

graph_data = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}
h_values = {'A': 3, 'B': 2, 'C': 1, 'D': 0}

path, cost = a_star_search(graph_data, 'A', 'D', h_values)
print(f"Optimal Path: {path} with total cost: {cost}")
