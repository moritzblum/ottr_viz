from setuptools import setup

install_requires = [
    'antlr4-python3-runtime==4.9.2',
    'networkx==2.5',
    'pygraphviz==1.6'
]

setup(
    name='ottr_viz',
    description='Collection of scripts for visualizations of OTTR data.',
    author='Moritz Blum',
    author_email='mblum@techfak.uni-bielefeld.de',
    python_requires='>=3.6',
    install_requires=install_requires,
)