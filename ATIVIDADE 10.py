#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

if __name__ == '__main__':
    # Pedindo o primeiro numero em celsius
    print("Welcome to the program, Write value in Celsius")
    celsius = float(input())# int() converte uma string para inteiro

    Fahrenheit = (celsius * 1.8) + 32

    print(f'The result is : {Fahrenheit}')
