from token import *

TOKENS = Tokens()

class Lexer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next_position = 0
        self.ch = ''
        self.__read_char()


    # Checks whether the given argument is a number.    
    def __is_digit(self, ch):
        return str(ch).isnumeric()
    

    # Checks whether the given argument is a letter.
    def __is_char(self, ch):
        return str(ch).isalpha()


    # Gives the next character and advance our position in the input string.
    def __read_char(self):
        if self.next_position >= len(self.source):
            self.ch = 0
        else:
            self.ch = self.source[self.next_position]

        self.position = self.next_position
        self.next_position += 1


    # “peek” ahead in the input and not move around in it.
    def __peek_char(self):
        if self.next_position >= len(self.source):
            return 0
        else:
            return self.source[self.next_position]


    # Reads in an identifier and advances our lexer’s positions until it encounters a non-digit.
    def __read_number(self):
        position = self.position
        while self.__is_digit(self.ch):
            self.__read_char()

        return self.source[position:self.position]


    # Reads in an identifier and advances our lexer’s positions until it encounters a non-letter-character.
    def __read_identifier(self):
        position = self.position
        while self.__is_char(self.ch):
            self.__read_char()

        return self.source[position:self.position]


    # Skips the whitespace character.
    def __eat_whitespace(self):
        try:
            while self.ch.isspace() :
                self.__read_char()
        except AttributeError:
            pass


    # Helps with initializing the tokens.
    def new_token(self, token_type, ch):
        return Token(token_type, str(ch))


    # Look at the current character under
    # examination (l.ch) and return a token depending on which character it is.
    def __next_token(self):
        tok = Token(None, None)

        self.__eat_whitespace()

        # Check the current character under examination.
        match self.ch:
            case 0:
                tok.Value = ''
                tok.Type = TOKENS.tokens['EOF']
            # {{ Operators }}
            case '=':
                if self.__peek_char() == '=':
                    ch = self.ch
                    self.__read_char()
                    tok = Token(TOKENS.tokens['EQ'], ch + self.ch)
                else:
                    tok = self.new_token(TOKENS.tokens['ASSIGN'], self.ch)
            case '+':
                tok = self.new_token(TOKENS.tokens['PLUS'], self.ch)
            case '-':
                tok = self.new_token(TOKENS.tokens['MINUS'], self.ch)
            case '*':
                tok = self.new_token(TOKENS.tokens['MULTIPLY'], self.ch)
            case '/':
                tok = self.new_token(TOKENS.tokens['DIVIDE'], self.ch)
            case '<':
                tok = self.new_token(TOKENS.tokens['LT'], self.ch)
            case '>':
                tok = self.new_token(TOKENS.tokens['GT'], self.ch)
            # {{ Boolean Operators }}
            case '!':
                if self.__peek_char() == '=':
                    ch = self.ch
                    self.__read_char()
                    tok = Token(TOKENS.tokens['NOT_EQ'], ch + self.ch)
                else:
                    tok = self.new_token(TOKENS.tokens['NOT'], self.ch)
            case '&':
                if self.__peek_char() == '&':
                    self.__read_char()
                    tok = Token(TOKENS.tokens['AND'], self.ch + self.ch)
                else:
                    tok = self.new_token(TOKENS.tokens['ILLEGAL'], self.ch)
            case '|':
                if self.__peek_char() == '|':
                    self.__read_char()
                    tok = Token(TOKENS.tokens['OR'], self.ch + self.ch)
                else:
                    tok = self.new_token(TOKENS.tokens['ILLEGAL'], self.ch)
            # {{ Delimiters }}
            case ',':
                tok = self.new_token(TOKENS.tokens['COMMA'], self.ch)
            case ';':
                tok = self.new_token(TOKENS.tokens['SEMICOLON'], self.ch)
            case '(':
                tok = self.new_token(TOKENS.tokens['LPAREN'], self.ch)
            case ')':
                tok = self.new_token(TOKENS.tokens['RPAREN'], self.ch)
            case '{':
                tok = self.new_token(TOKENS.tokens['LBRACE'], self.ch)
            case '}':
                tok = self.new_token(TOKENS.tokens['RBRACE'], self.ch)
            case '"':
                self.__read_char()
                tok = self.new_token(TOKENS.tokens['STRING'], self.__read_identifier())
            # {{ Default Case }}
            case _:
                if self.__is_char(self.ch):
                    tok.Value = self.__read_identifier()
                    tok.Type = TOKENS.lookup_ident(tok.Value)
                    return tok
                elif self.__is_digit(self.ch):
                    tok.Type = TOKENS.tokens['INT']
                    tok.Value = self.__read_number()
                    return tok
                else:
                    tok = self.new_token(TOKENS.tokens['ILLEGAL'], self.ch)

        # Return a token depending on which character it is.
        self.__read_char()
        return tok
    

    # Returns the tokens for the input code.
    def get_tokens(self):
        tokens = []
        current_token = self.__next_token()
        tokens.append(tuple([current_token.Type, current_token.Value]))

        while current_token.Type != TOKENS.tokens['EOF']:
            current_token = self.__next_token()
            tokens.append(tuple([current_token.Type, current_token.Value]))

        return tokens

