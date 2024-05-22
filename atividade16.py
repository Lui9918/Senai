#Faça um programa para uma loja de tintas. 
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
#e que a tinta é vendida em latas de 18 litros, 
#que custam R$ 80,00. 
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
from math import ceil
if __name__ == '__main__':

    print('How many square meters will you paint?')
    square_meters = float(input())
    litersofpaint = square_meters/3
    canofpaint = ceil(litersofpaint/18)
    pricecan = canofpaint * 80.00
    
print(f'You will need {canofpaint} cans of paint') 
print(f'and you will pay {pricecan}')
