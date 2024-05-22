#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
#deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
#e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que 
#João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

if __name__ == '__main__':
    print("Welcome to calculator, to begin wright the number of kilos of fish")
    kilosjoaofish = float(input())
    
    if (kilosjoaofish<50) :
        print (f'All ok 😁')
        
    else :
       result1 = (kilosjoaofish - 50)
       result2 = (result1 * 4)
       print(f'The number of kilos above the limit is: {result1}. And the amount of the fine will be:{result2}')
       
       
    
        
        