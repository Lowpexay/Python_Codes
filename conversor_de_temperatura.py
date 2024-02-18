print("**********************************************************")
print("**************** Conversor de Temperatura ****************")
print("**********************************************************")

temperatura = input("Digite a temperatura em Celsius: ")

print(temperatura)

def calculaTemp(tempFah):
    tempFah = float(temperatura) * 1.8 + 32
    return tempFah

resultado = calculaTemp(temperatura)
print("A temperatura em Fahrenheit é de: ", resultado)
