#include <stdio.h>

int main()
{
    int num, aux, div_cont;
    
    printf("digite um número para verificar se é primo: ");
    scanf("%d", &num);
    
    div_cont = 0;
    
    for (aux = num; aux > 0; aux--)
        if (num%aux == 0) {
            div_cont+=1;
        }
        
    if (div_cont != 2) {
        printf("o numero %d não é primo", num);
    }
    else {
        printf("o numero %d é primo", num);
    }
    return 0;
}