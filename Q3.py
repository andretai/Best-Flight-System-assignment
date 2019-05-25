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
cities = ["KUL", "ICN", "ITM", "MEL", "SHA", "CGK", "SIN", "JFK", "MAN", "MAD"]
cityGraph = Graph([
    (cities[0], cities[1],4601), (cities[0], cities[2],4974), (cities[0], cities[3],6305), (cities[0], cities[4],3786),
    (cities[0], cities[5],1125), (cities[0], cities[6],297), (cities[0], cities[7],15177), (cities[0], cities[8],10686),
    (cities[0], cities[9],4601), (cities[4], cities[1],820), (cities[4], cities[9],10290), (cities[4], cities[8],9206),
    (cities[1], cities[2],862), (cities[3], cities[5],5204), (cities[5], cities[6],879), (cities[9], cities[4],10290),
    (cities[9], cities[7],5774), (cities[8], cities[4],9206), (cities[8], cities[7],5375)

])

print(cityGraph.dijkstra("KUL", "JFK"))