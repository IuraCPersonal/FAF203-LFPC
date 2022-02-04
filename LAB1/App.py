# Importing all needed libraries.
import os
import time
import random
import graphviz as gz

# Add Graphviz to the PATH.
os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin'

# Setup the Grammar.
terminal_symbols = set(['a', 'b', 'c', 'd', 'e', 'f', 'j'])
non_terminal_symbols = set(['S', 'L', 'D'])

# Setup the Set of Productions of Rules.
set_of_productions = tuple([
    ('S', 'aS'),
    ('S', 'bS'),
    ('S', 'cD'),
    ('S', 'dL'),
    ('S', 'e'),
    ('L', 'eL'),
    ('L', 'fL'),
    ('L', 'jD'),
    ('L', 'e'),
    ('D', 'eD'),
    ('D', 'd')
])

# Empty Dictionary.
__set_of_productions = {}

# Converting the Set of Productions into a Dictionary.
for nonterminal in set_of_productions:
    __set_of_productions[nonterminal[0]] = [production[1]
                                            for production in set_of_productions if production[0] == nonterminal[0]]

# DEBUG:
# print(__set_of_productions)

# Computing the Finite Automaton (FA).
finite_automaton = dict()
for production in __set_of_productions:
    for result in __set_of_productions[production]:
        if len(result) == 2:
            # random.randint(0, 100000) is just a dummy way to work around dublicates.
            finite_automaton.update(
                {(production, result[0], random.randint(0, 100000)): result[1]})
        else:
            finite_automaton.update(
                {(production, result, random.randint(0, 100000)): 'Q'})

# DEBUG:
print(finite_automaton)

# BONUS POINT:
# Ploting the FA Graph.

# Initialize the Graph.
G = gz.Digraph()
G.attr(rankdir='LR', size='8,5')

# Compute all nodes.
for element in finite_automaton:
    G.attr('node', shape='circle')
    G.node(element[0])

    # Check for the empty node.
    if finite_automaton[element] == 'Q':
        G.attr('node', shape='doublecircle')
        G.node(finite_automaton[element])
    else:
        G.attr('node', shape='circle')
        G.node(finite_automaton[element])

    # Add the labels.
    G.edge(element[0], finite_automaton[element], label=element[1])

# Show/Export the Graph.
G.view()
