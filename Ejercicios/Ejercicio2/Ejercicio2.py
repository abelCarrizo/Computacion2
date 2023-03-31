import argparse

def main():
    parser = argparse.ArgumentParser(description='Repeticion de cadenas')
    parser.add_argument('-n', type=int, default=0, help='Numero de iteraciones en la cadena')
    parser.add_argument('--text', type=str, help='Texto que se repetira')
    args = parser.parse_args()
    print(f'{args.text} ' * args.n) 
if __name__=='__main__':
    main()