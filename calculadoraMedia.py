class CalculadoraMedia:
    def __init__(self):
        self.numeros = []

    def adicionar_numero(self, numero):
        self.numeros.append(numero)
        print(f'Número {numero} adicionado à lista.')

    def calcular_media(self):
        if not self.numeros:
            print('A lista de números está vazia. Não é possível calcular a média.')
            return

        media = sum(self.numeros) / len(self.numeros)
        print(f'Média dos números: {media}')

    def limpar_lista(self):
        self.numeros = []
        print('Lista de números limpa.')

if __name__ == "__main__":
    calculadora = CalculadoraMedia()

    
    calculadora.adicionar_numero(10)
    calculadora.adicionar_numero(20)
    calculadora.adicionar_numero(30)

    
    calculadora.calcular_media()
    ;

  
    calculadora.limpar_lista()

    
    calculadora.calcular_media()
