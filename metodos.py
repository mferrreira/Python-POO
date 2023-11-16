# Métodos em instâncias de classes Python
# Classe - Molde (geralmente sem dados)
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} acelerou!')

fusca = Carro('Fusca')
celta = Carro('Celta')

print(fusca.nome)
celta.acelerar()