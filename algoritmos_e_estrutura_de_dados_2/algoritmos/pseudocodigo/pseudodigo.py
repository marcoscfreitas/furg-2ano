op1_str = ''
op2_str = ''
op1 = [0,0,0,0]
op2 = [0,0,0,0]
res = [0,0,0,0,0,0,0,0]
aux_mult = 0
sobe = 0
res_aux = [0,0,0,0,0]

op1_str = input('informe o primeiro operador: ')
op2_str = input('informe o segundo operador: ')

for i in range(4) :
    op1[i] = int(op1_str[i])
    op2[i] = int(op2_str[i])
    print(i)

for i in range(3, -1, -1) :
    sobe = 0
    for j in range(3, -1, -1) :
        aux_mult = op1[j] * op2[i] + sobe
        res_aux[j+1] = aux_mult%10 #
        sobe = aux_mult//10
    res_aux[0] = sobe
    sobe = 0

    for j in range(4, -1, -1) :
        aux_soma = res_aux[j] +res[i+j] + sobe
        res[i+j] = aux_soma%10
        sobe = aux_soma//10

print(res)