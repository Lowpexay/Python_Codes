class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} realizado. Novo saldo: R${self.saldo}')
        else:
            print('Valor inválido para depósito.')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado. Novo saldo: R${self.saldo}')
        else:
            print('Valor inválido para saque ou saldo insuficiente.')

    def consultar_saldo(self):
        print(f'Saldo atual da conta de {self.titular}: R${self.saldo}')


if __name__ == "__main__":
    # Cria uma conta
    minha_conta = ContaBancaria(titular="Gabriel")

    # Faz operações na conta
    minha_conta.depositar(1000)
    minha_conta.sacar(500)
    minha_conta.consultar_saldo()
