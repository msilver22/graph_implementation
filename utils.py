import networkx as nx
import igraph as ig
import scipy.io


def nx_import_graph(file_path: str) -> nx.Graph:
    """
    Import a graph from a .mtx file

    Parameters
    ----------
    file_path : str
        File path of the .mtx file

    Returns
    -------
    nx.Graph
        Graph imported from the .mtx file
    """
    # try:
    # Check if the graph file is in the .mtx format or .gml
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

    for node in graph.nodes:
        # graph.nodes[node]['name'] = node
        graph.nodes[node]["num_neighbors"] = len(list(graph.neighbors(node)))
    return graph

def ig_import_graph(file_path: str) -> ig.Graph:
    """
    Import a graph from a file using igraph

    Parameters
    ----------
    file_path : str
        File path of the graph file

    Returns
    -------
    ig.Graph
        Graph imported from the file
    """
    if file_path.endswith(".txt"):
        if file_path.endswith("pow.txt"):
            graph = ig.Graph.Read_Edgelist(file_path, directed=False)
            graph.es["weight"] = [float(weight) for weight in graph.es["weight"]]
        else:
            graph = ig.Graph.Read_Edgelist(file_path, directed=False)
    elif file_path.endswith(".mtx"):
        matrix = scipy.io.mmread(file_path)
        graph = ig.Graph.Weighted_Adjacency(matrix.toarray().tolist(), mode="undirected")
    elif file_path.endswith(".gml"):
        graph = ig.Graph.Read_GML(file_path)
    else:
        raise ValueError("File format not supported")

    graph.vs["num_neighbors"] = [len(graph.neighbors(node.index)) for node in graph.vs]
    return graph