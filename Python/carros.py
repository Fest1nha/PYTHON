class Carros:
    carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor 
        self.ano = ano
        Carros.carros.append(self)
    
    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'

    def listar_carros():
        for carros in Carros.carros:
            print(f'{carros.modelo} | {carros.cor} | {carros.ano}')

    
carro1 = Carros('Honda Civic SI', 'Vermelho', '2009')
carro2 = Carros('VW Golf GTI', 'Vermelho', '2019')

Carros.listar_carros()