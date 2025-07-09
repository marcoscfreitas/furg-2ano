def inverterString(texto) :
    if len(texto) <= 1 :
        return texto
    return inverterString(texto[1:]) + texto[0]

texto = 'ABC'
saida = inverterString(texto)

print(saida)

# solução alternativa
def inverterString(string,pos=0) :
    if pos >= len(string) :
        return ''
    else :
        return inverterString(string,pos+1) + string[pos]

print(inverterString('abcd'))

'''
return ''
return inverterString('abcd',4) + d => '' + d
return inverterString('abcd',3) + c => d + c = dc
return inverterString('abcd',2) + b => dc + b = dcb
return inverterString('abcd',1) + a => dcb + a = dcba
'''