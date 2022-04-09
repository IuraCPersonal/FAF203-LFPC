from Productions import *


class Grammar:
    def __init__(self, Language):
        self.Language = Language
        self.grammar = self.Language.create_dict()
        self.nullable_variables = set()
        print(self.grammar)

    def remove_empty_productions(self):
        for state in self.grammar:
            if Language.has_empty(state):
                self.nullable_variables.update(set(state))
                self.grammar[state].remove('Q')

    def update_empty_states(self):
        for state in self.grammar:
            self.grammar[state], count = Language.replace_nullables(self.grammar[state], self.nullable_variables)
            if count != 0:
                self.remove_empty_productions()

    def update_empty_productions(self):
        updates = []
        for nullable in self.nullable_variables:
            temp = []
            for state in self.grammar:
                temp.append(Language.filter(self.grammar[state], nullable))
            updates.append(temp)

        updated_grammar = {} 
        for idx, state in enumerate(self.grammar):
            updated_grammar[idx] = []

        for row in updates:
            for idx, update in enumerate(row):
                foo = [item for item in update]
                updated_row = [item for sublist in foo for item in sublist]
                updated_grammar[idx].append(updated_row)
       
        for idx, state in enumerate(self.grammar):
            self.grammar[state] = sorted(set().union(*updated_grammar[idx]))

        print(self.grammar)

    def remove_renamings(self):
        pass


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
        ['G', 'D'],
]

Language = Productions(grammar)
CNF = Grammar(Language)

CNF.remove_empty_productions()
CNF.update_empty_states()
CNF.update_empty_productions()
