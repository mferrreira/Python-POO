# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de se fazer coisas
# @property é uma propriedade do objeto, ela 
# é um método que se comporta como um 
# atributo
# Geralmente é usada nas seguintes situações:
# - como getter
# - para evitar quebrar código cliente
# - para habilitar setter
# - para executar ações ao obter um atributo

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    # getter padrão
    def get_cor(self):
        print("GETTER")
        return self.cor_tinta
    
    @property
    def cor(self):
        print("PROPERTY")
        return self.cor_tinta


caneta = Caneta('Azul')
print(caneta.get_cor())
print(caneta.cor)
print(caneta.cor_tinta)