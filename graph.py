import networkx


class Graph(object):
    def __init__(self):
        self.Graph = None
        self.look_up_dictionary = {}
        self.look_back_list = []
        self.node_size = 0

    def encode_node(self):
        look_up = self.look_up_dictionary
        look_back = self.look_back_list

        for node in self.Graph.nodes():
            look_up[node] = self.node_size
            look_back.append(node)
            self.node_size += 1
            self.Graph.nodes[node]['status'] = ''

    def read_graph(self, graph):

        self.Graph = graph
        self.encode_node()

    def create_graph(self, filename):
        self.Graph = networkx.DiGraph()

        file = open(filename, 'r')

        for line in file.readlines():
            src, dst = line.split()
            self.Graph.add_edge(src, dst)
            self.Graph.add_edge(dst, src)
            self.Graph[src][dst]['weight'] = 1.0
            self.Graph[dst][src]['weight'] = 1.0

        file.close()
        self.encode_node()
