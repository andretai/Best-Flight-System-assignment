from collections import deque, namedtuple


# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path

#Sample alph graph
alph = ["a", "b", "c", "d", "e", "f"]
graph = Graph([
    (alph[0], alph[1], 7),  (alph[0], alph[2], 9),  (alph[0], alph[5], 14), (alph[1], alph[2], 10),
    (alph[1], alph[3], 15), (alph[2], alph[3], 11), (alph[2], alph[5], 2),  (alph[3], alph[4], 6),
    (alph[4], alph[5], 9)])

print(graph.dijkstra("a", "e"))

#Distance between cities graph
cities = ["KUL", "ICN", "ITM", "MEL", "SVO", "PEK", "CGK", "SIN", "JFK", "MAN", "MAD"]
cityGraph = Graph([
    (cities[0], cities[10],11098), (cities[0], cities[5],3200), (cities[0], cities[1],4601), (cities[0], cities[2],4975),
    (cities[0], cities[6],1125), (cities[0], cities[7],297), (cities[10], cities[5],9227), (cities[10], cities[4],3444),
    (cities[10], cities[9],1432), (cities[10], cities[8],5775), (cities[5], cities[4],5000), (cities[5], cities[9],8115), (cities[5], cities[1],903),
    (cities[1], cities[4],6598), (cities[1], cities[2],862), (cities[2], cities[4],7344), (cities[6], cities[3],5204),
    (cities[6], cities[7],9879), (cities[4], cities[9],2585), (cities[9], cities[8],5376)
])

print(cityGraph.dijkstra("KUL", "MAD"))


# (cities[0], cities[1],4601), (cities[0], cities[2],4975), (cities[0], cities[3],6305), (cities[0], cities[4],8129),
#     (cities[0], cities[5],4399), (cities[0], cities[6],1125), (cities[0], cities[7],297), (cities[0], cities[8],15178),
#     (cities[0], cities[9],10687), (cities[0], cities[10],11098), (cities[1], cities[2],862), (cities[1], cities[4],6598), (cities[1], cities[5],903),
#     (cities[2], cities[4],7344), (cities[3], cities[6],5204), (cities[3], cities[7],6024), (cities[4], cities[5],5801),
#     (cities[4], cities[9],2585), (cities[4], cities[8],7566), (cities[4], cities[10],3444),(cities[5], cities[10],9227),
#     (cities[6], cities[7],879), (cities[8], cities[9],5376), (cities[8], cities[10],5775),
#     (cities[9], cities[10],1432)
