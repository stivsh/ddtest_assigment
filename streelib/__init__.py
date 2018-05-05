"""This is "The Simple Tree Lib".
The Simple Tree Lib" provides Tree and Node structures and just one alg
DFS traversal.
Cause this all was done just for as a test work for the job application.

This script takes a file with a tree data and outputs all ways in this tree.
Files cat be a .dot file or a simple text file, with lines like this:
A->B;
B->C;
Where A,B and C are Nodes in an input tree and A->B indicates that
there is an edge from A to B.

Test files weren't be provided so use "generate" arg to create test examples
with pictures of trees in a current directory.

Usage:
    waysintree parsetree <file_name> [ --delimiter DELIMETER ]
    waysintree generate
    waysintree tests

Arguments:
  parsetree  parse tree and output all ways
  generate create test files in current directory
  tests perform all tests

Options:
  -h --help     show this help message and exit
  --delimiter   delimiter between nodes in a way

"""

from .structures import Node, Tree
from .algths import df_traversal
from .halperfuncs import generate_tree, save_tree, load_tree, draw_tree

__all__ = ['Node', 'Tree', 'df_traversal',
            'generate_tree', 'save_tree', 'load_tree', 'draw_tree']

from docopt import docopt
from .tests import generate_test_files
from .halperfuncs import way_to_str

def main():
    args = docopt(__doc__)

    if args['generate']:
        print('generate test examples')
        generate_test_files()

    elif args['tests']:
        print('performe tests')

    elif args['parsetree']:
        tree = load_tree(args['<file_name>'])
        ways = df_traversal(tree)
        print("\n".join([ way_to_str(way,
                    delimiter = ['', args['DELIMETER']][args['--delimiter']])
                    for way in ways ]))
