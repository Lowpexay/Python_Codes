# main.py
import advancedlib

# Operações matemáticas
result_add = advancedlib.add(5, 3)
result_subtract = advancedlib.subtract(10, 4)
result_multiply = advancedlib.multiply(2, 6)
result_divide = advancedlib.divide(8, 2)
result_power = advancedlib.power(2, 3)

# Manipulação de strings e listas
result_concatenate = advancedlib.concatenate_strings("Olá, ", "mundo!")
result_reverse_list = advancedlib.reverse_list([1, 2, 3, 4, 5])
result_average = advancedlib.find_average([10, 20, 30, 40, 50])

# Exibindo os resultados
print(f"Soma: {result_add}")
print(f"Subtração: {result_subtract}")
print(f"Multiplicação: {result_multiply}")
print(f"Divisão: {result_divide}")
print(f"Potência: {result_power}")
print(f"Concatenação de strings: {result_concatenate}")
print(f"Inversão de lista: {result_reverse_list}")
print(f"Média da lista: {result_average}")
