class Node:
    """
    Represents a node in a graph.

    Attributes:
        name (str): The name of the node.
    """

    def __init__(self, name):
        """
        The constructor for Node class.

        Parameters:
            name (str): The name of the node.
        """
        self.name = name

    def get_name(self):
        """
        Returns the name of the node.

        Returns:
            str: The name of the node.
        """
        return self.name

    def __str__(self):
        """
        Returns the string representation of the node.

        Returns:
            str: The name of the node.
        """
        return self.name


class Edge:
    """
    Represents a directed edge in a graph.

    Attributes:
        src (Node): The source node of the edge.
        dest (Node): The destination node of the edge.
    """

    def __init__(self, src, dest):
        """
        The constructor for Edge class.

        Parameters:
            src (Node): The source node of the edge.
            dest (Node): The destination node of the edge.
        """
        self.src = src
        self.dest = dest

    def get_source(self):
        """
        Returns the source node of the edge.

        Returns:
            Node: The source node of the edge.
        """
        return self.src

    def get_destination(self):
        """
        Returns the destination node of the edge.

        Returns:
            Node: The destination node of the edge.
        """
        return self.dest

    def __str__(self):
        """
        Returns the string representation of the edge.

        Returns:
            str: The string representation of the edge in the format 'src->dest'.
        """
        return self.src.get_name() + '->' + self.dest.get_name()


class Digraph:
    """
    A class to represent a directed graph.

    ...

    Attributes
    ----------
    edges : dict
        a dictionary mapping each node to a list of its children

    Methods
    -------
    add_node(node):
        Adds a node to the graph.
    add_edge(edge):
        Adds an edge to the graph.
    children_of(node):
        Returns the children of a node.
    has_node(node):
        Checks if a node is in the graph.
    get_node(name):
        Returns a node with the given name.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the digraph object.

        ...

        Attributes
        ----------
        edges : dict
            an empty dictionary to store the nodes and their children
        """
        self.edges = {}

    def add_node(self, node):
        """
        Adds a node to the graph.

        ...

        Parameters
        ----------
        node : Node
            a node to be added to the graph

        Raises
        ------
        ValueError
            if the node is already in the graph
        """
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def add_edge(self, edge):
        """
        Adds an edge to the graph.

        ...

        Parameters
        ----------
        edge : Edge
            an edge to be added to the graph

        Raises
        ------
        ValueError
            if the source or destination node is not in the graph
        """
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def children_of(self, node):
        """
        Returns the children of a node.

        ...

        Parameters
        ----------
        node : Node
            a node in the graph

        Returns
        -------
        list
            a list of the node's children
        """
        return self.edges[node]

    def has_node(self, node):
        """
        Checks if a node is in the graph.

        ...

        Parameters
        ----------
        node : Node
            a node to check

        Returns
        -------
        bool
            True if the node is in the graph, False otherwise
        """
        return node in self.edges

    def get_node(self, name):
        """
        Returns a node with the given name.

        ...

        Parameters
        ----------
        name : str
            a name to search for

        Returns
        -------
        Node
            a node with the given name

        Raises
        ------
        NameError
            if a node with the given name does not exist
        """
        for n in self.edges:
            if n.get_name() == name:
                return n
        raise NameError(name)

    def __str__(self):
        """
        Returns a string representation of the graph.

        ...

        Returns
        -------
        str
            a string representation of the graph
        """
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result += src.get_name() + '->' + dest.get_name() + '\n'
        return result[:-1]  # Omit final newline


class Graph(Digraph):
    """
    A class to represent a graph. Inherits from the Digraph class.

    ...

    Methods
    -------
    add_edge(edge):
        Adds an edge to the graph in both directions.
    """

    def add_edge(self, edge):
        """
        Adds an edge to the graph in both directions.

        ...

        Parameters
        ----------
        edge : Edge
            an edge to be added to the graph
        """
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        Digraph.add_edge(self, rev)

class CityPlanner():

    def __init__(self):
        self.print_queue = True
        self.g = []

    def print_path(self, path):
        """Assumes path is a list of nodes"""
        result = ''
        for i in range(len(path)):
            result += str(path[i])
            if i != len(path) - 1:
                result += '->'
        return result

    def DFS(self, graph, start, end, path, shortest, to_print=False):
        """Assumes graph is a Digraph; start and end are nodes;
           path and shortest are lists of nodes
           Returns a shortest path from start to end in graph"""
        path = path + [start]
        if to_print:
            print('Current DFS path:', self.print_path(path))
        if start == end:
            return path
        for node in graph.children_of(start):
            if node not in path:  # avoid cycles
                if shortest is None or len(path) < len(shortest):
                    new_path = self.DFS(graph, node, end, path, shortest,
                                    to_print)
                    if new_path is not None:
                        shortest = new_path
            elif to_print:
                print('Already visited', node)
        return shortest

    def BFS(self, graph, start, end, to_print=False):
        """Assumes graph is a Digraph; start and end are nodes
           Returns a shortest path from start to end in graph"""
        init_path = [start]
        path_queue = [init_path]
        while len(path_queue) != 0:
            # Get and remove oldest element in path_queue
            if to_print:
                print('Queue:', len(path_queue))
                for p in path_queue:
                    print(print_path(p))
            tmp_path = path_queue.pop(0)
            if to_print:
                print('Current BFS path:', self.print_path(tmp_path))
                print()
            last_node = tmp_path[-1]
            if last_node == end:
                return tmp_path
            for next_node in graph.children_of(last_node):
                if next_node not in tmp_path:
                    new_path = tmp_path + [next_node]
                    path_queue.append(new_path)
        return None

    def shortest_path_bfs(self, graph, start, end, toPrint = False):
        """Assumes graph is a Digraph; start and end are nodes
           Returns a shortest path from start to end in graph"""
        return self.BFS(graph, start, end, toPrint)


    def shortest_path_dfs(self, graph, start, end, toPrint = False):
        """Assumes graph is a Digraph; start and end are nodes
           Returns a shortest path from start to end in graph"""
        return self.DFS(graph, start, end, [], None, toPrint)


    def get_shortest_path(self, source, destination, method='dfs'):
        sp = self.shortest_path_dfs(self.g,
                           self.g.get_node(source),
                           self.g.get_node(destination),
                           True)
        if sp is not None:
            print('Shortest path from', source, 'to',
                  destination, 'is', self.print_path(sp))
        else:
            print('There is no path from', source, 'to', destination)

