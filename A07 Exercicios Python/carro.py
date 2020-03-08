class Carro:
    def __init__(self, consumo, qtdeCombustivel):
        self.consumo = consumo
        self.qtdeCombustivel = qtdeCombustivel

    def andar(self, quilometros):
        consumido = quilometros / self.consumo
        self.qtdeCombustivel -= consumido

    def abastecer(self, quantidade):
        self.

    def __str__(self):
        return str(self.consumo) + "km/l" + " " + str(self.qtdeCombustivel)
    
carro1 = Carro(10.0, 50.0)
print(carro1)
carro1.andar(100)
print(carro1)
