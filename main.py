from graph import *
from grarep import GraRep


def main():
    graph = Graph()
    graph_path = "data/nodes.edgelist"
    embedding_path = "data/embedding.txt"
    graph.create_graph(filename=graph_path)
    Kstep = 4
    dimension = 128

    model = GraRep(graph=graph, Kstep=Kstep, dimension=dimension)

    model.save_embeddings(embedding_path)


if __name__ == '__main__':
    main()
