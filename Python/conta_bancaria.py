class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'{self.titular} | {self.saldo} | {self._ativo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
    
conta1 = ContaBancaria('Joao', 1000)
conta2 = ContaBancaria('Maria', 500)

print(conta1)
print(conta2)

conta3 = ContaBancaria('Carlos', 200)
print(f'Antes de Ativar: Conta ativa? {conta3._ativo}')
ContaBancaria.ativar_conta(conta3)
print(f'Depois de ativar:: Conta ativa? {conta3._ativo}')


print(conta1)
print(conta2)
print(conta3)

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
    
conta4 = ContaBancariaPythonica('Fernanda', 1500)
print(f'titular da conta 4: {conta4.titular}')


class ClienteBanco():
    def __init__(self, nome, cpf, idade, saldo, salario):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade 
        self.saldo = saldo
        self.salario = salario

    def __str__(self):
        return f'{self.nome} | {self.cpf} | {self.idade} | {self.saldo} | {self.salario}'

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancariaPythonica(titular, saldo_inicial)
        return conta
        

cliente1 = ClienteBanco('Ana', '111.222.333-44', 19, 700, 2300)
clietne2 = ClienteBanco('Luiza', '123.456.789-10', 34, 3000, 6500)
cliente3 = ClienteBanco('Pedro', '987.654.321-01', 26, 1000, 3000)

print(cliente1)
print(clietne2)
print(cliente3)

conta_cliente4 = ClienteBanco.criar_conta('Otavio', 2000)
print(f'Conta de {conta_cliente4.titular} criada com saldo inicial de R${conta_cliente4.saldo}')

        


    


