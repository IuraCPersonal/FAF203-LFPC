// token/token.go

package token

// Define our TokenType type
type TokenType string

// Define our Token struct
type Token struct {
	Type  TokenType
	Value string
}

// Define our tokens
const (
	// Main
	ILLEGAL = "ILLEGAL"
	EOF     = "EOF"

	// Identifiers and Values
	IDENT  = "IDENT"
	INT    = "INT"
	DOUBLE = "DOUBLE"
	STRING = "STRING"
	CHAR   = "CHAR"

	// Operators
	ASSIGN   = "ASSIGN"   // =
	PLUS     = "PLUS"     // +
	MINUS    = "MINUS"    // -
	MULTIPLY = "MULTIPLY" // *
	DIVIDE   = "DIVIDE"   // /
	LT       = "LT"       // <
	GT       = "GT"       // >

	// Boolean Operators
	NOT    = "NOT"    // !
	EQ     = "EQ"     // ==
	NOT_EQ = "NOT_EQ" // !=
	AND    = "AND"    // &&
	OR     = "OR"     // ||

	// Delimiters
	COMMA     = "COMMA"     // ,
	SEMICOLON = "SEMICOLON" // ;
	LPAREN    = "LPAREN"    // (
	RPAREN    = "RPAREN"    // )
	LBRACE    = "LBRACE"    // {
	RBRACE    = "RBRACE"    // }
	QUOTE     = "QUOTE"     // "

	// Keywords
	FUNCTION = "FUNCTION"
	LET      = "LET"
	TRUE     = "TRUE"
	FALSE    = "FALSE"
	IF       = "IF"
	ELSE     = "ELSE"
	FOR      = "FOR"
	WHILE    = "WHILE"
	RETURN   = "RETURN"
)

// The correct TokenType for the token literal
var Keywords = map[string]TokenType{
	"fn":     FUNCTION,
	"let":    LET,
	"true":   TRUE,
	"false":  FALSE,
	"if":     IF,
	"else":   ELSE,
	"for":    FOR,
	"while":  WHILE,
	"return": RETURN,
	"int":    INT,
	"float":  DOUBLE,
	"string": STRING,
	"char":   CHAR,
}

// Checks the Keywords table to see whether the given identifier is in fact a keyword.
func LookupIdent(ident string) TokenType {
	if tok, ok := Keywords[ident]; ok {
		return tok
	}
	return IDENT
}
