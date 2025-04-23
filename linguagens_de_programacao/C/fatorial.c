#include <stdio.h>

int main()
{
    int num, cont, resultado;

    printf("digite um número para ver sua fatorial: ");
    scanf("%d", &num);
    
    resultado = 1;
    
    for(cont = num; cont != 0; cont--)
        resultado = resultado*cont;
        
    printf("%d", resultado);

    return 0;
}