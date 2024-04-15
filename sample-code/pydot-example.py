import pydot

# create a new graph
graph = pydot.Dot(graph_type='graph')

# add nodes to the graph
node_a = pydot.Node("Node A")
node_b = pydot.Node("Node B")
node_c = pydot.Node("Node C")

graph.add_node(node_a)
graph.add_node(node_b)
graph.add_node(node_c)

# add edges to the graph
edge_ab = pydot.Edge(node_a, node_b)
edge_bc = pydot.Edge(node_b, node_c)
edge_ca = pydot.Edge(node_c, node_a)

graph.add_edge(edge_ab)
graph.add_edge(edge_bc)
graph.add_edge(edge_ca)

# save the graph as a PNG image
graph.write_png('example_graph.png')
