"""Function for generating, loading, saving and plotting trees.
"""
from .structures import Tree, Node

from collections import deque
import networkx as nx
from collections import deque
import string
import matplotlib.pyplot as plt


def NamesGenerator():
    """Create node names iterator.
    All names consist of upper laters and names follow in lexical order.
    Example: A, B, C ... AB, AC, AD.
    """

    g_index = 1
    while True:
        name = []
        inx = g_index
        p_size = len(string.ascii_uppercase)
        while True:
            remainder = inx % p_size
            inx = inx // p_size
            name.append(string.ascii_uppercase[remainder])
            if inx == 0: break

        yield "".join(name)
        g_index += 1


def generate_tree(depth = 5, leave_count = 3):
    """Generate a tree with depth = depth,
    each node(except leaves) has leave_count leaves.
    """

    tree = Tree()
    leaves = [tree.root_node]

    name_generator = NamesGenerator()

    for _ in range(depth):
        new_leaves = []
        for leave in leaves:
            for _ in range(leave_count):
                new_child = Node(name_generator.__next__())
                leave.connections.append(new_child)
                new_leaves.append(new_child)
        leaves = new_leaves
    return tree


def save_tree(tree, fname):
    """Save the tree to the file.
    Use simple text format. Each line has this format:
    A->B;\n
    where A and B are nodes of the tree.
    """

    with open(fname, "w") as file:
        for node in tree.nodes():
            for child in node.connections:
                file.write("{pname}->{cname};\n".format(pname=node,cname=child))


class NoRootException(Exception):
    """This exception rases during loading a Tree
    from the file, when there isn't or multiple candidates for
    the root node(root node hasn't input edges).
    """

    def __init__(self, count):

        message = "{} root_condidates".format(str(count))
        super(NoRootException, self).__init__(message)


def load_tree(fname):
    """Load a tree from the file.
    Parameters
    ----------
    fname :
        name of a file.
        There could be is a simple text file with lines like
        A->B;\n, or .dot file.

    Returns
    -------
    Tree

    Exceptions
    -------
    NoRootException
        rases there isn't or multiple candidates for
        the root node.
    """

    connections = []

    if len(fname.split('.')) > 1 and fname.split('.')[-1] == "dot":
        G = nx.drawing.nx_pydot.read_dot(fname)
        connections = [ (edge[0], edge[1]) for edge in G.edges ]
    else:
        with open(fname, "r") as file:
            lines = file.readlines()
            for line in lines:
                node_names = line.split(';')[0].split('->')
                connections.append(node_names)

    nodes = dict()
    nodes_with_input = set()

    for node_names in connections:
        cfrom, cto = node_names
        nodes[cfrom] = nodes.get(cfrom, Node(cfrom))
        nodes[cto] = nodes.get(cto, Node(cto))

        nodes[cfrom].connections.append(nodes[cto])
        nodes_with_input.add(cto)

    root_condidates = list(set(nodes.keys()).difference(nodes_with_input))

    if len(root_condidates) != 1:
        raise NoRootException(len(root_condidates))

    return Tree(nodes[root_condidates[0]])


def to_nx_graph(tree):
    """Transform tree to networkx format."""

    G=nx.DiGraph()
    for node in tree.nodes():
        for child in node.connections:
            G.add_edge(node,child)
    return G



def draw_tree(tree, fname = None):
    """Draw tree or save image to the file."""

    G = to_nx_graph(tree)
    nx.draw_networkx(G, pos=nx.kamada_kawai_layout(G))

    if fname:
        plt.savefig(fname, format="PNG")
        plt.close()
    else:
        plt.show()

def way_to_str(way, delimiter = ""):
    """Convert sequence of Nodes to a string"""
    return delimiter.join([ str(n) for n in way ])
