#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês, 
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

if __name__ == '__main__':
    # Pedindo o primeiro numero
    print("Welcome to the program, Write down how much you earn per hour")
    money = float(input())# int() converte uma string para inteiro

    print("Now enter down how hours you work in month")
    hours = float(input())# int() converte uma string para inteiro
# Fazendo a soma
    resultbrute = money * hours
    resultinss = (resultbrute * 11/100)
    resultsindicate = (resultbrute * 5/100)
    resulttotal = resultbrute - resultinss - resultsindicate
    
    print(f'you earned per gross month: {resultbrute}') 
    print(f'you pay for inss:{resultinss}')
    print(f'you pay for sindicate: {resultsindicate}')
    print(f'you really earn per month: {resulttotal}')
    
    
   
 