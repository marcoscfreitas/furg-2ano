package main

import (
	"fmt"
)

func main() {
	var f float64
	fmt.Print("digite a temperatura em Fahrenheit: ")
	fmt.Scan(&f)

	c := (f - 32) * 5 / 9
	fmt.Printf("temperatura em Celsius: %.2f\n", c)
}
