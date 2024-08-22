class Veiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'A marca do veiculo é: {self.marca} {self.modelo.ljust(25)} --- Cor: {self.cor.ljust(25)} --- O veiculo esta ativo? {status}'
    
    
    

        
        