from graph import Edge, Graph, Node


class Ranker(Graph):
    def __init__(self, collection):
        super().__init__()

        self.collection = collection
        for image in collection:
            images_node = ImagesNode([image])
            self.add_node(images_node)

    def add_ranking(self, less, greater, equal=False):
        less_node = self.nodes[frozenset([less])]
        greater_node = self.nodes[frozenset([greater])]

        parent = None
        if equal:
            parent = ImagesNode(less_node.id.union(greater_node.id))
        else:
            parent = ImagesNode(greater_node.id.copy())
        parent.depth = greater_node.depth

        self.add_edge(Edge(parent, less_node))
        self.add_edge(Edge(parent, greater_node))

    @property
    def next_comparison(self):
        considered = set()
        not_considered = set()

        for node in self.nodes:
            if node not in considered:
                continue
            elif len(node.edges) > 0:
                not_considered.add(node)
                considered.remove(node)
            else:
                considered.add(node)

        sorted_considered = sorted(considered, key=lambda node: node.depth)
        return sorted_considered[0], sorted_considered[1]

class ImagesNode(Node):
    def __init__(self, images):
        super().__init__(frozenset(images))

        self.depth = 0
