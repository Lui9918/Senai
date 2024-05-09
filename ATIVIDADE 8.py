#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

if __name__ == '__main__':
    # Pedindo o primeiro numero
    print("Welcome to the program, Write down how much you earn per hour")
    money = float(input())# int() converte uma string para inteiro

    print("Now enter down how hours you work in month")
    hours = float(input())# int() converte uma string para inteiro
# Fazendo a soma
    result1 = money * hours

    print(f'The result is : {result1}')
