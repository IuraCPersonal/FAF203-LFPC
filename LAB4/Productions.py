import itertools


class Productions:
    def __init__(self, grammar, empty='Q'):
        self.grammar = grammar
        self.empty = empty

        self.get_symbols()
        self.grammar_dict = dict()

    
    def get_symbols(self):
        self.res = list(set([i for j in self.grammar for i in j]))
        self.res = list(set([i for j in self.res for i in j]))
        return self.res

    
    def get_non_terminals(self):
        return sorted([terminal for terminal in self.res if terminal.isupper() and terminal != self.empty])


    def get_terminals(self):
        return sorted([terminal for terminal in self.res if terminal.islower()])


    def create_dict(self):
        for production in self.grammar:
           self.grammar_dict[production[0]] = [
                prod[1] for prod in self.grammar
                    if prod[0] == production[0]] 

        return self.grammar_dict


    def has_empty(self, target):
        for productions in self.grammar_dict[target]:
            if 'Q' in productions:
                return True
        return False


    def filter(self, production, nullable):
        options = [(c,) if c != nullable else (nullable, '') for c in production]
        return list("".join(o) for o in itertools.product(*options))


    def replace_nullables(self, productions, nullables):
        for prod in productions:
            for nullable in nullables:
                if nullable in prod:
                    pass
    













