# print("Estrutura Sequencial exercício 1\n")
# print("Alo mundo!!!\n\n")


# print("Estrutura Sequencial exercício 2\n")
# a = input("introduza um número:")
# print("O número introduzido foi :",a,"\n")


# print("Estrutura Sequencial exercício 3\n")
# num1 = input("Introduza o primeiro número: ")
# num2 = input("Introduza o segundo número: ")
# soma = float(num1) + float(num2)
# print("A soma dos dois número é: ",soma,"\n\n")


# print("Estrutura Sequencial exercício 4\n")
# bi1 = input("Introduza a primeira nota: ")
# bi2 = input("Introduza a segunda nota: ")
# bi3 = input("Introduza a terceira nota: ")
# bi4 = input("Introduza a quarta nota: ")
# bisoma = float(bi1) + float(bi2) + float(bi3) + float(bi4) 
# bimedia = bisoma /4
# print("A média é: ",bimedia,"\n\n")


# print("Estrutura Sequencial exercício 5\n")
# convM = input("intorduza os metros: ")
# convCM = float(convM) * 100
# print(convM," são ",convCM," centimetros\n\n")



# print("Estrutura Sequencial exercício 6\n")
import math
# raiocirc = input("Introduza o raio do circulo: ")
# areacirc = math.pi * float(raiocirc) * float(raiocirc)
# print(f"A area do circulo é {areacirc:g}")


#  Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
# print("Estrutura Sequencial exercício 7\n")
# ladoquad = input("introduza o tamanho do lado do quadrado: ")
# areaquad = float(ladoquad) * float(ladoquad)
# print(f"O dobro da área do quadrado é: {areaquad * 2:g}")


# print("Estrutura Sequencial exercício 8\n")
# remHora = input("introduza o valor hora: ")
# horasDia = input("introduza quantas horas trabalha por dia: ")
# horasTrab = float(horasDia) * 22
# remMes = float(remHora) * horasTrab
# print(f"O salário é: {remMes:g}""\n\n")


# print("Estrutura Sequencial exercício 9\n")
# grausF = input("Introduza a temperatura em Fahrenheit para transformar em ºC: ")
# grausC = 5 * ((float(grausF)-32)/9)
# print(f"{grausF}ºF são {grausC:g}ºC")


# print("Estrutura Sequencial exercício 10\n")
# print("Estrutura Sequencial exercício 9\n")
# grausC = input("Introduza a temperatura em Celsius para transformar em Fahrenheit: ")
# grausF = float(grausC) * 9/5 + 32
# print(f"{grausC}ºC são {grausF:g}ºF")


# print("Estrutura Sequencial exercício 11\n")
# int1 = int(input("Intorduza o primeiro número inteiro: "))
# int2 = int(input("Intorduza o segundo número inteiro: "))
# real1 = float(input("Intorduza um número real: "))
# primConta = (int1*2) / (int2/2)
# segConta = (3*int1)+(real1)
# terConta = real1 * real1 * real1
# print(f"a = {primConta}\n b = {segConta}\n c = {terConta}")


# print("Estrutura Sequencial exercício 12\n")
# altura1 = float(input("Intorduza a sua altura em metros: "))
# pesoIdeal = (72.7*altura1)-58
# print(f"O seu peso ideal é {pesoIdeal:g}")


# print("Estrutura Sequencial exercício 13\n")
# altura1 = float(input("Intorduza a sua altura em metros: "))
# pesoIdeal2 = 0
# gen = input("Introduza H para homem ou M para mulher: ")
# while gen != 'M' and gen != 'H':
#     gen = input(f"Introduziu {gen}, introduza H para homem ou M para mulher: ")

# if gen == 'M':
#     pesoIdeal2 = (62.1*altura1)-44.7
# if gen == 'H':
#     pesoIdeal2 = (72.7*altura1)-58

# print(f"Tendo em conta o seu sexo e a sua altura, o seu peso ideal é {pesoIdeal2}")


# print("Estrutura Sequencial exercício 14\n")
# pesoReg = 50  
# multaKgExc = 4
# excesso = 0
# pesoPesc = float(input("Qual a quantidade de peixe que pescou, em kilos: "))
# multa = 0

# if pesoPesc > pesoReg:
#     excesso = round((pesoPesc - pesoReg),0)
#     multa = excesso * multaKgExc
# if excesso != 0: print(f"Você pescou {excesso:g}kg acima do legalmente permitido, terá de pagar {multa:g}€ de multa")
# if excesso == 0: print(f"Você pescou {pesoPesc}kg")


# print("Estrutura Sequencial exercício 15\n")
# remHora1 = float(input("introduza o valor hora: "))
# horasMes1 = float(input("introduza quantas horas trabalhou este mês: "))
# remMes1 = remHora1 * horasMes1
# impostoRenda = 0.11
# inssImposto = 0.08
# sindicatoImposto = 0.05
# salarioLiquido = remMes1 - (remMes1 * (impostoRenda + inssImposto + sindicatoImposto))
# print(f"O salário liquido é: {salarioLiquido:g}€, descontou:\n{remMes1*impostoRenda:g}€ de IR\n{remMes1*inssImposto:g}€ de INSS\n{remMes1*sindicatoImposto:g}€ para o sindicato")




# print("Estrutura Sequencial exercício 16\n")
# areaPintar = float(input("Indique o tamanho em metros quadrados da área a pintar: "))
# precoLata = 80
# litrosNec = areaPintar / 3
# latas18 = litrosNec / 18

# print(f"São necessárias {math.ceil(latas18)} latas de 18L, por {math.ceil(latas18)*precoLata}€")



# print("Estrutura Sequencial exercício 17\n")
# areaPintar1 = float(input("Indique o tamanho em metros quadrados da área a pintar: "))
# precoLata = 80
# precoGalao = 25
# areaCoberta = 6
# lata = 18
# galao = 3.6
# litrosNec = math.ceil((areaPintar1 / areaCoberta) * 1.1)

# # caso 1
# # print(f"São necessárias {math.ceil(litrosNec/lata)} latas de 18L, por {math.ceil(litrosNec/lata)*precoLata}€")

# # caso 2
# # print(f"São necessário/os {math.ceil(litrosNec/galao)} galão/ões de 3.6L, por {math.ceil(litrosNec/galao)*precoGalao}€")

# # caso 3
# restolatas = (litrosNec % lata)
# latasNec = math.floor(litrosNec/lata)
# galaoNec = math.ceil(restolatas/galao)
# if galaoNec % 5 == 0: latasNec + 1 and galaoNec - 5
# print(f"Para pintar {areaPintar1:g}m2 são aconselhados {litrosNec:g} litros, sendo necessário/s {latasNec:g} lata/s e {galaoNec:g} galão/ões\ncom um custo de {(latasNec*precoLata)+(galaoNec*precoGalao):g}€")




# print ("Estrutura Sequencial exercício 18\n")
# tamanhoArq = float(input("Qual o tamanho do arquivo que deseja fazer download, em MB? "))
# velocidadeInt = float(input("Que velocidade de internet tem, em Mbps? "))
# tempo = (tamanhoArq / velocidadeInt) / 60


# print(f"Usando este link consegue descarregar o ficheiro em {tempo:g} minutos")