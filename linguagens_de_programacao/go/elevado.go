package main

import (
	"fmt"
)

func main() {
	var x, n int
	fmt.Print("digite a base (x): ")
	fmt.Scan(&x)
	fmt.Print("digite o expoente (n): ")
	fmt.Scan(&n)

	resultado := 1
	for i := 0; i < n; i++ {
		resultado *= x
	}
	fmt.Printf("%d elevado a %d é %d\n", x, n, resultado)
}
