# 1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    inputDoUtilizador = int(input("Atribua uma nota de 1 a 10: "))                   
                    
    if inputDoUtilizador > 10 or inputDoUtilizador < 0 :
        print("O número escolhido é inválido!! /n")
    else:
        print(f"Atribuido o valor: {inputDoUtilizador}")
        break                
