from setuptools import setup

setup(
    name='my-simple-tree-library',
    version='0.1',
    description='test work for job assigment. Tree alg.',
    url='https://github.com/stivsh/ddtest_assigment',
    author='Sorokin Stepan',
    author_email='stivsh@gmail.com',
    license='NO',
    packages=['streelib'],
    install_requires=['networkx','docopt', 'matplotlib',
                        'pydot', 'scipy', 'numpy'],
    entry_points={
    'console_scripts': [
        'waysintree=streelib:main',
    ],
},
)
