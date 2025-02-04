import networkx as nx
import time

from src.utils.utils import nx_import_graph, ig_import_graph
from src.utils.markdown import create_markdown_table
import pandas as pd

def measure_time(graph_func, *args):
    start_time = time.time()
    graph_func(*args)
    end_time = time.time()
    return round(end_time - start_time, 5)


def main():

    #datasets = ["kar","words"]
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

if __name__ == "__main__":
    main()