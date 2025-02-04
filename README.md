# Graph implementation using NetworkX and iGraph libraries

To start, we need to import the required libraries:

```python
import networkx as nx
import igraph as ig
```

## Import functions

Graphs can be stored in various formats such as **`.txt` (edge list), `.mtx` (matrix market format), and `.gml` (graph markup language)**.  
To check the computational time for each file type, refer to this [link](https://github.com/msilver22/graph_implementation/blob/main/outputs/import_time_table.md).

### Importing from a `.txt` file

Let's assume we store the graph in the following path:
```python
file_path = "graph.txt"
```

#### Case 1: Standard Edge List 

##### NetworkX:
```python
graph = nx.read_edgelist(file_path, nodetype=int)
```

##### iGraph:
```python
graph = ig.Graph.Read_Edgelist(file_path, directed=False)
```

#### Case 2: Weighted Edge List

##### NetworkX:
```python
graph = nx.read_weighted_edgelist(file_path, nodetype=int)
```

### Importing from a `.mtx` file

Let's assume we store the adjacency matrix of the graph as follows:

```python
file_path = "graph.mtx"
graph_matrix = scipy.io.mmread(file_path)
```

#### NetworkX:
```python
graph = nx.Graph(graph_matrix)
```

#### iGraph:
```python
graph = ig.Graph.Weighted_Adjacency(matrix.toarray().tolist(), mode="undirected")
```

### Importing from a `.gml` file

Let's assume we store the graph in the following path:
```python
file_path = "graph.gml"
```

#### NetworkX:
```python
graph = nx.read_gml(file_path, label="id")
```

#### iGraph:
```python
graph = ig.Graph.Read_GML(file_path)
```


## API References
Let's assume that the variable `graph` is a nx.Graph or ig.Graph object.  
To check the computational time for each file type, refer to this [link](https://github.com/msilver22/graph_implementation/blob/main/outputs/functions_time_table.md).

### Number of nodes
#### NetworkX:
```python
graph.number_of_nodes()
```

#### iGraph:
```python
graph.vcount()
```

### Number of edges
#### NetworkX:
```python
graph.number_of_edges()
```

#### iGraph:
```python
graph.ecount()
```

### Node List
#### NetworkX:
```python
nx.nodes(graph)
```

#### iGraph:
```python
graph.vs()
```

### Edge List
#### NetworkX:
```python
nx.edges(graph)
```

#### iGraph:
```python
graph.get_edgelist()
```

### Neighbourhood of node `u`

#### NetworkX or iGraph:
```python
graph.neighbors(u)
```

### Neighbourhood of node `u`

#### NetworkX or iGraph:
```python
graph.degree(u)
```

### Adjacency between node `u` and node `v`

#### NetworkX:
```python
graph.has_edge(u,v)
```

#### iGraph:
```python
graph.are_adjacent(0,1)
```

### Betweenness Centrality

#### NetworkX:
```python
nx.betweenneess_centrality(graph)
```

#### iGraph:
```python
graph.betweenness()
```

### Add edge (`u`,`v`)

#### NetworkX or iGraph:
```python
graph.degree(u)
```

### Remove edge (`u`,`v`)

#### NetworkX:
```python
graph.remove_edge(u,v)
```

#### iGraph:
```python
graph.delete_edges(u,v)
```


