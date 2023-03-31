import argparse
import sys

def count_words_and_lines(filename, print_avg_length=False):
    num_words = 0
    num_lines = 0
    total_length = 0
    with open(filename, 'r') as f:
        for line in f:
            num_lines += 1
            words = line.split()
            num_words += len(words)
            total_length += sum(len(word) for word in words)
    if num_words > 0:
        avg_length = total_length / num_words
    else:
        avg_length = 0
    print(f"El archivo {filename} tiene {num_lines} líneas y {num_words} palabras.")
    if print_avg_length:
        print(f"La longitud promedio de las palabras en el archivo es {avg_length:.2f} caracteres.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Contar palabras y líneas de un archivo de texto.')
    parser.add_argument('filename', metavar='filename', type=str, help='nombre del archivo')
    parser.add_argument('-a', '--avg-length', action='store_true', help='imprimir la longitud promedio de las palabras')
    args = parser.parse_args()
    try:
        count_words_and_lines(args.filename, args.avg_length)
    except Exception as e:
        with open('errors.log', 'a') as f:
            print(f"Error: {e}", file=sys.stderr)
            print(f"Filename: {args.filename}", file=sys.stderr)
            print(f"Arguments: {sys.argv}", file=sys.stderr)
            print(f"{'-'*20}", file=sys.stderr)
            f.write(f"Error: {e}\n")
            f.write(f"Filename: {args.filename}\n")
            f.write(f"Arguments: {sys.argv}\n")
            f.write(f"{'-'*20}\n")
