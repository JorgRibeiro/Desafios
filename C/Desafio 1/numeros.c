#include <stdio.h>

int *tranformar(int numero);

int main(void)
{

    int numero;
    scanf("%d", &numero);

    tranformar(numero);

    return 0;
}

int *tranformar(int numero)
{

    int vetor[0];
    char string[30];
    int i;

    sprintf(string, "%d", numero);
     printf("%s", string);
  
    if (numero == 0)
    {
        return 0;
    }
    else
    {
        for (i = 0; string[i] != '\n'; i++)
        {
            vetor[i] = string[i];
        }
    }
    for (int j = 0; j < i; j++)
    {
        printf("[%d]", vetor[j]);
    }

    return vetor;
}