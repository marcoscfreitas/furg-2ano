package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Print("digite um número inteiro positivo: ")
	fmt.Scan(&n)

	fmt.Println("os", n, "primeiros naturais ímpares são:")
	count := 0
	num := 1
	for count < n {
		fmt.Print(num, " ")
		num += 2
		count++
	}
	fmt.Println()
}
