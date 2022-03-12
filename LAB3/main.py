from lexer import Lexer

def scan_file(file):
    f = open(file)

    my_lexer = Lexer(f.read())
    tokens = my_lexer.get_tokens()
    for tok in tokens:
        print(tok)

if __name__ == '__main__':
    scan_file('script.txt')
