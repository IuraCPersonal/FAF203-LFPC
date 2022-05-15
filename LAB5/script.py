from LL1 import LL1

grammar = {
    'S': ['Bc', 'BcdC'],
    'C': ['Ae'],
    'A': ['fD'],
    'D': ['bfD', 'X'],
    'B': ['aE'],
    'E': ['baE', 'X']
}

terminals = ['a', 'b', 'c', 'd', 'e', 'f']
non_terminals = ['S', 'A', 'B', 'C', 'D', 'E']
empty, start = 'X', 'S'

language = "abacdfbfe"

LL1 = LL1(grammar, terminals, non_terminals, start, empty)
LL1.main(language)
