package main

import (
	"fmt"
	"io/ioutil"
	"lab3/lexer"
	"lab3/token"
	"log"
)

func main() {

	var tokens = scanFile("script.txt")

	for i, token := range tokens {
		fmt.Println(i, token)
	}
}

func scanFile(path string) []token.Token {
	file, err := ioutil.ReadFile(path)
	if err != nil {
		log.Fatal(err)
	}

	code := string(file)
	l := lexer.New(code)
	return l.GetTokens()
}
