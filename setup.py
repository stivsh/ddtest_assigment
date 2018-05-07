from setuptools import setup

setup(
    name='the_simple_tree_lib',
    version='2.1.1',
    description='test work for job assigment. Tree alg.',
    url='https://github.com/stivsh/ddtest_assigment',
    author='Sorokin Stepan',
    author_email='stivsh@gmail.com',
    license='NO',
    packages=['streelib'],
    install_requires=['docopt'],
    entry_points={
        'console_scripts': [
            'waysintree=streelib:main', ],
            },
)
