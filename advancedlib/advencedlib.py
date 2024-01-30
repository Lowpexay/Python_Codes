# advancedlib.py

def add(a, b):
    """Função para adicionar dois números."""
    return a + b

def subtract(a, b):
    """Função para subtrair dois números."""
    return a - b

def multiply(a, b):
    """Função para multiplicar dois números."""
    return a * b

def divide(a, b):
    """Função para dividir dois números."""
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

def power(a, b):
    """Função para elevar um número ao expoente."""
    return a ** b

def concatenate_strings(str1, str2):
    """Função para concatenar duas strings."""
    return str1 + str2

def reverse_list(lst):
    """Função para inverter uma lista."""
    return lst[::-1]

def find_average(numbers):
    """Função para calcular a média de uma lista de números."""
    if not numbers:
        return "Erro: Lista vazia"
    return sum(numbers) / len(numbers)
