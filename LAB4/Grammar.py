from Productions import *
import itertools


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

            for x in self.grammar[state]:
                if x == '':
                    self.nullable_variables.update(set(state))
                    self.grammar[state].remove('')

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

    def foo(self):
        for i in range(5):
            self.update_empty_productions()
            self.remove_empty_productions()

    def remove_renamings(self):
        grammar_copy = self.grammar.copy()
        for state in self.grammar:
            for transition in self.grammar[state]:
                if transition in self.grammar and transition != state:
                    index = self.grammar[state].index(transition)
                    temp = list(itertools.chain(self.grammar[state], self.grammar[transition]))
                    grammar_copy[state] = temp 

        for state in grammar_copy:
            self.grammar[state] = list(set(grammar_copy[state]))

    def remove_inaccessible(self):
        states = [state for state in self.grammar]
        inaccessible = []
        for state in states:
            accessible = False
            for productions in self.grammar.values():
                for prod in productions:
                    if state in prod:
                        accessible = True
                        break

            if not accessible:
                inaccessible.append(state)

        for ics in inaccessible:
            self.grammar.pop(ics)

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
]

Language = Productions(grammar)
CNF = Grammar(Language)

CNF.remove_empty_productions()
CNF.update_empty_states()
CNF.update_empty_productions()
CNF.foo()
CNF.remove_renamings()
CNF.remove_inaccessible()

print("DEBUG")
for key in CNF.grammar:
    print(key, ":", CNF.grammar[key])
