#include <stdio.h>

int main()
{
    int num, cont, aux;

    printf("digite o número de ímpares: ");
    scanf("%d", &num);
    printf("os primeiros ímpares são: ");
    
    aux = 0;
    
    for (cont = 0; aux != num; cont++ )
        if (cont%2 != 0) {
            printf("%d ", cont);
            aux++;
        }
    return 0;
}