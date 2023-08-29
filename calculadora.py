import os
from time import sleep
#Ferramenta utilizada para deixar a calculadora em looping:
while True:
    #Inserção do primeiro número
    num1 = int(input("..................Calculadora..................\n\n             Informe o 1º número: "))

    #Escolha da operação
    op = input("\n...................Operações...................\n\n                 (+) Adição\n                 (-) Subtração\n                 \n...............................................\n          Informe a operação desejada: ")

    #Inserção do segundo número
    num2 = int(input("\n...............................................\n             Informe o 2º número: "))

    #Adição
    if op == '+':
        result = num1 + num2
    
    #Subtração
    elif op == '-':
        result = num1 - num2
    
    #Impressão do resultado
    print('\n..................Resultado..................\n\n                 ' + str(num1) + ' ' + str(op) + ' ' + str(num2) + ' = ' + str(result))

    #Ferramentas utilizadas para esperar 2 segundos antes de limpar o console 
    sleep(2)
    os.system('cls') or None