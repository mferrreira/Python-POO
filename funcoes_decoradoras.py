# Funções decoradoras e com classe

# def adiciona_repr(cls):
#     def meu_repr(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name} {class_dict}'
#         return class_repr
#     cls.__repr__ = meu_repr
#     return cls

# class MyReprMixin:
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name} {class_dict}'

#         return class_repr

# class Time(MyReprMixin):
#     def __init__(self, nome):
#         self.nome = nome
    
# class Planeta(MyReprMixin):
#     def __init__(self, nome):
#         self.nome = nome
     

    
# a = Time('cruzeiro')
# b = Planeta('plutão')

# c = adiciona_repr(Time('flamengo'))
# print(a, b, c)

def adiciona_repr(cls):

    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} {class_dict}'
        return class_repr
    
    cls.__repr__ = meu_repr
    return cls

@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome
    
@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome
     

    

brasil = Time('Brasil')
portugal = Time('Portugal')

plutao = Planeta('Plutão')

print(brasil)
print(portugal)
print(plutao)