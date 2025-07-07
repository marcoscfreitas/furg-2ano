def hanoi_resolver(n, origem, destino, auxiliar) :
    # Caso base: apenas 1 disco
    if n == 1 :
        print(f'Mova disco de {origem} para {destino}')
    else :
        # Passo 1: Mover n-1 discos para auxiliar
        hanoi_resolver(n-1, origem, auxiliar, destino)

        # Passo 2: Mover disco maior para destino
        print(f'Mova disco de {origem} para {destino}')

        # Passo 3: Mover n-1 discos do auxiliar para destino
        hanoi_resolver(n-1, auxiliar, destino, origem)

# Exemplo de Uso
hanoi_resolver(3, 'A','C','B')