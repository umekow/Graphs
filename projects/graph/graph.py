"""
Simple graph implementation
"""
# from util import Stack, Queue  # These may come in handy

from util import Stack, Queue

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {} #adjaceny list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        #check if they exist
        if v1 in self.vertices and v2 in self.vertices: 
                #add the edge
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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # create a queue
        searching = Queue()

        # add first vertex to queue
        searching.enqueue([starting_vertex])

        # Create a set of traversed vertices
        visited = set()

        # While queue is not empty:
        while searching.size() > 0:

            # dequeue/pop the first vertex
            current = searching.dequeue()

            # if not visited
            if current[-1] not in visited:

                # DO THE THING!!!!!!!
                print(current[-1])
                # mark as visited
                visited.add(current[-1])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(current[-1]):
                    new_path = list(current)
                    new_path.append(next_vert)
                    searching.enqueue(new_path)
            
            
            


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack to store current
        searching = Stack()
        #push starting vertex to stack 
        searching.push(starting_vertex)
        # create a set for visited items; used a set because the big o of using the in keyword is better for sets 
        visited = set()
        # while stack is not empty: 
        while searching.size() > 0: 
            # get last item on stack 
            current_vertex = searching.pop()
            #if item is not in visited items: 
            if current_vertex not in visited: 
                # add item to visited items 
                visited.add(current_vertex)
                # print current 
                print(current_vertex)
                #for each neighbor of current_vertex: 
                for neighbor in self.get_neighbors(current_vertex): 
                    # add neighbor to stack
                    searching.push(neighbor)     



    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first orde
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if visited is None: 
            visited = set()
        
        visited.add(starting_vertex)
        print(starting_vertex)

        for neighbor in self.vertices[starting_vertex]: 

            if neighbor not in visited: 
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #create a new queue
        searching = Queue()
        #add starting vertex to queue
        searching.enqueue([starting_vertex])
        #create a stack for visited vertices
        visited = []
        # while queue is not empty: 
        while searching.size() > 0:
            # current equals to first vertex in queue
            current = searching.dequeue()
            # if current is not in visited or it equals to destination 
            if current[-1] not in visited or current[-1] != destination_vertex:  
                visited.append(current[-1])
                # for each neighbor: 
                for i in self.get_neighbors(current[-1]): 
                    # check if destination is in self.neighbors
                    if destination_vertex in self.get_neighbors(i): 
                        # found destination vertex
                        # add neighbor to visited
                        visited.append(i)
                        # add destination vertex to visited 
                        visited.append(destination_vertex)
                        # return path 
                        return visited
                    else: 
                        # create a new list 
                        new_list = list()
                        # add neighbor to new list
                        new_list.append(i)
                        # add new list 
                        searching.enqueue(new_list)
           
                   
        return None


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a stack 
        searching = Stack()
        # add starting vertex to stack 
        searching.push(starting_vertex)
        # create a set to store visited vertices
        visited = []
        #while stack is not empty: 
        while searching.size() > 0: 
            #remove last item from stack and store it in variable 
            current_vertex = searching.pop()
            #if current item is not in visited: 
            if current_vertex not in visited:
                #add current vertex to visited  
                visited.append(current_vertex)
                #if current is the destination vertex, return: 
                if current_vertex == destination_vertex: 
                    return visited
                #for each neighbor: 
                for neighbor in self.get_neighbors(current_vertex): 
                    #add neighbor to stack 
                    searching.push(neighbor)

        #return none if destination vertex is not found
        return None
              
        

    def dfs_recursive(self, start_vert, target_value, visited = None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(start_vert)
        path = path + [start_vert]
        if start_vert == target_value:
            return path
        for child_vert in self.get_neighbors(start_vert):
            if child_vert not in visited:
                new_path = self.dfs_recursive(child_vert, target_value, visited, path)
                if new_path:
                    return new_path
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    # '''
    # Should print:
    #     {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    # '''
    # print(graph.vertices)

    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    # graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
