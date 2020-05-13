from typing import Hashable

class Node:
    def __init__(self, id_: Hashable):
        self.id: Hashable = id_

        self.edges: dict[Hashable: Edge] = {}

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self)


class Edge:
    def __init__(self, tail: Node, head: Node):
        self.tail: Node = tail
        self.head: Node = head


class Graph:
    def __init__(self):
        self.nodes: dict[Hashable: Node] = {}

    def add_node(self, node: Node):
        self.nodes[node.id] = node

    def add_edge(self, edge: Edge):
        self.nodes[edge.tail.id].edges[edge.head.id] = edge

    def breadth_first_traverse(self, start_id):
        s = self.nodes[start_id]
        layers = [{s}]  # layer : nodes in layer
        discovered = set()

        current_layer = {s}
        next_layer = set()

        while len(current_layer) > 0:
            node = current_layer.pop()
            if node in discovered:
                continue

            discovered.add(node)
            for edge in node.edges.values():
                if edge.head not in discovered:
                    next_layer.add(edge.head)

            if len(current_layer) == 0:
                current_layer = next_layer
                layers.append(current_layer.copy())
                next_layer = set()

        return layers[:-1]

    def breadth_first_search(self, s_id, t_id):
        s = self.nodes[s_id]
        t = self.nodes[t_id]
        discovered = set()
        stack = [s]
        parents = {}

        while len(stack) > 0:
            top = stack.pop(0)
            if top in discovered:
                continue
            discovered.add(top)
            edges = top.edges.values()

            for edge in edges:
                new_node = edge.head
                parents[new_node] = top
                if new_node == t:
                    ret = new_node
                    path = [ret]
                    while ret != s:
                        ret = parents[ret]
                        path.append(ret)
                    return list(reversed(path))
                elif new_node not in discovered:
                    stack.append(new_node)

    def __str__(self):
        out = ""
        for node in self.nodes.values():
            out += str(node)
            for edge in node.edges.values():
                out += f" -> {edge.head}"
            out += "\n"
        return out[:-1]

    def __contains__(self, item):
        return item in self.nodes


if __name__ == '__main__':
    graph = Graph()

    graph.add_node(Node(1))
    graph.add_node(Node(2))
    graph.add_node(Node(3))
    graph.add_node(Node(4))

    graph.add_edge(Edge(graph.nodes[1], graph.nodes[2]))
    graph.add_edge(Edge(graph.nodes[1], graph.nodes[3]))
    graph.add_edge(Edge(graph.nodes[2], graph.nodes[3]))
    graph.add_edge(Edge(graph.nodes[2], graph.nodes[4]))

    print(graph)

    print(graph.breadth_first_traverse(1))
    print(graph.breadth_first_search(1,3))
