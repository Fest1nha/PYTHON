from veiculos import Veiculo

class Moto(Veiculo):
    def __init__(self,marca,modelo,tipo,cor):
        super().__init__(marca,modelo)
        self.tipo = tipo
        self.cor = cor

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'A marca do veiculo é: {self.marca} {self.modelo.ljust(30)} | Tipo da moto: {self.tipo.ljust(25)} | Cor: {self.cor.ljust(25)} | Status: {status}'    
