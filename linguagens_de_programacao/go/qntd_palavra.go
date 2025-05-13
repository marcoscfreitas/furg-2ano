package main

import (
	"fmt"
	"strings"
)

func main() {
	var frase, palavra string

	fmt.Print("digite a frase: ")
	fmt.Scanln(&frase)
	fmt.Print("digite a palavra a procurar: ")
	fmt.Scanln(&palavra)

	frase = strings.ToUpper(frase)
	palavra = strings.ToUpper(palavra)

	contador := 0
	for i := 0; i <= len(frase)-len(palavra); i++ {
		if frase[i:i+len(palavra)] == palavra {
			contador++
		}
	}

	fmt.Printf("a palavra %s ocorre %d vezes na frase.\n", palavra, contador)
}
