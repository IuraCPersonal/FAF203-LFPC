from typing import NewType

class Token:
    def __init__(self, Type, Value):
        self.Type = Type
        self.Value = Value

class Tokens:
    def __init__(self):
        self.tokens = {
            # {{ Main Tokens }}
            'ILLEGAL': 'ILLEGAL',
            'EOF'    : 'EOF',

            # {{ Ident and Values }}
            'IDENT'  : 'IDENT',
            'INT'    : 'INT',
            'DOUBLE' : 'DOUBLE',
            'STRING' : 'STRING',
            'CHAR'   : 'CHAR',

            # {{ Operators }}
            'ASSIGN'   : 'ASSIGN',
            'PLUS'     : 'PLUS',
            'MINUS'    : 'MINUS',
            'MULTIPLY' : 'MULTIPLY',
            'DIVIDE'   : 'DIVIDE',
            'LT'       : 'LT',
            'GT'       : 'GT',

            # {{ Delimiters }}
            'SEMICOLON' : 'SEMICOLON',
            'COMMA'     : 'COMMA',
            'LPAREN'    : 'LPAREN',
            'RPAREN'    : 'RPAREN',
            'LBRACE'    : 'LBRACE',
            'RBRACE'    : 'RBRACE',

            # {{ Boolean Operators }}
            'EQ'     : 'EQ',
            'NOT'    : 'NOT',
            'NOT_EQ' : 'NOT_EQ',
            'AND'    : 'AND',
            'OR'     : 'OR',
        }

        self.keywords = {
            'fn'    : 'FUNCTION',
            'let'   : 'LET',
            'true'  : 'TRUE',
            'false' : 'FALSE',
            'if'    : 'IF',
            'else'  : 'ELSE',
            'for'   : 'FOR',
            'while' : 'WHILE',
            'return': 'RETURN',
            'int'   : 'INT',
            'double': 'DOUBLE',
            'string': 'STRING',
            'char'  : 'CHAR',
        }

    def lookup_ident(self, ident):
        if ident in self.keywords:
            return self.keywords[ident]
        return 'IDENT'
