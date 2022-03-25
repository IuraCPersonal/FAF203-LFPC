from Productions import *


class Grammar:
    def __init__(self, Language):
        self.Language = Language
        self.grammar = self.Language.create_dict()
        self.nullable_variables = set()

    def remove_empty_productions(self):
        for state in self.grammar:
            if Language.has_empty(state):
                self.nullable_variables.update(set(state))
                self.grammar[state].remove('Q')

        print(self.grammar)
        # for productions in self.grammar.values():
        #     Language.replace_nullables(productions, self.nullable_variables)        

                


grammar = [
        ['S', 'aB'],
        ['S', 'bA'],
        ['S', 'A'],
        ['A', 'B'],
        ['A', 'AS'],
        ['A', 'bBAB'],
        ['A', 'b'],
        ['B', 'b'],
        ['B', 'bS'],
        ['B', 'aD'],
        ['B', 'Q'],
        ['D', 'AA'],
        ['C', 'Ba'],
]

Language = Productions(grammar)
CNF = Grammar(Language)

CNF.remove_empty_productions()
