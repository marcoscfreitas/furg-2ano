def inverterString(texto) :
    if len(texto) <= 1 :
        return texto
    return inverterString(texto[1:]) + texto[0]

texto = 'ABC'
saida = inverterString(texto)

print(saida)