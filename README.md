# INTRO
This is "The Simple Tree Lib".
The "Simple Tree Lib" provides Tree and Node structures and just one alg
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

# INSTALLATION

### Optional:
* python3 -m venv env
* source env/bin/activate

### This project is on PyPi so just:
* pip3 install my_simple_tree_library

### OR:
* pip3 install -r requirements.txt
* python3 setup.py install

### RUN
waysintree -h
waysintree generate
waysintree parsetree test2_4.tr --delimiter .
A.B.D
A.B.E
A.C.F
A.C.G

#### Usage:
* waysintree parcetree <file_name> [ --delimeter DELIMETER ]
* waysintree generate
* waysintree tests

#### Arguments:
* parsetree  parse tree and output all ways
* generate create test files in current directory
* tests perform all tests

#### Options:
* -h --help     show this help message and exit
* --delimiter   delimiter between nodes in a way
