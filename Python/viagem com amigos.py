'''Luiza vai viajar com seus amigos e estΓ‘ pesquisando preΓ§os. O grupo estΓ‘ em dΓΊvida entre alugar uma casa em Pipa ou em Fortaleza.

Caso escolham ir para Pipa, o aluguel de uma casa com 2 quartos sai por R 600πππππ’πππππ3ππ’πππ‘ππ ππ’π π‘ππ  900. LΓ‘ eles pretendem fazer um passeio de barco, que custa R$ 75 por pessoa.

Caso a escolha do grupo seja Fortaleza, eles poderΓ£o pagar R 950ππππ’πππππ ππππ3ππ’πππ‘ππ ππ’π  1120 por uma com 4 quartos. A atraΓ§Γ£o que querem visitar Γ© um parque aquΓ‘tico cujo ingresso individual custa R$ 60.

Escreva um programa que receba como entrada a quantidade de pessoas do grupo, a cidade escolhida, e a quantidade de quartos que querem na casa, e calcule e exiba o valor total da viagem, e quanto cada um irΓ‘ pagar.

Obs: Considere que todos do grupo irΓ£o para o passeio da cidade.'''

participantes=int(input())
lugar=input().upper()
qtd_quartos=int(input())
aluguel=0
soma=0
if lugar =='PIPA':
    if qtd_quartos==2:
        aluguel=600
    elif qtd_quartos>2:
        aluguel=900
    soma=aluguel+participantes*75
    print(f'{soma:.2f}')
    print(f'{soma/participantes:.2f}')
else:
    if qtd_quartos==3:
        aluguel=950
    else:
        aluguel=1150
    soma=aluguel+participantes*60
    print(f'{soma:.2f}')
    print(f'{soma/participantes:.2f}')
    