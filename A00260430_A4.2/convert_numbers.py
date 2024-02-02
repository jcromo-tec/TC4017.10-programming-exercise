'''
Programa para desplegar una lista números leidos de un archivo en formato binario y
hexadecimal.
'''
import sys
import time
from files import read_numbers_file

# Constantes
OK_STATUS = 0
ERROR_STATUS = 9
MAX_16BIT_NUMBER = 2**16
MAX_32BIT_NUMBER = 2**32

def format_numbers(numbers_list):
    '''
    Funcion para crear lista de numeros en formato binario y hexadecimal.
    Numeros negativos son presentados en formato de complementos de 2.

    Para convertir numeros negativos a formato binario y hexadecimal
    es necesario determinar el tamaño del numero en bits. Se usan 3
    tamaños posibles: 16 bits, 32 bits y 64 bits. Una vez determinado
    el tamaño el numero negativo se convierte a complementos de 2.

    El numero se representa en formato binario y hexadecimal, se convierte
    a mayúsculas y se remueven los prefijos 0b y 0x, y se crea un lista
    de líneas con los valores a desplegar.
    '''
    formatted_numbers_list = []
    unsigned = 0
    for number in numbers_list:
        if number < 0:
            # Convirtiendo números negativos a complemento de 2
            if abs(number) > MAX_16BIT_NUMBER:
                if abs(number) > MAX_32BIT_NUMBER:
                    unsigned = number + (1 << 64)
                else:
                    unsigned = number + (1 << 32)
            else:
                unsigned = number + (1 << 16)
        else:
            # Usando números positivos sin alterar
            unsigned = number

        # Generando representaciones binaria y hexadecimal, en mayúsculas sin prefijos
        bin_number = f'{bin(unsigned)}'.upper()[2:]
        hex_number = f'{hex(unsigned)}'.upper()[2:]
        formatted_number = f'NUMBER: {number}, BINARY: {bin_number}, HEX: {hex_number}\n'
        formatted_numbers_list.append(formatted_number)
    return formatted_numbers_list

def get_elapsed_time(started):
    '''
    Funcion para calcular el tiempo de ejecución del programa
    '''
    finished = time.time()
    return f'ELAPSED TIME: {(finished - started):.6f} seconds.\n'

# Logica principal
start_time = time.time()

if len(sys.argv) < 2:
    print('Usage:\n', 'python convert_numbers.py <file name>\n')
    sys.exit(OK_STATUS)
else:
    file_name = sys.argv[1]

status, numbers, values_read, values_discarded = read_numbers_file(file_name)

if status == 0:
    # Se procede a formatear la lista de números si te tienen uno o más números
    converted_numbers = format_numbers(numbers)

    # Preparando líneas del encabezado
    lines = [
        f'FILE:      {file_name}\n',
        f'READ:      {values_read}\n',
        f'DISCARDED: {values_discarded}\n',
        f'COUNT:     {len(numbers)}\n',
    ]

    try:
        # Escribiendo las líneas del encabezado y los números convertidos a un archivo
        with open('ConvertionResults.txt', '+wt', encoding='UTF-8') as fd:
            fd.writelines(lines)
            fd.writelines(converted_numbers)
        # Desplegando las líneas del encabezado y los números convertidos en la consola
        for line in lines:
            print(line, end='')
        for converted_number in converted_numbers:
            print(converted_number, end='')
    except OSError as error:
        print(f'[ERROR] - An exception ocurred while processing results file: {error}')
        elapsed_time = get_elapsed_time(start_time)
        print (elapsed_time)
        sys.exit(ERROR_STATUS)

elapsed_time = get_elapsed_time(start_time)

try:
    with open('ConvertionResults.txt', '+at', encoding='UTF-8') as fd:
        fd.writelines(elapsed_time)
    print (elapsed_time)
except OSError as error:
    print(f'[ERROR] - An exception ocurred while processing results file: {error}')
    print (elapsed_time)
    sys.exit(ERROR_STATUS)

sys.exit(status)
