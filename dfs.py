from typing import List, Dict, Set

class Graph:
    def __init__(self):
        self.adjacency_list: Dict[int, List[int]] = {}

    def add_edge(self, start: int, end: int) -> None:
        if start not in self.adjacency_list:
            self.adjacency_list[start] = []
        if end not in self.adjacency_list:
            self.adjacency_list[end] = []
        self.adjacency_list[start].append(end)

    def dfs(self, start: int) -> List[int]:
        visited: Set[int] = set()
        traversal_order: List[int] = []

        def dfs_visit(node: int) -> None:
            if node not in visited:
                print(f"Visiting node: {node}")
                visited.add(node)
                traversal_order.append(node)
                for neighbor in self.adjacency_list[node]:
                    dfs_visit(neighbor)

        print(f"Initiating DFS from node: {start}")
        dfs_visit(start)
        print(f"DFS complete. Order of nodes visited: {traversal_order}")
        return traversal_order

# Example usage
if __name__ == "__main__":
    graph = Graph()
    edges = [
        (0, 1), (0, 2), (1, 3), (1, 4),
        (2, 5), (2, 6), (3, 7), (4, 8)
    ]

    for start, end in edges:
        graph.add_edge(start, end)

    # Perform DFS starting from node 0
    traversal_result = graph.dfs(0)
