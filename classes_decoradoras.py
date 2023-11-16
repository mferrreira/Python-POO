
class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna

@Multiplicar(4)
def soma(x,y):
    return x + y

a = soma(1,4)
print(a)