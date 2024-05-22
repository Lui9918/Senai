#12.Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

if __name__ == '__main__':
    print("Welcome to weicht calculator, to begin write your height")
    height = float(input())
    
    result = (height * 72.7) - 58
    
    print(f'The result is: {result}')
    