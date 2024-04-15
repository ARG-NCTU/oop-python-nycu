class Node:
    """
    Represents a node in a graph.

    Attributes:
        name (str): The name of the node.
    """

    def __init__(self, name):
        """
        Initializes a Node with a name.

        Args:
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
        Returns a string representation of the node.

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
        Initializes an Edge with a source and destination node.

        Args:
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
        Returns a string representation of the edge.

        Returns:
            str: A string in the format 'source->destination'.
        """
        return self.src.get_name() + '->' + self.dest.get_name()


class Digraph:
    """
    Represents a directed graph.

    Attributes:
        edges (dict): A dictionary mapping each node to a list of its children.
    """

    def __init__(self):
        """
        Initializes an empty Digraph.
        """
        self.edges = {}

    def add_node(self, node):
        """
        Adds a node to the graph.

        Args:
            node (Node): The node to be added.

        Raises:
            ValueError: If the node is already in the graph.
        """
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def add_edge(self, edge):
        """
        Adds an edge to the graph.

        Args:
            edge (Edge): The edge to be added.

        Raises:
            ValueError: If the source or destination node is not in the graph.
        """
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def children_of(self, node):
        """
        Returns the children of a node.

        Args:
            node (Node): The node to get the children of.

        Returns:
            list: The children of the node.
        """
        return self.edges[node]

    def has_node(self, node):
        """
        Checks if a node is in the graph.

        Args:
            node (Node): The node to check.

        Returns:
            bool: True if the node is in the graph, False otherwise.
        """
        return node in self.edges

    def get_node(self, name):
        """
        Returns the node with the given name.

        Args:
            name (str): The name of the node.

        Returns:
            Node: The node with the given name.

        Raises:
            NameError: If there is no node with the given name.
        """
        for n in self.edges:
            if n.get_name() == name:
                return n
        raise NameError(name)

    def __str__(self):
        """
        Returns a string representation of the graph.

        Returns:
            str: A string representation of the graph.
        """
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result += src.get_name() + '->' + dest.get_name() + '\n'
        return result[:-1]  # Omit final newline

class Graph(Digraph):
    """
    Represents a graph as a dictionary of nodes mapping.
    Inherits from the Digraph class.
    """

    def add_edge(self, edge):
        """
        Adds an edge to the graph in both directions.

        Args:
            edge (Edge): The edge to be added.
        """
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        Digraph.add_edge(self, rev)


class CityPlanner:
    """
    Represents a city planner that can find shortest paths in a graph.
    """

    def __init__(self):
        """
        Initializes a CityPlanner.
        """
        self.print_queue = True
        self.g = []

    def print_path(self, path):
        """
        Prints a path as a string.

        Args:
            path (list): The path to be printed.

        Returns:
            str: The path as a string.
        """
        result = ''
        for i in range(len(path)):
            result += str(path[i])
            if i != len(path) - 1:
                result += '->'
        return result

    def DFS(self, graph, start, end, path, shortest, to_print=False):
        """
        Performs a depth-first search to find the shortest path.

        Args:
            graph (Digraph): The graph to search.
            start (Node): The start node.
            end (Node): The end node.
            path (list): The current path.
            shortest (list): The current shortest path.
            to_print (bool, optional): Whether to print the paths. Defaults to False.

        Returns:
            list: The shortest path from start to end.
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
        Performs a breadth-first search to find the shortest path.

        Args:
            graph (Digraph): The graph to search.
            start (Node): The start node.
            end (Node): The end node.
            to_print (bool, optional): Whether to print the paths. Defaults to False.

        Returns:
            list: The shortest path from start to end.
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
        Finds the shortest path using breadth-first search.

        Args:
            graph (Digraph): The graph to search.
            start (Node): The start node.
            end (Node): The end node.
            toPrint (bool, optional): Whether to print the paths. Defaults to False.

        Returns:
            list: The shortest path from start to end.
        """
        return self.BFS(graph, start, end, toPrint)

    def shortest_path_dfs(self, graph, start, end, toPrint = False):
        """
        Finds the shortest path using depth-first search.

        Args:
            graph (Digraph): The graph to search.
            start (Node): The start node.
            end (Node): The end node.
            toPrint (bool, optional): Whether to print the paths. Defaults to False.

        Returns:
            list: The shortest path from start to end.
        """
        return self.DFS(graph, start, end, [], None, toPrint)

    def get_shortest_path(self, source, destination, method='dfs'):
        """
        Finds the shortest path between two nodes.

        Args:
            source (str): The name of the source node.
            destination (str): The name of the destination node.
            method (str, optional): The search method ('dfs' or 'bfs'). Defaults to 'dfs'.

        Prints the shortest path or a message if no path exists.
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
