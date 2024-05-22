#13.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Obs:Para homens: (72.7*h) - 58, Para mulheres: (62.1*h) - 44.7

if __name__ == '__main__':
    print("Welcome to weicht calculator, to begin tell me: You are men wright 1, or woman wright 2")
    gender = float(input())
    
    print("Now wright your height")
    height = float(input())
    
    if (gender == 1) :  
        result = (height * 72.7) - 58
    
    else : 
        result = (height * 62.1) - 44.7
    print (f'The result is: {result}')
    