# Importing all needed libraries.
import os
import graphviz as gz

# Add Graphviz to the PATH.
os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin'

# Setup the Grammar.
terminal_symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'j']
non_terminal_symbols = ['S', 'L', 'D']

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

# Make the link between the states
g_dict = {}
count = 0

for element in non_terminal_symbols:
    g_dict[element] = "q{}".format(count)
    count += 1

g_dict['Q'] = "q{}".format(count + 1)

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
for non_terminal in __set_of_productions:
    finite_automaton[g_dict[non_terminal]] = []
    for transition in __set_of_productions[non_terminal]:
        if len(transition) == 2:
            finite_automaton[g_dict[non_terminal]].append(
                (transition[0], g_dict[transition[1]]))
        else:
            finite_automaton[g_dict[non_terminal]].append((transition, 'Q'))


# DEBUG:
print('Finite Automaton:')
print(finite_automaton)


# Function to check if the given string belongs to the language L(G).
def is_accepted(string, adjacency_matrix, start_node='q0'):
    # Set the current node to the start one.
    current_node = start_node
    for c in string:
        if current_node == 'Q':
            return False

        for weight, adj_node in adjacency_matrix[current_node]:
            if c == weight:
                current_node = adj_node
                break
        else:
            return False

    # why NFA
    # Check if the last node is other then Empty.
    if current_node != 'Q':
        for prod in adjacency_matrix[current_node]:
            # If there exists a prod with the exact weight like the last character
            # and the adjacency node empty.
            if prod[0] == string[-1] and prod[1] == 'Q':
                return True

    # Return True or False if the current (last) node is the empty one.
    return current_node == 'Q'


# DEBUG:
print('Is accepted:', is_accepted('aade', finite_automaton))

# BONUS POINT:
# Ploting the FA Graph.

# Initialize the Graph.
G = gz.Digraph()
G.attr(rankdir='LR', size='8,5')

# Compute all nodes.
for element in finite_automaton:
    for weight, adj_node in finite_automaton[element]:
        G.attr('node', shape='circle')
        G.node(element)

        # Check for the empty node.
        if adj_node == 'Q':
            G.attr('node', shape='doublecircle')
            G.node(adj_node)
        else:
            G.attr('node', shape='circle')
            G.node(adj_node)

        # Add the labels.
        G.edge(element, adj_node, label=weight)

# Add the start arrow.
G.attr('node', shape='none')
G.node('')
G.edge('', 'q0')

# Show/Export the Graph.
# G.view()
