from graph import Edge, Graph, Node

class Ranker:
    def __init__(self, collection):
        self.collection = collection
        self.ranking = Graph()
        for image in collection:
            images_node = Node(frozenset(image))
            self.ranking.add_node(images_node)