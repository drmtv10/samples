"""
A Graph class contains a list of nodes and edges. You can sometimes get
by with just a list of edges, since edges contain references to the nodes
they connect to, or vice versa. However, our Graph class is built with
both for the following reasons: 

If you're storing a disconnected graph, not every node will be tied to an
edge, so you should store a list of nodes.  We could probably leave it there,
but storing an edge list will make our lives much easier when we're trying
to print out different types of graph representations. 
Unfortunately, having both makes insertion a bit complicated. We can
assume that each value is unique, but we need to be careful about keeping
both nodes and edges updated when either is inserted. You'll also be
given these insertion functions to help you out:
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        edge_list = list()
        for each_edge in self.edges:
            edge_detail = (each_edge.value, each_edge.node_from.value, each_edge.node_to.value)
            edge_list.append(edge_detail)
        return edge_list

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        adjacencies = list()
        for eN in self.nodes:
            adjacents = list()
            for adjacent_edge in eN.edges:
                #print adjacent_edge.node_from.value, eN.value
                if (adjacent_edge.node_from.value == eN.value):
                    adjacent_item = (adjacent_edge.node_to.value, adjacent_edge.value)
                    adjacents.append(adjacent_item)
            if (adjacents == []):
                adjacencies.append(None)
            else:
                adjacencies.append(adjacents)
        return adjacencies
        #[ adjacencies.append(v.value) for v in self.nodes ]
        #[ adjacencies.append(v.value) for v in self.edges ]
        #print len(self.nodes), len(self.edges)
        return adjacencies
    
    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        a_m = list()
        for row in self.nodes:
            a_m_row = list()
            for col in self.nodes:
                bEdge = False
                for edge in self.edges:
                    if (row.value == edge.node_from.value) and \
                       (col.value == edge.node_to.value):
                      a_m_row.append(edge.value)
                      bEdge = True
                if not bEdge:
                    a_m_row.append(0)
            #print a_m_row
            a_m.append(a_m_row)
        return a_m

graph = Graph()
graph.insert_node(0)
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print graph.get_edge_list()
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print graph.get_adjacency_list()
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print graph.get_adjacency_matrix()
