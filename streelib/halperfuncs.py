"""Function for generating, loading, saving and plotting trees.
"""
from .structures import Tree, Node
from collections import deque
import networkx as nx
from collections import deque


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


def way_to_str(way, delimiter = ""):
    """Convert sequence of Nodes to a string"""
    return delimiter.join([ str(n) for n in way ])
