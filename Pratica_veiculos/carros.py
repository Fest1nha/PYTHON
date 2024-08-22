from veiculos import Veiculo

class Carro(Veiculo):
    def __init__(self,marca,modelo,portas,cor):
        super().__init__(marca,modelo)
        self.portas = portas
        self.cor = cor

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"  
        return f'A marca do veiculo é: {self.marca} {self.modelo.ljust(30)} | Quantidade de portas: {str(self.portas).ljust(25)} | Cor: {self.cor.ljust(25)} | Status: {status}'
          