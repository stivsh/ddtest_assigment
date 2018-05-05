python3 setup-waysintree.py bdist_wheel --universal && twine upload dist/*
rm -rf dist
rm -rf build
rm -rf my_simple_tree_library.egg-info
