// lexer/lexer.go

package lexer

import (
	"lab3/token"
)

// Define our Lexer struct
type Lexer struct {
	input        string
	position     int
	nextPosition int
	ch           byte
}

//  Function to return *Lexer
func New(input string) *Lexer {
	l := &Lexer{input: input}
	l.readChar()
	return l
}

// Checks whether the given argument is a number.
func isDigit(ch byte) bool {
	return '0' <= ch && ch <= '9'
}

// Checks whether the given argument is a letter.
func isChar(ch byte) bool {
	return 'a' <= ch && ch <= 'z' || 'A' <= ch && ch <= 'Z' || ch == '_'
}

// Gives the next character and advance our position in the input string.
func (l *Lexer) readChar() {
	// Checks it reached the end of the string.
	if l.nextPosition >= len(l.input) {
		// 0 = "NUL" in the ASCII table.
		l.ch = 0
	} else {
		// Sets ch to the next character.
		l.ch = l.input[l.nextPosition]
	}

	// Update positions.
	l.position = l.nextPosition
	l.nextPosition += 1
}

// “peek” ahead in the input and not move around in it.
func (l *Lexer) peekChar() byte {
	if l.nextPosition >= len(l.input) {
		return 0
	} else {
		return l.input[l.nextPosition]
	}
}

// Reads in an identifier and advances our lexer’s positions until it encounters a non-letter-character.
func (l *Lexer) readNumber() string {
	position := l.position
	for isDigit(l.ch) {
		l.readChar()
	}
	return l.input[position:l.position]

}

// Reads in an identifier and advances our lexer’s positions until it encounters a non-letter-character.
func (l *Lexer) readIdentifier() string {
	position := l.position
	for isChar(l.ch) {
		l.readChar()
	}
	return l.input[position:l.position]
}

// Skips the whitespace character.
func (l *Lexer) eatWhitespace() {
	for l.ch == ' ' || l.ch == '\t' || l.ch == '\n' || l.ch == '\r' {
		l.readChar()
	}
}

// Helps with initializing the tokens.
func newToken(tokenType token.TokenType, ch byte) token.Token {
	return token.Token{Type: tokenType, Value: string(ch)}
}

// Look at the current character under
// examination (l.ch) and return a token depending on which character it is.
func (l *Lexer) nextToken() token.Token {
	var tok token.Token

	l.eatWhitespace()

	// Check the current character under examination.
	switch l.ch {
	case 0:
		tok.Value = ""
		tok.Type = token.EOF
	// Operators.
	case '=':
		// Check for the EQ (==) token.
		if l.peekChar() == '=' {
			ch := l.ch
			l.readChar()
			tok = token.Token{Type: token.EQ, Value: string(ch) + string(l.ch)}
		} else {
			// It's just the assign token.
			tok = newToken(token.ASSIGN, l.ch)
		}
	case '+':
		tok = newToken(token.PLUS, l.ch)
	case '-':
		tok = newToken(token.MINUS, l.ch)
	case '*':
		tok = newToken(token.MULTIPLY, l.ch)
	case '/':
		tok = newToken(token.DIVIDE, l.ch)
	case '<':
		tok = newToken(token.LT, l.ch)
	case '>':
		tok = newToken(token.GT, l.ch)
	// Boolean Operators
	case '!':
		// Check for the NOT_EQ (!=) token.
		if l.peekChar() == '=' {
			ch := l.ch
			l.readChar()
			tok = token.Token{Type: token.NOT_EQ, Value: string(ch) + string(l.ch)}
		} else {
			// Just the negation NOT token.
			tok = newToken(token.NOT, l.ch)
		}
	case '&':
		if l.peekChar() == '&' {
			ch := l.ch
			l.readChar()
			tok = token.Token{Type: token.AND, Value: string(ch) + string(l.ch)}
		} else {
			tok = newToken(token.ILLEGAL, l.ch)
		}
	case '|':
		if l.peekChar() == '|' {
			ch := l.ch
			l.readChar()
			tok = token.Token{Type: token.OR, Value: string(ch) + string(l.ch)}
		} else {
			tok = newToken(token.ILLEGAL, l.ch)
		}
	// Delimiters
	case ',':
		tok = newToken(token.COMMA, l.ch)
	case ';':
		tok = newToken(token.SEMICOLON, l.ch)
	case '(':
		tok = newToken(token.LPAREN, l.ch)
	case ')':
		tok = newToken(token.RPAREN, l.ch)
	case '{':
		tok = newToken(token.LBRACE, l.ch)
	case '}':
		tok = newToken(token.RBRACE, l.ch)
	default:
		if isChar(l.ch) {
			tok.Value = l.readIdentifier()
			tok.Type = token.LookupIdent(tok.Value)
			return tok
		} else if isDigit(l.ch) {
			tok.Type = token.INT
			tok.Value = l.readNumber()
			return tok
		} else {
			tok = newToken(token.ILLEGAL, l.ch)
		}
	}

	l.readChar()
	// Return a token depending on which character it is
	return tok
}

// Returns the tokens for the input code.
func (l *Lexer) GetTokens() []token.Token {
	var tokens []token.Token
	currentToken := l.nextToken()
	tokens = append(tokens, currentToken)

	for currentToken.Type != token.EOF {
		currentToken = l.nextToken()
		tokens = append(tokens, currentToken)
	}

	return tokens
}
