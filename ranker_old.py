from graph import Edge, Graph, Node


class Ranker(Graph):
    def __init__(self, collection):
        super().__init__()

        self.collection = collection
        for image in collection:
            images_node = RankableNode([image])
            self.add_node(images_node)

    def add_ranking(self, less, greater, equal=False):
        less_node = self.nodes[frozenset([less])]
        greater_node = self.nodes[frozenset([greater])]

        if equal:
            tie_group = RankableNode(less_node.id.union(greater_node.id))
            self.add_node(tie_group)
            self.remove_node(less_node)
            self.remove_node(greater_node)
        else:
            parent = RankableNode(greater_node.id.copy())
            parent.depth = greater_node.depth
            self.add_edge(Edge(parent, less_node))
            self.add_edge(Edge(parent, greater_node))

    @property
    def next_comparison(self):
        considered = set()
        not_considered = set()

        for node in self.nodes:
            if node in not_considered:
                continue
            elif len(node.edges) > 0:
                not_considered.add(node)
                considered.remove(node)
            else:
                considered.add(node)

        sorted_considered = sorted(considered, key=lambda node: node.depth)
        return sorted_considered[0]

    @property
    def rank(self):
        return {images: node.depth for images, node in self.nodes.items()}


class RankableNode(Node):
    def __init__(self, images):
        super().__init__(frozenset(images))

        self.depth = 0
