%include "io.inc"

SECTION .data
numero DD 5
fatorial DD 1

SECTION .text
global CMAIN
CMAIN:
    MOV EAX, 1
    MOV ECX, [numero]

calcula_fatorial:
    MUL ECX
    LOOP calcula_fatorial

    MOV [fatorial], EAX
    PRINT_UDEC 4, [fatorial]
    PRINT_CHAR 10

    MOV EAX, 0
    RET