# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).


if __name__ == '__main__':
    # Pedindo o primeiro numero em celsius
    print("Welcome to the program, Write value in Fahrenheit")
    Fahrenheit = float(input())# int() converte uma string para inteiro

    Celsius = (Fahrenheit - 32) / 1.8

    print(f'The result is : {Celsius}')
