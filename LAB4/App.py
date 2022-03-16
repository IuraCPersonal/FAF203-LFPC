from itertools import product

class Grammar:
    def __init__(self, grammar, terminal_symbols, non_terminal_symbols, start='S'):
        self.grammar = grammar
        self.terminal_symbols = terminal_symbols
        self.non_terminal_symbols = non_terminal_symbols
        self.start = start


    def __filter(self, word, to_replace, replacement):
        options = [(c,) if c != to_replace else (to_replace, replacement) for c in word]
        return ("".join(o) for o in product(*options))

    def check_start_symbol(self):
        """
        If the Start Symbol S occurs on some right side, create
            a new Start Symbol S' and a new Production S -> S'.
        """
        for production in self.grammar:
            if self.start in production[1]:
                self.grammar.insert(0, ['S*', 'S'])
                break


    def remove_empty(self):
        """
        Remove Null Productions.
        """
        nullable_variables = []
        for production in self.grammar:
            if 'Q' in production[1]:
                nullable_variables.append(production[0])

        # DEBUG:
        print(nullable_variables)

        grammar_cp = self.grammar.copy()
        for nullable in nullable_variables:
            for i in range(len(self.grammar)):
                if nullable in self.grammar[i][1]:
                    X = list(self.__filter(self.grammar[i][1], nullable, ''))
                    print('DEBUG:', X)
                    grammar_cp[i][1] = "|".join(X) if '' not in X else ''





    def remove_unit(self):
        """
        Remove Unit Productions.
        """
        pass


    def replace_productions(self):
        """
        Replace each Production A -> B1 ... Bn, where n > 2, with
            A -> B1C where C -> B2 ... Bn for all Productions having
            two or more Symbols on the right side.
        """
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
    ['C', 'Ba'],
]

grammar2 = [
    ['S', 'ABAC'],
    ['A', 'aA'],
    ['A', 'Q'],
    ['B', 'bB'],
    ['B', 'Q'],
    ['C', 'c']
]

terminal_symbols = ['a', 'b']
non_terminal_symbols = ['S', 'A', 'B', 'C', 'D']

CFG = Grammar(grammar2, terminal_symbols, non_terminal_symbols)

print(grammar2)

print("+---------------+")
CFG.check_start_symbol()
print(CFG.grammar)

print("+---------------+")
CFG.remove_empty()
print(CFG.grammar)

