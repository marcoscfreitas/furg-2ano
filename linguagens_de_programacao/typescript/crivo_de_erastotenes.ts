function crivoDeEratostenes(n: number): number[] {
    const ehPrimo: boolean[] = Array.from({ length: n + 1 }, () => true);
    ehPrimo[0] = false;
    ehPrimo[1] = false;

    for (let p = 2; p * p <= n; p++) {
        if (ehPrimo[p]) {
            for (let i = p * p; i <= n; i += p) {
                ehPrimo[i] = false;
            }
        }
    }

    const primos: number[] = [];
    for (let i = 2; i <= n; i++) {
        if (ehPrimo[i]) {
            primos.push(i);
        }
    }

    return primos;
}

// Exemplo de uso, primos até 30
const limite: number = 30;
const primos: number[] = crivoDeEratostenes(limite);
console.log(`Primos até ${limite}: ${primos.join(", ")}`);
