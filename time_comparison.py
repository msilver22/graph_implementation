import networkx as nx
import time

from utils import nx_import_graph, ig_import_graph
import pandas as pd

def measure_time(graph_func, *args):
    start_time = time.time()
    graph_func(*args)
    end_time = time.time()
    return end_time - start_time


def main():

    dataset = "kar"

    TXT_PATH = f"./datasets/data/{dataset}.txt"
    MTX_PATH = f"./datasets/data/{dataset}.mtx"
    GML_PATH = f"./datasets/data/{dataset}.gml"

    # Measure time for each graph creation
    time_G1 = measure_time(nx_import_graph, TXT_PATH)
    time_G2 = measure_time(nx_import_graph, MTX_PATH)
    time_G3 = measure_time(nx_import_graph, GML_PATH)
    time_G4 = measure_time(ig_import_graph, TXT_PATH)
    time_G5 = measure_time(ig_import_graph, MTX_PATH)
    time_G6 = measure_time(ig_import_graph, GML_PATH)


    data = {
        "File Type": ["TXT", "MTX", "GML"],
        "Networkx Time (s)": [time_G1, time_G2, time_G3],
        "Igraph Time (s)": [time_G4, time_G5, time_G6]
    }

    df = pd.DataFrame(data)
    print(df)

    best_nx_time = min(df["Networkx Time (s)"])
    best_ig_time = min(df["Igraph Time (s)"])

    print(f"Best Networkx time: {best_nx_time:.6f} seconds")
    print(f"Best Igraph time: {best_ig_time:.6f} seconds")

    if best_nx_time < best_ig_time:
        best_result = f"Networkx is faster with {best_nx_time:.6f} seconds"
    else:
        best_result = f"Igraph is faster with {best_ig_time:.6f} seconds"

    print(best_result)

if __name__ == "__main__":
    main()