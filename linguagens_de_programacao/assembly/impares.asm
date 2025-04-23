%include "io.inc"

SECTION .data
n DD 5
contador DD 0
numero DD 1

SECTION .text
global CMAIN
CMAIN:
    MOV ECX, [n]
    MOV EAX, [numero]

loop_impares:
    CMP [contador], ECX
    JGE fim

    PRINT_UDEC 4, EAX
    PRINT_CHAR 10

    ADD EAX, 2
    INC DWORD [contador]

    JMP loop_impares

fim:
    MOV EAX, 0
    RET