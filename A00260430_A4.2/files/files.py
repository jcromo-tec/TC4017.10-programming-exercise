'''
Modulo para leer archivos con numeros enteros o con palabras. Una linea puede
tener una o más palabras, o uno o más números, separados o separadas por
espacios.

Cada número o palabra sera agregado a una lista si es un número valido o es una
palabra con una o mas letras y/o números. Las palabras pueden ser únicamente
alfanuméricas y los números pueden tener decimales
'''
import re

OK_STATUS = 0
ERROR_STATUS = 9
EMPTY_LIST_STATUS = 1

def read_words_file(file_name):
    '''
    Funcion para leer listas de palabras. 
    '''
    status = OK_STATUS
    line_number = 0
    item_number = 0
    values_read = 0
    values_discarded = 0
    words = []
    try:
        with open(file_name, 'r', encoding='UTF-8') as fd:
            lines = fd.readlines()
            for line in lines:
                line_number += 1
                item_number = 0
                # Se remueven caracteres al final de cada línea leída del archivo y
                # se usa un espacio como separador para separar cada palabra en una línea
                for item in line.rstrip().split(' '):
                    values_read += 1
                    item_number += 1
                    # Se checa la palabra para verificar que es alfanumérica usando una
                    # expresión regular. La palabra es agregada a la lista si pasa la
                    # verificación. Si no se despliega un error en la consola
                    if bool(re.match('^[a-zA-Z0-9]+$', item)):
                        words.append(item.lower())
                    else:
                        values_discarded += 1
                        print(
                            f'[WARNING] - item number {item_number}',
                            f' in line {line_number} is not an alphanumeric word.')
    except OSError as error:
        print(f'[ERROR] - An exception ocurred while processing input file: {error}')
        status = ERROR_STATUS

    if len(words) < 1:
        status = EMPTY_LIST_STATUS

    return status, words, values_read, values_discarded

def read_numbers_file(file_name):
    '''
    Funcion para leer listas de numeros
    '''
    status = OK_STATUS
    line_number = 0
    item_number = 0
    values_read = 0
    values_discarded = 0
    numbers = []
    try:
        with open(file_name, 'r', encoding='UTF-8') as fd:
            lines = fd.readlines()
            for line in lines:
                line_number += 1
                item_number = 0
                # Se remueven caracteres al final de cada línea leída del archivo y
                # se usa un espacio como separador para separar cada número en una línea
                for item in line.rstrip().split(' '):
                    values_read += 1
                    item_number += 1
                    try:
                        # Se trata de convertir convertir el texto del número en un entero.
                        # El número se agrega a la lista de números si pasa verificación.
                        # Si no se despliega un error en la consola.
                        # La primera conversión se hace a punto flotante para poder manejar
                        # números grandes y luego a entero para forzar python a usar la
                        # versión larga de un valor entero.
                        num = round(float(item))
                        numbers.append(num)
                    except ValueError:
                        values_discarded += 1
                        print(
                            f'[WARNING] - item number {item_number}',
                            f' in line {line_number} is not a number.'
                        )
    except OSError as error:
        print(f'[ERROR] - An exception ocurred while processing input file: {error}')
        status = ERROR_STATUS

    if len(numbers) < 1:
        status = EMPTY_LIST_STATUS

    return status, numbers, values_read, values_discarded
