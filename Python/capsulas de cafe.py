'''Alguns professores do DCX adoram tomar café e decidiram adquirir uma cafeteira especial para a sala do Departamento. A cafeteira utiliza cápsulas de café de vários sabores para preparar a bebida, e cada cápsula prepara o equivalente a duas xícaras.

As cápsulas são vendidas em caixas pequenas (10 unidades) ou grandes (16 unidades), e ficou acertado que cada professor faria a doação de quantas caixas quisesse para o grupo.

Escreva um programa que receba como entrada a quantidade e o tamanho das caixas doadas por cada um dos sete professores que compartilham a cafeteira, e exiba a quantidade total de cápsulas de café doadas, e quantas xícaras cada professor poderá beber.'''
n=0
n2=0 
for c in range (7):
    qtd=int(input("digite a quantidade : "))
    tam=input("digite o tamanho: ").upper()
    if tam=="P":
        n+=qtd
    elif tam=="G":
        n2+=qtd
    else:
        print("vc digitou um tamaho invalido")
        break
soma=(n*10)+(n2*16)
print("Quantidade de caixas doadas: ",soma)
xicaras= int(soma*2/7)
print("Cada professor poderá beber {} xicaras de café".format(xicaras))
