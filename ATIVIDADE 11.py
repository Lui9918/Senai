#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

if __name__ == '__main__':
    # Pedindo o primeiro numero
    print("Write the first integer number:")
    integer1 = int(input())# int() converte uma string para inteiro

    # Pedindo o segundo numero
    print("Write the second integer number:")
    integer2 = int(input())

    # Pedindo o terceiro numero
    print("Write the real number:")
    real = float(input())

    calculus1 = integer1*2 + (integer2/2)

    print(f'The first result is: {calculus1}')

    calculus2 = (integer1)*3 + real

    print(f'The second result is: {calculus2}')

    calculus3 = (real*real*real)

    print(f'The thirth result is: {calculus3}')

