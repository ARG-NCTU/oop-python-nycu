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
        # Assigning the name of the node to the instance variable 'name'
        self.name = name

    def get_name(self):
        """
        Returns the name of the node.

        Returns:
            str: The name of the node.
        """
        # Returning the name of the node
        return self.name

    def __str__(self):
        """
        Returns the string representation of the node.

        Returns:
            str: The name of the node.
        """
        # Returning the string representation of the node
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


        str
            a string representation of the graph
        """
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result += src.get_name() + '->' + dest.get_name() + '\n'
        return result[:-1]  # Omit final newline
