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

class CityPlanner:
    
    def __init__(self):
        self.g = Digraph()
    def get_shortest_path(self, start, end):
        # Check if start and end cities are in the graph
        if not (self.g.has_node(start) and self.g.has_node(end)):
            return None
        
        # Initialize a queue for BFS
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            current_city, path = queue.popleft()

            # If we reach the end city, return the path
            if current_city == end:
                return path

            # Add current city to visited set
            visited.add(current_city)

            # Explore neighbors of the current city
            for neighbor in self.g.children_of(self.g.get_node(current_city)):
                if neighbor.get_name() not in visited:
                    queue.append((neighbor.get_name(), path + [neighbor.get_name()]))

        # If no path found
        return None 
