# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 15:04:56 2016

@author: guttag, revised egrimson
"""

class Node(object):
    def __init__(self, name):

        """Initializes a Node object with a name.
        
        Args:
            name (str): The name of the node.
        """
        self.name = name

    def getName(self):
        """Returns the name of the node."""
        return self.name

    def __str__(self):
        """Returns a string representation of the node."""
        return self.name


class Edge(object):
    def __init__(self, src, dest):
        """Initializes an Edge object with a source and destination node.
        
        Args:
            src (Node): The source node.
            dest (Node): The destination node.
        """
        self.src = src
        self.dest = dest

    def getSource(self):
        """Returns the source node of the edge."""
        return self.src

    def getDestination(self):
        """Returns the destination node of the edge."""
        return self.dest

    def __str__(self):
        """Returns a string representation of the edge."""
        return self.src.getName() + '->' + self.dest.getName()


class Digraph(object):
    """A class representing a directed graph. The edges is a dict mapping each node to a list of its children."""
    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        """Adds a node to the graph.
        
        Args:
            node (Node): The node to be added.
            
        Raises:
            ValueError: If the node already exists in the graph.
        """

        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        """Adds an edge to the graph.
        
        Args:
            edge (Edge): The edge to be added.
            
        Raises:
            ValueError: If the source or destination node of the edge is not in the graph.
        """

        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        """Returns the children of a node.
        
        Args:
            node (Node): The node to get the children of.
            
        Returns:
            list: The children of the node.
        """
        return self.edges[node]

    def hasNode(self, node):
        """Checks if a node is in the graph.
        
        Args:
            node (Node): The node to check.
            
        Returns:
            bool: True if the node is in the graph, False otherwise.
        """
        return node in self.edges

    def getNode(self, name):
        """Gets a node by its name.
        
        Args:
            name (str): The name of the node.
            
        Returns:
            Node: The node with the given name.
            
        Raises:
            NameError: If no node with the given name exists.
        """

        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        """Returns a string representation of the graph."""
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'
        return result[:-1]  # omit final newline


class Graph(Digraph):
    def addEdge(self, edge):
        """Adds an edge to the graph and also adds a reverse edge.
        
        Args:
            edge (Edge): The edge to be added.
        """
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def buildCityGraph(graphType):
    """Builds a city graph of a given type.
    
    Args:
        graphType (type): The type of the graph to build.
        
    Returns:
        Digraph: The built city graph.
    """
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles'):  # Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g


def printPath(path):

    """Prints a path.
    
    Args:
        path (list): The path to print.
        
    Returns:
        str: A string representation of the path.
    """
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'

    return result


def DFS(graph, start, end, path, shortest, toPrint=False):
    """Performs a depth-first search (DFS) on a graph.
    
    Args:
        graph (Digraph): The graph to perform the DFS on.
        start (Node): The start node.
        end (Node): The end node.
        path (list): The current path.
        shortest (list): The current shortest path.
        toPrint (bool, optional): Whether to print the current DFS path. Defaults to False.
        
    Returns:
        list: The shortest path from start to end in the graph.
    """
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):

        if node not in path:  # avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)
    return shortest

def shortestPath(graph, start, end, toPrint=False):
    """Finds the shortest path between two nodes in a graph.
    
    Args:
        graph (Digraph): The graph to find the shortest path in.
        start (Node): The start node.
        end (Node): The end node.
        toPrint (bool, optional): Whether to print the shortest path. Defaults to False.
        
    Returns:
        list: The shortest path from start to end in the graph.
    """
    return DFS(graph, start, end, [], None, toPrint)


def testSP(source, destination):
    """Tests the shortest path function.
    
    Args:
        source (str): The name of the source node.
        destination (str): The name of the destination node.
    """
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint=True)
    if sp != None:
        print('Shortest path from', source, 'to', destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)


testSP('Chicago', 'Boston')
print()

printQueue = True


def BFS(graph, start, end, toPrint=False):
    """Performs a breadth-first search (BFS) on a graph.
    
    Args:
        graph (Digraph): The graph to perform the BFS on.
        start (Node): The start node.
        end (Node): The end node.
        toPrint (bool, optional): Whether to print the current BFS path. Defaults to False.
        
    Returns:
        list: The shortest path from start to end in the graph.
    """
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        if printQueue:
            print('Queue:', len(pathQueue))
            for p in pathQueue:
                print(printPath(p))
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
            print()
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None


def shortestPath(graph, start, end, toPrint=False):
    """Finds the shortest path between two nodes in a graph using BFS.
    
    Args:
        graph (Digraph): The graph to find the shortest path in.
        start (Node): The start node.
        end (Node): The end node.
        toPrint (bool, optional): Whether to print the shortest path. Defaults to False.
        
    Returns:
        list: The shortest path from start to end in the graph.
    """
    return BFS(graph, start, end, toPrint)