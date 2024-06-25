class Node:
    def __init__(self, Id):
        self.Id = Id

    def generate_edges(self):
        edges = []
        if self.Id[0] == 1:
            for i in range(len(self.Id) + 1):
                if i != len(self.Id) and self.Id[i] == 1:
                    continue
                w = self.Id[1:] + [0]
                if i != 0:
                    w[i - 1] = 1
                edges.append(Edge(self, Node(w), i))
        else:
            w = self.Id[1:] + [0]
            edges.append(Edge(self, Node(w), 0))
        return edges

    def __hash__(self):
        return hash(tuple(self.Id))

    def __eq__(self, other):
        return tuple(self.Id) == tuple(other.Id)

class Edge:
    def __init__(self, From: Node, To: Node, value: int):
        self.From = From
        self.To = To
        self.value = value

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def build_graph(self, init_id):
        waiting_nodes = [Node(init_id)]
        visited_nodes = set()
        while waiting_nodes:
            current = waiting_nodes.pop()
            if current in visited_nodes:
                continue
            visited_nodes.add(current)
            self.nodes.add(current)
            for edge in current.generate_edges():
                if edge.To not in visited_nodes:
                    waiting_nodes.append(edge.To)
                self.edges.append(edge)

    def to_mermaid(self, file_name) -> str:
        mermaid_str = "stateDiagram-v2\n"

        for edge in self.edges:
            from_node = ','.join([str(item) for item in edge.From.Id])
            to_node = ','.join([str(item) for item in edge.To.Id])
            from_node_label = f'{from_node}'
            to_node_label = f'{to_node}'
            mermaid_str += f'    {from_node_label} --> {to_node_label} : {edge.value}\n'

        md_content = f"```mermaid\n{mermaid_str}\n```"
        with open(file_name, 'w') as f:
            f.write(md_content)

# Example usage:
graph = Graph()
graph.build_graph([1, 0, 0, 0])

mermaid_syntax = graph.to_mermaid("1000.md")

