package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Print("digite um número inteiro positivo: ")
	fmt.Scan(&n)

	if n < 2 {
		fmt.Println("não é primo.")
		return
	}

	primo := true
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			primo = false
			break
		}
	}

	if primo {
		fmt.Println("é primo.")
	} else {
		fmt.Println("não é primo.")
	}
}
