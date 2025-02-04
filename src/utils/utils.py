import networkx as nx
import igraph as ig
import scipy.io


def nx_import_graph(file_path: str) -> nx.Graph:
    """
    Import a graph from a .mtx file

    Parameters
    ----------
    file_path : str
        File path of the .mtx/.txt./.gml file

    Returns
    -------
    nx.Graph
        Graph imported from the file path
    """
    # try:
    # Check if the graph file is in the .mtx format , .txt or .gml
    if file_path.endswith(".txt"):
        # if is the POW graph use weighted edges
        if file_path.endswith("pow.txt"):
            graph = nx.read_weighted_edgelist(file_path, nodetype=int)
        else:
            graph = nx.read_edgelist(file_path, nodetype=int)
    elif file_path.endswith(".mtx"):
        graph_matrix = scipy.io.mmread(file_path)
        graph = nx.Graph(graph_matrix)
    elif file_path.endswith(".gml"):
        graph = nx.read_gml(file_path, label="id")
    else:
        raise ValueError("File format not supported")
    return graph

def ig_import_graph(file_path: str) -> ig.Graph:
    """
    Import a graph from a file using igraph

    Parameters
    ----------
    file_path : str
        File path of the .mtx/.txt./.gml file
        
    Returns
    -------
    ig.Graph
        Graph imported from the file path
    """
    if file_path.endswith(".txt"):
        if file_path.endswith("pow.txt"):
            with open(file_path, 'r') as f:
                edges = []
                for line in f:
                    v1, v2, w = map(float, line.strip().split())
                    if v1 < v2:
                        edges.append((int(v1), int(v2)))
            graph = ig.Graph(edges=edges, directed=False)
        else:
            graph = ig.Graph.Read_Edgelist(file_path, directed=False)
    elif file_path.endswith(".mtx"):
        matrix = scipy.io.mmread(file_path)
        graph = ig.Graph.Weighted_Adjacency(matrix.toarray().tolist(), mode="undirected")
    elif file_path.endswith(".gml"):
        graph = ig.Graph.Read_GML(file_path)
    else:
        raise ValueError("File format not supported")
    
    # Igraph starts from 0 index, so remove the node created with 0 degree
    graph.vs.select(_degree=0).delete()
    return graph