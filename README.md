# INTRO
This is "The Simple Tree Lib".
The "Simple Tree Lib" provides Tree and Node structures and just one alg
DFS traversal.
Cause this all was done just for as a test work for the job application.

This script takes a file with a tree data and outputs all ways in this tree.
Files have a simple structure, lines like this:
A->B;
B->C;

Where A,B and C are Nodes in an input tree and A->B indicates that
there is an edge from A to B.

[It's not up to date but it gives good intuition how it works.](https://github.com/stivsh/ddtest_assigment/blob/master/Experiments.ipynb)

# INSTALLATION

### Optional:
* python3 -m venv env
* source env/bin/activate

### This project is on PyPi so just:
* pip3 install the_simple_tree_lib

### OR:
* python3 setup.py install

### RUN
waysintree -h
waysintree parsetree test2_4.tr --delimiter .
A.B.D
A.B.E
A.C.F
A.C.G

#### Usage:
Usage:
* waysintree <file_name> [ --delimiter DELIMETER ]

#### Arguments:
* parsetree  parse tree and output all ways
* generate create test files in current directory
* tests perform all tests

#### Options:
* --delimiter   delimiter between nodes in a way

#### Tests
##### Lib tests
* python3 -m unittest streelib/tests/test_lib.py -v

##### CMD util tests
* python3 -m unittest streelib/tests/test_cmd.py -v
