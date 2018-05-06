python3 setup.py bdist_wheel --universal && twine upload dist/*
rm -rf dist
rm -rf build
rm -fr *.egg-info
