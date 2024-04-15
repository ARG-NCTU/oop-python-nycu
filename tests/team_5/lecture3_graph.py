class Node:
    """
    Represents a node in a graph.

    Attributes:
        name (str): The name of the node.
    """

    def __init__(self, name):
        """
        Initializes a new instance of the Node class.

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
        Initializes a new instance of the Edge class.
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
            str: A string representation of the edge in the format 'src->dest'.
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
        Initializes a new instance of the Digraph class.
        """
        self.edges = {}

    def add_node(self, node):
        """
        Adds a node to the graph.

        Args:
            node (Node): The node to add.

        Raises:
            ValueError: If the node already exists in the graph.
        """
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def add_edge(self, edge):
        """
        Adds an edge to the graph.

        Args:
            edge (Edge): The edge to add.

        Raises:
            ValueError: If the source or destination node of the edge is not in the graph.
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
        Returns a node with a specific name.

        Args:
            name (str): The name of the node.

        Returns:
            Node: The node with the specified name.

        Raises:
            NameError: If no node with the specified name exists in the graph.
        """
        for n in self.edges:
            if n.get_name() == name:
                return n
        raise NameError(name)

    def __str__(self):
        """
        Returns a string representation of the graph.

        Returns:
            str: A string representation of the graph in the format 'src->dest'.
        """
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result += src.get_name() + '->' + dest.get_name() + '\n'
        return result[:-1]  # Omit final newline


class Graph(Digraph):
    """
    Represents a graph. Inherits from the Digraph class.

    Overrides the add_edge method to make the graph undirected.
    """
    def add_edge(self, edge):
        """
        Adds an edge to the graph.

        Overrides the add_edge method of the Digraph class to make the graph undirected.
        Adds the edge in both directions.

        Args:
            edge (Edge): The edge to add.
        """
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        Digraph.add_edge(self, rev)
