#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

if __name__ == '__main__':
    # Pedindo o primeiro numero
    print("Welcome to the program, enter the side of the square:")
    number1 = int(input())# int() converte uma string para inteiro
     # Fazendo a soma
    result1 = (number1*number1) * 2


    # Imprimindo
    print(f'The double result is : {result1}')
