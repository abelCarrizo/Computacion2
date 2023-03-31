import argparse

def main():
    parser = argparse.ArgumentParser(description='Generador de numeros impares') #Contiene información sobre los argumentos que esperamos que el usuario proporcione
    parser.add_argument('-n', type=int, default=0, help='Ingresar un entero positivo') #Argumentos que esperamos recibir del usuario
    args = parser.parse_args() #Contiene los valores de los argumentos que el usuario proporcionó.
    
    #Generar la lista de los n primero numeros impares
    impares = []
    for i in range(1, 2*args.n, 2):
        impares.append(i)
    print(impares)

if __name__=='__main__':
    main()
        