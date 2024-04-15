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
        The function to get the name of the node.

        Returns:
            str: The name of the node.
        """
        return self.name

    def __str__(self):
        """
        The function to get the string representation of the node.

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
        The function to get the source node of the edge.

        Returns:
            Node: The source node of the edge.
        """
        return self.src

    def get_destination(self):
        """
        The function to get the destination node of the edge.

        Returns:
            Node: The destination node of the edge.
        """
        return self.dest

    def __str__(self):
        """
        The function to get the string representation of the edge.

        Returns:
            str: The string representation of the edge in the format 'src->dest'.
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
        The constructor for Digraph class.
        """
        self.edges = {}

    def add_node(self, node):
        """
        The function to add a node to the graph.

        Parameters:
            node (Node): The node to be added.

        Raises:
            ValueError: If the node already exists in the graph.
        """
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def add_edge(self, edge):
        """
        The function to add an edge to the graph.

        Parameters:
            edge (Edge): The edge to be added.

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
        The function to get the children of a node.

        Parameters:
            node (Node): The node to get the children of.

        Returns:
            list: The list of children of the node.
        """
        return self.edges[node]

    def has_node(self, node):
        """
        The function to check if a node is in the graph.

        Parameters:
            node (Node): The node to check.

        Returns:
            bool: True if the node is in the graph, False otherwise.
        """
        return node in self.edges

    def get_node(self, name):
        """
        The function to get a node by its name.

        Parameters:
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
        The function to get the string representation of the graph.

        Returns:
            str: The string representation of the graph in the format 'src->dest'.
        """
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result += src.get_name() + '->' + dest.get_name() + '\n'
        return result[:-1]  # Omit final newline
