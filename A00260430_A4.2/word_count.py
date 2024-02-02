'''
Programa para calcular la frequencia de cada palabra en una lista de palabras leídas de un
archivo.
'''
import sys
import time
from files import read_words_file

# Constantes
OK_STATUS = 0
ERROR_STATUS = 9

def get_frecuency(words_list):
    '''
    Funcion para calcular la frequencia de palabras creandon un diccionario donde
    cada elemento representa una palabra única en la lista de palabras.
    
    Cada vez que se encuentre la palabra en el diccionario se incrementa el valor
    para ese elemento por 1.

    Si la palabra no está en el diccionario se agrega con un valor inicial de 1.
    '''
    words_dictionary = {}
    for word in words_list:
        if word in words_dictionary:
            words_dictionary[word] += 1
        else:
            words_dictionary.update({word: 1})
    return sum(words_dictionary.values()), zip(words_dictionary.keys(), words_dictionary.values())

def format_words_frequency(word_frequency_list, frequency_total):
    '''
    Funcion para crear lista de palabras con su frequencia.
    '''
    formatted_frequency_list = []
    for word_frequency in word_frequency_list:
        # El primer elemento (0) de la variable word_frequency contiene la palabra
        # El segundo elemento (1) de la variable word_frequency contiene la frequencia
        formatted_frequency = f'{word_frequency[0]}: {word_frequency[1]}\n'
        formatted_frequency_list.append(formatted_frequency)

    formatted_total = f'GRAND TOTAL: {frequency_total}\n'
    formatted_frequency_list.append(formatted_total)
    return formatted_frequency_list

def get_elapsed_time(started):
    '''
    Funcion para calcular el tiempo de ejecución del programa
    '''
    finished = time.time()
    return f'ELAPSED TIME: {(finished - started):.6f} seconds.\n'

# Logica principal
start_time = time.time()

if len(sys.argv) < 2:
    print('Usage:\n', 'python word_count.py <file name>\n')
    sys.exit(OK_STATUS)
else:
    file_name = sys.argv[1]

status, words, values_read, values_discarded = read_words_file(file_name)

if status == 0:
    # Se procede a calcular las frequencias de cada palabra en la lista
    total, frequency_list = get_frecuency(words)

    # Se procede a formatear la lista de frequencias
    formatted_freq_list = format_words_frequency(frequency_list, total)

    # Preparando líneas del encabezado y líneas con las estadísticas
    lines = [
        f'FILE:      {file_name}\n',
        f'READ:      {values_read}\n',
        f'DISCARDED: {values_discarded}\n',
        f'COUNT:     {len(words)}\n',
    ]

    try:
        # Escribiendo las líneas del encabezado y las frequencias a un archivo
        with open('WordCountResults.txt', '+wt', encoding='UTF-8') as fd:
            fd.writelines(lines)
            fd.writelines(formatted_freq_list)
        # Desplegando las líneas del encabezado y las frequencias en la consola
        for line in lines:
            print(line, end='')
        for frequency_element in formatted_freq_list:
            print(frequency_element, end='')
    except OSError as error:
        print(f'[ERROR] - An exception ocurred while processing results file: {error}')
        elapsed_time = get_elapsed_time(start_time)
        print (elapsed_time)
        sys.exit(ERROR_STATUS)

elapsed_time = get_elapsed_time(start_time)

try:
    with open('WordCountResults.txt', '+at', encoding='UTF-8') as fd:
        fd.writelines(elapsed_time)
    print (elapsed_time)
except OSError as error:
    print(f'[ERROR] - An exception ocurred while processing results file: {error}')
    print (elapsed_time)
    sys.exit(ERROR_STATUS)

sys.exit(status)
