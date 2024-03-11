'''
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
N = int(input())

for i in range (0,N):
    valores = input().split()
    A = valores[0]
    B = valores[1]

    n = len(B)
    ultimos_carct = A[-n:]
    if ultimos_carct == B:
        print("encaixa")
    else:
        print("nao encaixa")

    



#    if(len(A) < len(B)):
#        print("nao encaixa")
#    elif ultimos_carct == B:
#        print("encaixa")