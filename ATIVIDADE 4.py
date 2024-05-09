# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

if __name__ == '__main__':
    # Pedindo o primeiro numero
    print("Write first number:")
    number1 = int(input())# int() converte uma string para inteiro

    # Pedindo o segundo numero
    print("Write second number:")
    number2 = int(input())

    # Pedindo o terceiro numero
    print("Write thirth number:")
    number3 = int(input())

    # Pedindo o quarto numero
    print("Write four number:")
    number4 = int(input())

        # Fazendo a soma
    result1 = (number1 + number2 + number3 + number4) / 4

    # Imprimindo
    print(f'Result: {result1}')
