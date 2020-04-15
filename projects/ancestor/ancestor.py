"""
inputs : vertex or starting point, a list containing key value pairs
output : earliest ancestor or destination vertex

 * key value pairs need to be constructed in a graph --> use graph class from previous assignment to complete

 * perform a dft to traverse the graph until it reaches a vertex without any neighbors

 * edges only point downward

 * create a method that gets the vertices that point to the current node

 * store a node's parents in a set to get the lowest value if more than one earliest ancestor exist




"""
from util import Stack


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}  # adjaceny list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # add the edge
            self.vertices[v1].add(v2)
        else:
            print("Error adding edge: vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        #
        if vertex_id in self.vertices:
            #
            return self.vertices[vertex_id]
        else:
            return None

    def get_parents(self, vertex):
        # create empty set
        parents = set()
        # for each key in vertices:
        for key in self.vertices:
            # if vertex is in value:
            if vertex in self.vertices[key]:
                # add to set
                parents.add(key)
        if parents:
            return parents
        else:
            return None


def create_graph(ancestors):
    # construct a new graph using class from previous assignment with an additional method: get parents
    graph = Graph()

    # for each pair in ancestors:
    for ancestor in ancestors:
        # check if key is in vertices
        if ancestor[0] not in graph.vertices:
            graph.add_vertex(ancestor[0])
        # check if value is in vertices
        if ancestor[1] not in graph.vertices:
            graph.add_vertex(ancestor[1])

        # create a new edge using the key value pair
        graph.add_edge(ancestor[0], ancestor[1])

    return graph


def earliest_ancestor(ancestors, starting_node):
    # create a graph from list of ancestors
    graph = create_graph(ancestors)

    # check if starting node has ancestors
    if graph.get_parents(starting_node) is None:
        return -1

    # create a stack
    searching = Stack()

    # add starting node to stack
    searching.push(starting_node)

    # create a set to keep track of visited nodes
    visited = []

    # keep track of parents b/c a node can have two parents
    parents_list = []

    # complete a dft

    # while stack is not empty:
    while searching.size() > 0:
        # current = last item in stack
        current_node = searching.pop()
        # if current is not in visited:
        if current_node not in visited:
            # add current to visited
            visited.append(current_node)
            # if there are any parents:
            if graph.get_parents(current_node):
                # create a set to store current node's parents
                parents = set()
                # for each parent:
                for parent in graph.get_parents(current_node):
                    # add parent to stack
                    searching.push(parent)
                    # add parent to parents set
                    parents.add(parent)
                # add parents to parents list
                parents_list.append(parents)

    # return the smallest value of the earliest ancestors
    return min(parents_list[-1])
