import pydot

class Digraph:
    def __init__(self):
        self.graph = pydot.Dot(graph_type='digraph')

    def add_node(self, name):
        node = pydot.Node(name)
        self.graph.add_node(node)

    def add_edge(self, source, dest):
        edge = pydot.Edge(source, dest)
        self.graph.add_edge(edge)

    def draw(self, filename='graph.png'):
        self.graph.write_png(filename)

if __name__ == '__main__':
    # create a new Digraph object
    g = Digraph()
    
    # add nodes to the graph
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    
    # add edges to the graph
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'A')
    
    # draw the graph and save it as 'my_graph.png'
    g.draw('my_graph.png')