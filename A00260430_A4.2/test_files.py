'''
Modulo para probar las funciones para leer archivos con números y archivos con palabras.
'''
from files import read_numbers_file, read_words_file
status, numbers, values_read, values_discarded = read_numbers_file('numbers-list-by-line.txt')
print(status, numbers)

status, words, values_read, values_discarded = read_words_file('words-list-by-line.txt')
print(status, words)
