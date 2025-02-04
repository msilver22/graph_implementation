import networkx as nx
import time

from src.utils.utils import nx_import_graph, ig_import_graph
from src.utils.markdown import create_markdown_table
import pandas as pd

def measure_time(graph_func, *args):
    start_time = time.time()
    graph_func(*args)
    end_time = time.time()
    return round(end_time - start_time, 8)


def main():

    datasets = ["kar","words", "vote","pow","fb-75"]
    raws = []

    for dataset in datasets:
        G1 = nx_import_graph(f"./datasets/data/{dataset}.txt")
        G2 = ig_import_graph(f"./datasets/data/{dataset}.txt")
        if G1.number_of_nodes() + G1.number_of_edges() == G2.vcount() + G2.ecount():
            
            file_types = ["TXT", "MTX", "GML"]
            paths = [f"./datasets/data/{dataset}.{ft.lower()}" for ft in file_types]

            for path in paths:
                nx_time=measure_time(nx_import_graph, path)
                ig_time=measure_time(ig_import_graph, path)
                raws.append([dataset, G1.number_of_nodes() + G1.number_of_edges(), path.split(".")[-1].upper(), nx_time, ig_time])
       

    headers = ["Network", "Size", "File Type", "Nx Time(s)", "Ig Time(s)"]
    print(create_markdown_table(headers, raws, "./outputs/import_time_table.md"))

    functions = [ "Get Edge List", "Get Node List", "Get Neighbourhood", "Has Edge","Get Degree", "Get Betweenness Centrality", "Add Edge", "Remove Edge"]
    raws = []

    
    for dataset in datasets:
        print(dataset)
        for func_name in functions:
            print(func_name)
            G1 = nx_import_graph(f"./datasets/data/{dataset}.txt")
            G2 = ig_import_graph(f"./datasets/data/{dataset}.txt")
            if G1.number_of_nodes() + G1.number_of_edges() == G2.vcount() + G2.ecount():
                if func_name == "Get Edge List":
                    nx_time=measure_time(nx.edges, G1)
                    ig_time=measure_time(G2.get_edgelist)
                elif func_name == "Get Node List":
                    nx_time=measure_time(nx.nodes, G1)
                    ig_time=measure_time(G2.vs)
                elif func_name == "Get Neighbourhood":
                    nx_time=measure_time(G1.neighbors, 1)
                    ig_time=measure_time(G2.neighbors, 0)
                elif func_name == "Has Edge":
                    nx_time=measure_time(G1.has_edge, 1, 2)
                    ig_time=measure_time(G2.are_adjacent, 0, 1)
                elif func_name == "Get Degree":
                    nx_time=measure_time(G1.degree, 1)
                    ig_time=measure_time(G2.degree, 0)
                elif func_name == "Get Betweenness Centrality":
                    nx_time=measure_time(nx.betweenness_centrality,G1)
                    ig_time=measure_time(G2.betweenness)
                elif func_name == "Add Edge":
                    if not G2.are_adjacent(0, 1):
                        nx_time=measure_time(G1.add_edge, 1, 2)
                        ig_time=measure_time(G2.add_edge, 0, 1)
                    else:
                        neighbors = set(G2.neighbors(0))
                        non_neighbors = set(range(G2.vcount())) - neighbors
                        v = non_neighbors.pop()
                        nx_time=measure_time(G1.add_edge, 1, v+1)
                        ig_time=measure_time(G2.add_edge, 0, v)   

                elif func_name == "Remove Edge":
                    if G2.are_connected(0, 1):
                        nx_time=measure_time(G1.add_edge, 1, 2)
                        ig_time=measure_time(G2.add_edge, 0, 1)
                    else:
                        neighbors = set(G2.neighbors(0))
                        v = neighbors.pop()
                        nx_time=measure_time(G1.remove_edge, 1, v+1)
                        ig_time=measure_time(G2.delete_edges, 0, v)  
                raws.append([dataset, G1.number_of_nodes() + G1.number_of_edges(), func_name, nx_time, ig_time])

    headers = ["Network", "Size", "Function", "Nx Time(s)", "Ig Time(s)"]
    print(create_markdown_table(headers, raws, "./outputs/functions_time_table.md"))

if __name__ == "__main__":
    main()