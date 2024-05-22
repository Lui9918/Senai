#Faça um Programa para uma loja de tintas. 
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
#e que a tinta é vendida em latas de 18 litros, 
#que custam R$ 80,00 
#ou em galões de 3,6 litros, 
#que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. 
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

from math import ceil
if __name__ == '__main__':

    print('How many square meters will you paint?')
    square_meters = float(input())
    litersofpaint = square_meters/6
    canofpaint = ceil(litersofpaint/18)
    pricecan = canofpaint * 80.00
    
    gallonsofpaint = ceil(litersofpaint/3.6)
    pricegallonsofpaint = gallonsofpaint * 25.00
    
    
    
print(f'You will need {canofpaint} cans of 18 liters paint') 
print(f'and you will pay {pricecan}')

print(f'Or {gallonsofpaint} of gallons paint')
print(f'and you will pay {pricegallonsofpaint}')
