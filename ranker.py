from graph import Graph, Node, Edge

class Ranker(Graph):
    def __init__(self, collection):
        super().__init__()

        self.collection = collection
        for item in collection:
            rankable_node = RankableNode(item)
            self.add_node(rankable_node)

    def add_ranking(self, loser, winner):  # tail = loser
        winner_node = self.nodes.get(winner)
        loser_node = self.nodes.get(loser)
        self.add_edge(Edge(loser_node, winner_node))

    @property
    def next_comparison(self):
        considered = set()
        not_considered = set()

        for node in self.nodes.values():
            if node in not_considered:
                continue
            elif len(node.edges) > 0:
                not_considered.add(node)
                if node in considered:
                    considered.remove(node)
            else:
                considered.add(node)

        sorted_considered = sorted(considered, key=lambda node: node.depth)
        return sorted_considered[0], sorted_considered[1]

class RankableNode(Node):
    def __init__(self, id_):
        super().__init__(id_)

        self.depth = 0

if __name__ == '__main__':
    coll = ['sam', 'josh', 'gchuckin']
    r = Ranker(coll)
    print(r.next_comparison)
    r.add_ranking('gchuckin', 'josh')
    print(r.next_comparison)