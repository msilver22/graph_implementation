# Graph implementation using NetworkX and iGraph libraries

To start, we need to import the required libraries:

```python
import networkx as nx
import igraph as ig
```

## Import functions

Graphs can be stored in various formats such as **`.txt` (edge list), `.mtx` (matrix market format), and `.gml` (graph markup language)**.  
To check the computational time for each file type, refer to this [link](https://github.com/msilver22/graph_implementation/blob/main/outputs/import_time_table.md)

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




