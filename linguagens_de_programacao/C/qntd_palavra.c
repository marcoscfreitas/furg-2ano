#include <stdio.h>
#include <string.h>

int main() {
    char frase[200];
    char palavra[50];
    int i, j, cont = 0;
    int tamFrase, tamPalavra;

    printf("Digite a frase:\n");
    gets(frase);

    printf("Digite a palavra:\n");
    gets(palavra);

    tamFrase = strlen(frase);
    tamPalavra = strlen(palavra);

    for (i = 0; i <= tamFrase - tamPalavra; i++) {
        int igual = 1;
        for (j = 0; j < tamPalavra; j++) {
            if (frase[i + j] != palavra[j]) {
                igual = 0;
                break;
            }
        }
        if (igual) {
            cont++;
        }
    }

    printf("A palavra '%s' ocorre %d vezes na frase.\n", palavra, cont);

    return 0;
}
