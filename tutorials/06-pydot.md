# Pydot Example
This is an example of how to use the Pydot library in Python to create and save a graph.

## Installation

To use Pydot, you must first install the Graphviz graph visualization tool. You can download Graphviz from the official website: https://graphviz.org/download/

After installing Graphviz, you can install Pydot using pip:

```
$ pip install pydot
```

## Usage

To use Pydot, you need to import the pydot module in your Python code:

```
import pydot
```

Then, you can create a new graph using the pydot.Dot() constructor:

```
graph = pydot.Dot(graph_type='graph')
```

This creates a new graph object with the specified graph_type. You can add nodes to the graph using the pydot.Node() constructor:

```
node_a = pydot.Node("Node A")
node_b = pydot.Node("Node B")
node_c = pydot.Node("Node C")
```

This creates three new node objects with the specified names. You can add the nodes to the graph using the add_node() method:

```
graph.add_node(node_a)
graph.add_node(node_b)
graph.add_node(node_c)
```

This adds the three nodes to the graph. You can add edges to the graph using the pydot.Edge() constructor:

```
edge_ab = pydot.Edge(node_a, node_b)
edge_bc = pydot.Edge(node_b, node_c)
edge_ca = pydot.Edge(node_c, node_a)
```

This creates three new edge objects connecting the nodes in the specified order. You can add the edges to the graph using the add_edge() method:

```
graph.add_edge(edge_ab)
graph.add_edge(edge_bc)
graph.add_edge(edge_ca)
```

This adds the three edges to the graph. Finally, you can save the graph as a PNG image using the write_png() method:

```
graph.write_png('example_graph.png')
```

This saves the graph as a PNG image file named example_graph.png.
<img src="./img/example_graph.png"/>

