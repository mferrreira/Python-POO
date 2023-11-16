# Associação

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class Ferramenta_de_Escrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'
    

escritor = Escritor('Márcio')
ferramenta = Ferramenta_de_Escrever('Lápis')

escritor.ferramenta = ferramenta

print(ferramenta.escrever())
print(escritor.ferramenta.escrever())

# Agregação

"""
    Agregação é uma forma mais especializada de associação
    entre dois ou mais objetos. Cada objeta terá
    seu ciclo de vida independente.

    Geralmente é uma relação de um para muitos, onde um 
    objeto tem um ou muitos objetos.
    Os objetos podem viver separadamente, mas pode
    se tratar de uma relação onde um objeto precisa de outro para
    fazer determinada tarefa.
    (existem controvérsias sobre as definições de agregação)
"""

class Carrinho:
    def __init__(self):
        self._produtos = []

    def adicionar_produto(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)


    def total(self):
        return sum([float(p.preco) for p in self._produtos])
    
    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

p1, p2 = Produto('Goiaba', "1.20"), Produto('Café', "5.76")
c = Carrinho()

print(c.adicionar_produto(p1, p2))
c.listar_produtos()
print(c.total())

# Composição

"""
    Composição é uma especialização da agregação.
    Mas nela, quando o objeto "pai" for apagado, todas
    as referências dos objetos filhos também são
    apagadas        
"""

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_indereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO', self.rua)

cliete1 = Cliente('Marcio')
cliete1.inserir_indereco('Av. Brasil', 52)
cliete1.inserir_indereco('Rua 4', 195)
cliete1.listar_enderecos()