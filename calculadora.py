import os
from time import sleep
#Ferramenta utilizada para deixar a calculadora em looping:
while True:
    #Inserção do primeiro número
    num1 = int(input("..................Calculadora..................\n\n             Informe o 1º número: "))

    #Escolha da operação
    op = input("\n...................Operações...................\n\n                 (+) Adição\n                 (-) Subtração\n                 (*) Multiplicação\n                 (/) Divisão\n                 (&) Potenciação\n                 (#) Radiciação\n...............................................\n          Informe a operação desejada: ")

    #Estrutura para identificar se o usuário tenha escolhido a opção "(#) Radiciação"
    if op == '#':
        result = num1 ** 0.5
        print('\n..................Resultado..................\n\n                     √' + str(result))
        sleep(2)
        os.system('cls') or None

    #Estrutura para as demais operações
    else:
        #Inserção do segundo número
        num2 = int(input("\n...............................................\n             Informe o 2º número: "))

        #Adição
        if op == '+':
            result = num1 + num2
        
        #Subtração
        elif op == '-':
            result = num1 - num2
        
        #Multiplicação
        elif op == '*':
            result = num1 * num2

        #Divisão
        elif op == '/':
            if num2 == 0:
                result = 'Impossível!'
            else:
                result = num1 / num2
        
        #Potenciação
        elif op == '&':
            result = num1 ** num2
        
        #Impressão do resultado
        print('\n..................Resultado..................\n\n                 ' + str(num1) + ' ' + str(op) + ' ' + str(num2) + ' = ' + str(result))

        #Ferramentas utilizadas para esperar 2 segundos antes de limpar o console 
        sleep(2)
        os.system('cls') or None