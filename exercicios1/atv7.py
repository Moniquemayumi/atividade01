
numero = int(input("Digite um número ímpar: "))

if numero % 2 == 0:
    print("O número digitado não é ímpar. Tente novamente com um número ímpar.")
else:

    numero_anterior = numero - 2
    numero_proximo = numero + 2


    quadrado_anterior = numero_anterior ** 2
    quadrado_proximo = numero_proximo ** 2

    diferenca = quadrado_anterior - quadrado_proximo

    print(f"A diferença entre o quadrado do número ímpar anterior ({quadrado_anterior}) e o próximo ({quadrado_proximo}) é {diferenca}.")
