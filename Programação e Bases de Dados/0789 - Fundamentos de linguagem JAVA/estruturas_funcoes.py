def exerc_1(n):
    for i in range(n):
        i += 1
        print( (str(i) + " ")*i)


inputUtilizador = int(input("Escolha um n: "))


def exerc_2(n):
    for i in range(n):
                
        for j in range (i+1):
            
            print (j+1, end=" ")
        print("\n")       

exerc_2(inputUtilizador)









