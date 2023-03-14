from collections import defaultdict, namedtuple
from pprint import pprint

Edge = namedtuple('Edge', ['end', 'weight'])
adj_list = defaultdict(set)
adj_list[1].add(Edge(4, weight=3))
adj_list[2].add(Edge(1, weight=1))
adj_list[2].add(Edge(4, weight=5))
adj_list[3].add(Edge(2, weight=11))
adj_list[3].add(Edge(4, weight=9))
pprint(adj_list)


# adjacency matrix
num_vertices = 5
adj_matrix = [[-1] * num_vertices for _ in range(num_vertices)]
adj_matrix[1][4] = 3
adj_matrix[2][1] = 1
adj_matrix[2][4] = 5
adj_matrix[3][2] = 11
adj_matrix[3][4] = 9
pprint(adj_matrix)