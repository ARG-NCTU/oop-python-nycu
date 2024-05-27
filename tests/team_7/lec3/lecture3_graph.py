class Node:
    """    Represents a node in a graph.
    Each node has a name which is assumed to be a string.
    """
    def __init__(self, name):
        """
        Initializes a Node with a given name.
        :param name: The name of the node.
        """
        self.name = name

    def get_name(self):
        """
        Returns the name of the node.
        :return: The name of the node.
        """
        return self.name

    def __str__(self):
        """
        Returns a string representation of the node.
        :return: The name of the node.
        """
        return self.name


class Edge:
    """
    Represents a directed edge in a graph.
    Each edge has a source node and a destination node.
    """
    def __init__(self, src, dest):
        """
        Initializes an Edge with a source node and a destination node.
        :param src: The source node.
        :param dest: The destination node.
        """
        self.src = src
        self.dest = dest

    def get_source(self):
        """
        Returns the source node of the edge.
        :return: The source node.
        """
        return self.src

    def get_destination(self):
        """
        Returns the destination node of the edge.
        :return: The destination node.
        """
        return self.dest

    def __str__(self):
        """
        Returns a string representation of the edge.
        :return: A string in the format 'source->destination'.
        """
        return self.src.get_name() + '->' + self.dest.get_name()


class Digraph:
    """
    Represents a directed graph.
    The graph is represented as a dictionary mapping each node to a list of its children.
    """
    def __init__(self):
        """
        Initializes an empty Digraph.
        """
        self.edges = {}

    def add_node(self, node):
        """
        Adds a node to the graph.
        Raises a ValueError if the node is already in the graph.
        :param node: The node to be added.
        """
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def add_edge(self, edge):
        """
        Adds an edge to the graph.
        Raises a ValueError if the source or destination node is not in the graph.
        :param edge: The edge to be added.
        """
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def children_of(self, node):
        """
        Returns the children of a node.
        :param node: The node.
        :return: A list of the node's children.
        """
        return self.edges[node]

    def has_node(self, node):
        """
        Checks if a node is in the graph.
        :param node: The node to check.
        :return: True if the node is in the graph, False otherwise.
        """
        return node in self.edges

    def get_node(self, name):
        """
        Returns the node with the given name.
        Raises a NameError if no such node exists.
        :param name: The name of the node.
        :return: The node with the given name.
        """
        for n in self.edges:
            if n.get_name() == name:
                return n
        raise NameError(name)

    def __str__(self):
        """
        Returns a string representation of the graph.
        :return: A string representing the graph.
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
    """
    A class used to represent a City Planner

    ...

    Attributes
    ----------
    print_queue : bool
        a flag used to control the printing of the queue
    g : list
        a list to store the graph nodes

    Methods
    -------
    print_path(path)
        Prints the path from start to end node.
    DFS(graph, start, end, path, shortest, to_print=False)
        Performs Depth First Search on the graph.
    BFS(graph, start, end, to_print=False)
        Performs Breadth First Search on the graph.
    shortest_path_bfs(graph, start, end, toPrint = False)
        Finds the shortest path from start to end node using BFS.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the city planner object.

        """
        self.print_queue = True
        self.g = []

    def print_path(self, path):
        """
        Assumes path is a list of nodes
        Prints the path from start to end node.

        Parameters:
            path (list): The path to be printed.

        Returns:
            result (str): The string representation of the path.
        """
        result = ''
        for i in range(len(path)):
            result += str(path[i])
            if i != len(path) - 1:
                result += '->'
        return result

    def DFS(self, graph, start, end, path, shortest, to_print=False):
        """
        Assumes graph is a Digraph; start and end are nodes;
        path and shortest are lists of nodes
        Performs Depth First Search on the graph.

        Parameters:
            graph (Digraph): The graph to be searched.
            start (Node): The start node.
            end (Node): The end node.
            path (list): The current path.
            shortest (list): The shortest path found so far.
            to_print (bool, optional): Flag to control printing. Defaults to False.

        Returns:
            shortest (list): The shortest path from start to end in graph.
        """
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
        """
        Assumes graph is a Digraph; start and end are nodes
        Performs Breadth First Search on the graph.

        Parameters:
            graph (Digraph): The graph to be searched.
            start (Node): The start node.
            end (Node): The end node.
            to_print (bool, optional): Flag to control printing. Defaults to False.

        Returns:
            tmp_path (list): The shortest path from start to end in graph.
        """
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
        """
        Assumes graph is a Digraph; start and end are nodes
        Finds the shortest path from start to end node using BFS.

        Parameters:
            graph (Digraph): The graph to be searched.
            start (Node): The start node.
            end (Node): The end node.
            toPrint (bool, optional): Flag to control printing. Defaults to False.

        Returns:
            BFS (list): The shortest path from start to end in graph.
        """
        return self.BFS(graph, start, end, toPrint)


    def shortest_path_dfs(self, graph, start, end, toPrint = False):
        """
        Assumes graph is a Digraph; start and end are nodes
        Returns a shortest path from start to end in graph

        Parameters:
            graph (Digraph): The graph to be searched.
            start (Node): The start node.
            end (Node): The end node.
            toPrint (bool, optional): Flag to control printing. Defaults to False.

        Returns:
            DFS (list): The shortest path from start to end in graph.
        """
        return self.DFS(graph, start, end, [], None, toPrint)


    def get_shortest_path(self, source, destination, method='dfs'):
        """
        Finds the shortest path from source to destination using the specified method.

        Parameters:
            source (str): The source node.
            destination (str): The destination node.
            method (str, optional): The method to be used for finding the shortest path. Defaults to 'dfs'.

        Prints:
            The shortest path from source to destination if it exists, else prints that there is no path.
        """
        sp = self.shortest_path_dfs(self.g,
                            self.g.get_node(source),
                            self.g.get_node(destination),
                            True)
        if sp is not None:
            print('Shortest path from', source, 'to',
                destination, 'is', self.print_path(sp))
        else:
            print('There is no path from', source, 'to', destination)
