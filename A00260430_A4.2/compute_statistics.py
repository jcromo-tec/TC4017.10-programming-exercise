'''
Programa para calcular las estadisticas de una lista de números leidos de un archivo.
Las estadisticas a calcular son la media, la mediana, la moda, la varianza y la 
desviación standard.
'''
import sys
from files import read_numbers_file

# Constantes
OK_STATUS = 0
ERROR_STATUS = 9

def get_mean(numbers_list):
    '''
    Funcion para calcular la media sumando todos los valores de la lista y
    dividiendo la suma por el tamaño de la lista.
    '''
    mean = sum(numbers_list) / len(numbers_list)
    return mean

def get_median(numbers_list):
    '''
    Funcion para calcular la mediana:
    - La lista de números se sortea de menor a mayor
    - Se determina si el tamaño es impar o par
    - Si el tamaño es par se calcula la mediana como el promedio de los dos números
      en ambos lados de la mitad del arreglo
    - Si el tamaño es impar se usa el número a la mitad del arreglo
    '''
    list_size = len(numbers_list)
    median = 0.
    numbers_list.sort()
    if list_size % 2 == 0:
        left_number = numbers_list[list_size // 2]
        right_number = numbers_list[list_size // 2 + 1]
        median = (left_number + right_number) / 2
    else:
        median = numbers_list[list_size // 2]
    return median

def get_mode(numbers_list):
    '''
    Funcion para calcular la moda creandon un diccionario donde cada elemento
    representa un número único en la lista de números.
    
    Cada vez que se encuentre el número en el diccionario se incrementa el valor
    para ese elemento por 1.

    Si el número no está en el diccionario se agrega con un valor inicial de 1.

    La moda puede ser multi-modal, o con más de un número que se repita el mayor
    número de veces, así que se prepara una lista como respuesta.
    '''
    numbers_dictionary = {}
    for number in numbers_list:
        if number in numbers_dictionary:
            numbers_dictionary[number] += 1
        else:
            numbers_dictionary.update({number: 1})
    mode = [mode_number[0] for mode_number in numbers_dictionary.items()
            if mode_number[1] == max(numbers_dictionary.values())]
    return mode

def get_variance_and_standard_deviation(numbers_list, mean_value):
    '''
    Funcion para calcular la variancia y la desviacion estandard:
    - la varianza se calcula como la suma de los cuadrados de la diferencia entre los
      valores en la lista y la media obtenida para la lista, dividida por el tamaño de
      la lista menos 1
    - la desviación estándar es la raíz cuadrada de la varianza
    '''
    variance = sum(pow((number - mean_value), 2) for number in numbers_list) \
               / (len(numbers_list) - 1)
    standard_deviation = pow(variance, 0.5)
    return variance, standard_deviation

# Logica principal
if len(sys.argv) < 2:
    print('Usage:\n', 'python compute_statistics.py <file name>\n')
    sys.exit(OK_STATUS)
else:
    file_name = sys.argv[1]

status, numbers, values_read, values_discarded = read_numbers_file(file_name)

if status == 0:
    # Se procede a calcular estadísticas si te tienen uno o más números
    numbers_mean = get_mean(numbers)
    numbers_median = get_median(numbers)
    numbers_mode = get_mode(numbers)
    var_value, std_dev = get_variance_and_standard_deviation(numbers, numbers_mean)

    # Preparando líneas del encabezado y líneas con las estadísticas
    lines = [
        f'FILE:      {file_name}\n',
        f'READ:      {values_read}\n',
        f'DISCARDED: {values_discarded}\n',
        f'COUNT:     {len(numbers)}\n',
        f'MEAN:      {numbers_mean}\n',
        f'MEDIAN:    {numbers_median}\n',
        f'MODE:      {numbers_mode}\n',
        f'SD:        {std_dev}\n',
        f'VAR:       {var_value}\n',
    ]

    try:
        # Escribiendo las líneas del encabezado y de las estadísticas a un archivo
        with open('StatisticsResults.txt', '+wt', encoding='UTF-8') as fd:
            fd.writelines(lines)
        # Desplegando las líneas del encabezado y de las estadísticas en la consola
        for line in lines:
            print(line, end='')
    except OSError as error:
        print(f'[ERROR] - An exception ocurred while processing results file: {error}')
        sys.exit(ERROR_STATUS)

sys.exit(status)
    