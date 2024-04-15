def test_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5

def test_coordinate():
    c = lc.Coordinate(3, 4)
    origin = lc.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5

 Write documentation for the selected code. The reply should be a codeblock containing the original code with the documentation added as comments. Use the most appropriate documentation style for the programming language used (e.g. JSDoc for JavaScript, docstrings for Python etc.

## Copilot ---

```python
class Node:
    """Represents a node in a graph."""
    def __init__(self, name):
        """Initializes a Node with a name.

        Args:
            name (str): The name of the Node.
        """
        self.name = name

    def get_name(self):
        """Returns the name of the Node.

        Returns:
            str: The name of the Node.
        """
        return self.name

    def __str__(self):
        """Returns a string representation of the Node.

        Returns:
            str: The name of the Node.
        """
        return self.name


class Edge:
    """Represents a directed edge in a graph."""
    def __init__(self, src, dest):
        """Initializes an Edge with a source Node and a destination Node.

        Args:
            src (Node): The source Node.
            dest (Node): The destination Node.
        """
        self.src = src
        self.dest = dest

    def get_source(self):
        """Returns the source Node of the Edge.

        Returns:
            Node: The source Node.
        """
        return self.src

    def get_destination(self):
        """Returns the destination Node of the Edge.

        Returns:
            Node: The destination Node.
        """
        return self.dest

    def __str__(self):
        """Returns a string representation of the Edge.

        Returns:
            str: A string in the format 'source->destination'.
        """
        return self.src.get_name() + '->' + self.dest.get_name()


class Digraph:
    """Represents a directed graph."""
    def __init__(self):
        """Initializes an empty directed graph."""
        self.edges = {}

    def add_node(self, node):
        """Adds a Node to the graph.

        Args:
            node (Node): The Node to add.

        Raises:
            ValueError: If the Node is already in the graph.
        """
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def add_edge(self, edge):
        """Adds an Edge to the graph.

        Args:
            edge (Edge): The Edge to add.

        Raises:
            ValueError: If either the source or destination Node of the Edge is not in the graph.
        """
        src = edge.get_source()
        dest = edge.get_destination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def children_of(self, node):
        """Returns the children of a Node.

        Args:
            node (Node): The Node to get the children of.

        Returns:
            list: The children of the Node.
        """
        return self.edges[node]

    def has_node(self, node):
        """Checks if a Node is in the graph.

        Args:
            node (Node): The Node to check.

        Returns:
            bool: True if the Node is in the graph, False otherwise.
        """
        return node in self.edges

    def get_node(self, name):
        """Returns the Node with the given name.

        Args:
            name (str): The name of the Node.

        Returns:
            Node: The Node with the given name.

        Raises:
            NameError: If there is no Node with the given name.
        """
        for n in self.edges:
            if n.get_name() == name:
                return n
        raise NameError(name)

    def __str__(self):
        """Returns a string representation of the graph.

        Returns:
            str: A string representation of the graph.
        """
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result += src.get_name() + '->' + dest.get_name() + '\n'
        return result[:-1]  # Omit final newline
```

