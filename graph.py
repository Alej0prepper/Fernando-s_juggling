class Node:
    def __init__(self, Id):
        self.Id = Id

    def generate_edges(self, siteswap_string):
        edges = []
        if self.Id[0] == 1:
            for i in range(len(self.Id) + 1):
                if i != len(self.Id) and self.Id[i] == 1:
                    continue
                w = self.Id[1:] + [0]
                if i != 0:
                    w[i - 1] = 1
                if str(i) in siteswap_string:
                    edges.append(Edge(self, Node(w), i))
        else:
            w = self.Id[1:] + [0]
            edges.append(Edge(self, Node(w), 0))
        return edges

    def __hash__(self):
        return hash(tuple(self.Id))

    def __eq__(self, other):
        return tuple(self.Id) == tuple(other.Id)

    def __repr__(self):
        return f"Node({self.Id})"

class Edge:
    def __init__(self, From: Node, To: Node, value: int):
        self.From = From
        self.To = To
        self.value = value

    def __repr__(self):
        return f"Edge({self.From} -> {self.To}, value={self.value})"

class Graph:
    def __init__(self):
        self.siteswap = []
        self.nodes = set()
        self.edges = []
        self.adjacency_list = {}

    def build_graph(self, init_id, siteswap_string):
        self.nodes = set()
        self.edges = []
        self.adjacency_list = {}
        self.siteswap = init_id
        self.siteswap_string = siteswap_string
        waiting_nodes = [Node(init_id)]
        visited_nodes = set()
        while waiting_nodes:
            current = waiting_nodes.pop()
            if current in visited_nodes:
                continue
            visited_nodes.add(current)
            self.nodes.add(current)
            for edge in current.generate_edges(self.siteswap_string):
                if edge.To not in visited_nodes:
                    waiting_nodes.append(edge.To)
                self.edges.append(edge)
                if current not in self.adjacency_list:
                    self.adjacency_list[current] = []
                self.adjacency_list[current].append(edge)

    def find_cycles_from_node(self, start_node):
        cycles = []
        start_node = Node(start_node)

        def dfs(node, visited, path, path_values):
            if node == start_node and path:
                cycles.append(path_values)
                return
            if node in visited:
                return
            visited.add(node)
            for edge in self.adjacency_list.get(node, []):
                dfs(edge.To, visited.copy(), path + [edge.To], path_values + [edge.value])

        dfs(start_node, set(), [], [])
        return cycles

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

    def decrease_siteswap_size(self):
        for i in range(len(self.siteswap)):
            if self.siteswap[-1 - i] == 1:
                self.siteswap[-1 - i] = 0
                return self.siteswap

    def get_siteswap_from_graph(self):
        return self

    def get_subsiteswap_list(self):
        siteswaps_list = []
        while 1 in self.siteswap:
            # Build the graph and find cycles
            self.build_graph(self.siteswap, self.siteswap_string)
            for node in self.nodes:
                cycles = self.find_cycles_from_node(node.Id)
                siteswaps_list.extend(cycles)
            # self.to_mermaid("graphs/" + ''.join([str(number) for number in self.siteswap]) + ".md")
            self.decrease_siteswap_size()
        return siteswaps_list