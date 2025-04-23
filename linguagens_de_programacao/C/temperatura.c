#include <stdio.h>

int main()
{
    int fahren, celcius;

    printf("digite uma temperatura em farenheidt: ");
    scanf("%d", &fahren);
    
    celcius = ((fahren - 32)*5)/9;
    
    printf("%d graus farenheidt em celcius é %d graus", fahren, celcius);
    return 0;
}