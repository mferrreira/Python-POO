# @property + @setter - getter e setter no modo Pythonico
# - como getter
# - para evitar quebrar código cliente
# - para habilitar setter
# - para executar ações ao obter um atributo

# Atributos que começam com um ou dois "_" não devem ser usados fora da classe

class Caneta:

    def __init__(self, cor):
        self._cor = cor                 # 

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor
        ...

caneta = Caneta("Azul")
print(caneta.cor)

caneta.cor = "Rosa"
print(caneta.cor)