import funcoes

while True:
    # funcoes.exibir_menu()
    escolha = input("Digite o número da opção desejada (ou 's' para sair): ")
    
    if escolha.isdigit() and 1 <= int(escolha) <= 28:
        print(f"Você escolheu a opção {escolha}.")
        match escolha:
            case '1':
                print(escolha)
                numEsc1 = input("escolha o primeiro numero: ")
                numEsc2 = input("escolha o segundo numero: ")
                    
                if numEsc1 > numEsc2:
                        print(f"O maior número é {numEsc1}")
                else:  print(f"O maior número é {numEsc2}")
            
            case '2':
                print(escolha)
                positivoNegativo = float(input("digite um número: "))
                if positivoNegativo < 0:
                    print(f"o número {positivoNegativo:g} é negativo")
                elif positivoNegativo > 0:
                    print(f"o número {positivoNegativo:g} é positivo")
                else: print(f"o número {positivoNegativo:g} é zero")
                
            case '3':
                print(escolha)
                while True:
                    sexoEscolhido = input("Escreva 'M' para mulher ou 'H' para homem : ")
                    match sexoEscolhido :
                        case 'M' :
                            print("Mulher")
                            break
                        case 'H':
                            print("Homem")
                            break
                        case other:
                            print("Sexo inválido\n")

            case '4':
                print(escolha)
                while True:
                    vogalConsoante = input("Escolha uma letra do alfabeto ou enter para sair: ").lower()
                    if not vogalConsoante:
                        print("Saindo da função!")
                        break
                    if vogalConsoante.isalpha():
                        if vogalConsoante in 'aeiou':
                            print(f'A letra "{vogalConsoante}" é uma vogal.')
                        else:
                            print(f'A letra "{vogalConsoante}" é uma consoante.')
                    else:
                        print('Por favor, digite uma letra do alfabeto.')
                        
            case '5':
                print(escolha)
                nota1 = float(input("Qual a primeira nota do aluno? "))
                nota2 = float(input("Qual a segunda nota do aluno? "))
                media = (nota1 + nota2) / 2
                if media < 7:
                    print(f"A sua média foi de {media:g}, está Reprovado!!!")
                elif 10 < media >= 7:
                    print(f"A sua média foi de {media:g}, está Aprovado!!!")
                else: print(f"A sua média foi de {media:g}, está Aprovado com distinção!!!")
                
            case '6':
                print(escolha)
                num1 = float(input("Qual o primeiro número a comparar: "))
                num2 = float(input("Qual o segundo número a comparar: "))
                num3 = float(input("Qual o terceiro número a comparar: "))
                
                if num1 <= num2:
                    num1 = num2
                if num3 >= num1:
                    print(f"O maior número dos inseridos é {num3}")
                else:
                    print(f"O maior número dos inseridos é {num1}")
            case '7':
                num1 = float(input("Qual o primeiro número a comparar: "))
                num2 = float(input("Qual o segundo número a comparar: "))
                num3 = float(input("Qual o terceiro número a comparar: "))
                num1menor = num1
                
                if num1menor <= num2:
                    if num1menor <= num3:
                        print(f"O menor número é {num1}")
                    if num3 < num1menor:
                        print(f"O menor número é {num3}")
                if num2 < num1:
                    if num2 <= num3:
                        print(f"O menor número é {num2}")
                    if num3 < num2:
                        print(f"O menor número é {num3}")             
                if num1 <= num2:
                    num1 = num2    
                if num3 >= num1:
                    print(f"O maior número dos inseridos é {num3}")
                else:
                    print(f"O maior número dos inseridos é {num1}")
                
            case '8':
                print(escolha)
                num1 = float(input("Qual o preço do primeiro artigo a comparar: "))
                num2 = float(input("Qual o preço do segundo artigo a comparar: "))
                num3 = float(input("Qual o preço do terceiro artigo a comparar: "))
                
                if num1 <= num2:
                    if num1 <= num3:
                        print(f"Deve adquirir o primeiro artigo por {num1}€")
                    if num3 < num1:
                        print(f"Deve adquirir o terceiro artigo por {num3}€")
                if num2 < num1:
                    if num2 <= num3:
                        print(f"Deve adquirir o segundo artigo por {num2}€")
                    if num3 < num2:
                        print(f"Deve adquirir o terceiro artigo por {num3}€")         
            case '9':
                print(escolha)
                num1 = float(input("Qual o primeiro número: "))
                num2 = float(input("Qual o segundo número: "))
                num3 = float(input("Qual o terceiro número: "))
                if num1 >= num2 and num1 >= num3:
                    if num2 >= num3:
                        print(f"{num1} > {num2} > {num3}")
                    else :
                        print(f"{num1} > {num3} > {num2}")
                elif num2 >= num1 and num2 >= num3:
                    if num1 >= num3:
                        print(f"{num2} > {num1} > {num3}")
                    else:
                        print(f"{num2} > {num3} > {num1}")
                elif num3 >= num1:
                    if num1 >= num2:
                        print(f"{num3} > {num1} > {num2}")
                    else:
                        print(f"{num3} > {num2} > {num1}")

            case '10':
                print(f"{escolha} é repetido")
            case '11':
                print(f"{escolha} é repetido")
            case '12':
                print(f"{escolha} é repetido")
            case '13':
                print(escolha)
                while True:
                    diaSemana = input("Escreva um número entre 1 e 7: ")
                    match diaSemana:
                        case '1':
                            print("Segunda-feira =)")
                            break
                        case '2':
                            print("Terça-feira =)")
                            break
                        case '3':
                            print("Quarta-feira =)")
                            break
                        case '4':
                            print("Quinta-feira =)")
                            break
                        case '5':
                            print("Sexta-feira =)")
                            break
                        case '6':
                            print("Sábado =)")
                            break
                        case '7':
                            print("Domingo =) ")
                            break
                        case other:
                           print("colocou um numero errado \n")

            case '14':
                print(escolha)
                notaAluno = [float(input("1ª nota: ")),float(input("2ª nota: "))]
                def calcMedia (nota):
                    return ((nota[0] + nota[1]) / 2)
                def aproveitamento(media) :
                    if ( 9.0 < media <= 10.0):
                        return 'A  -- Aprovado' 
                    if ( 7.5 < media <= 9.0):
                        return 'B  -- Aprovado' 
                    if ( 6.0 < media <= 7.5):
                        return 'C  -- Aprovado'
                    if ( 4.0 < media <= 6.0):
                        return 'D  -- Reprovado' 
                    return 'E  -- Reprovado'
                print(f"A sua média é {calcMedia(notaAluno)}, termina o ano com {aproveitamento(calcMedia(notaAluno))}")

            case '15':
                print(escolha)
                inputDoUtilizador = [float(input("Introduza um lado de um triângulo: ")), float(input("Introduza o segundo lado de um triângulo:  ")), float(input("Introduza o terceiro lado de um triângulo:  ")),]
                
                def verificarTriangulo(lados):
                    return (((lados[0] + lados[1]) > lados[2] and (lados[0] + lados[2]) > lados[1] and (lados[1] + lados[2]) > lados[0]))
                def tipoTriangulo(lados):
                    if lados[0] == lados[1] == lados[2]:
                        return 'Triângulo Equilátero'
                    if lados[0] != lados[1] != lados [2] != lados[0]:
                        return 'Triângulo Escaleno'
                    else : return 'Triângulo Isósceles'
                print(tipoTriangulo(inputDoUtilizador) if (verificarTriangulo(inputDoUtilizador)) else 'Não é um triangulo')

            case '16':
                print(escolha)
                inputDoUtilizador = [float(input("Introduza o 'a': "))]
                if inputDoUtilizador[0] == 0:
                    print(f"a = {inputDoUtilizador[0]}, o programa vai encerrar")
                    break
                inputDoUtilizador2 = [float(input("Introduza o 'b': ")), float(input("Introduza o 'c': "))]
                inputDoUtilizador.extend(inputDoUtilizador2)
                
                def formulaResolvente(parametrosFormulaResolvente):
                    delta = ((parametrosFormulaResolvente[1]^2)- (4*parametrosFormulaResolvente[0]*parametrosFormulaResolvente[2]))
                    if delta < 0:
                        return print("A equação não possui raizes reais por o Delta ser negativo")
                    elif delta == 0:
                        formResolPos = -parametrosFormulaResolvente[1] + (delta)

            
            case '17':
                print(escolha)
            case '18':
                print(escolha)
            case '19':
                print(escolha)
            case '20':
                print(escolha)
            case '21':
                print(escolha)
            case '22':
                print(escolha)
            case '23':
                 print(escolha)
            case '24':
                print(escolha)
            case '25':
                 print(escolha)
            case '26':
                print(escolha)
            case '27':
                print(escolha)
            case '28':
                    print(escolha)
    elif escolha.lower() == 's':
        print("Saindo do menu.")
        break
    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 28 ou 's' para sair.")