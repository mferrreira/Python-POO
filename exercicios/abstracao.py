# Exercício com Abstração, Herança, Encapsulamento e Polimorfismo

# Criar um sistema bancário (extremamente simples) que tem clientes, contas
# e um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente)
# e que possa sacar/depositar nessa conta. Contas corrente tem um limite extra

# Conta (ABC)
#     sacar()
#     ContaCorrente
#     ContaPoupanca

# Pessoa (ABC)
#     Cliente
#         Cliente -> Conta

# Banco
#     Banco -> Cliente
#     Banco -> Conta

# Dicas:

# Criar classe Cliente que herda da classe Pessoa (Herança)
#     Pessoa tem nome e idade (getters)
#     Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupança)

# Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
#     ContaCorrente deve ter um limite extra
#     Contas têm agência, número da conta e saldo
#     Contas devem ter método para depósito
#     Conta (super classe) deve ter o método sacar abstrato (ABC)
#     polimorfismo - as subclasses que implementam o método sacar

# Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
# Banco será responsável por autenticar o cliente e as contas da seguinte
# maneira:
#     Banco tem contas e clientes (Agregação)
#         Checar se a agência é daquele banco
#         Checar se o cliente é daquele banco
#         Checar se a conta é daquele banco

# Só será possível sacar se passar na autenticação do banco (descrita acima)
# Banco autentica por um método

from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo=0):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    def __repr__(self):
        cls_name = type(self).__name__
        agc = self._agencia
        c = self._conta
        s = self._saldo
        return f"\n\t{cls_name} ({agc} {c} {s})"

    @abstractmethod
    def sacar(self, idade):
        ...

    def depositar(self, valor: float) -> None:
        self._saldo += valor


class ContaPoupanca(Conta):
    def sacar(self, valor: float):
        valor_pos_saque = self._saldo - valor

        if valor_pos_saque >= 0:
            self._saldo -= valor
            return self._saldo
        return "Não foi possível sacar o valor desejado"


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = -limite

    def sacar(self, valor):
        valor_pos_saque = self._saldo - valor
        limite_maximo = self.limite

        if valor_pos_saque >= limite_maximo:
            self._saldo -= valor
            return self._saldo
        print("Não foi possível sacar o valor desejado")


class Pessoa(ABC):
    def __init__(self, nome: str, idade: int):
        if not isinstance(idade, int):
            raise TypeError("Idade deve ser um número")
        self._nome = nome
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        atts = f"({self.nome!r}, {self.idade!r})"
        return f"{class_name} {atts}"

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade
        return


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta: Conta | None):
        if idade <= 18:
            raise Exception("O cliente deve ser maior de idade")

        super().__init__(nome, idade)
        self.conta = conta

    def __repr__(self):
        class_name = type(self).__name__
        atts = f"({self.nome!r}, {self.idade!r}, {self.conta})"
        return f"{class_name} {atts}"


class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[Pessoa] | None = None,
        contas: list[Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def __repr__(self):
        return f"{self.agencias} {self.clientes} {self.contas}"

    def _checa_agencia(self, conta: Conta):
        if conta._agencia in self.agencias:
            return True
        return False

    def _checa_cliente(self, cliente: Pessoa):
        if cliente in self.clientes:
            return True
        return False

    def _checa_conta(self, conta: Conta):
        if conta in self.contas:
            return True
        return False

    def autenticar(self, cliente: Cliente, conta: Conta):
        c_is_con = conta is cliente.conta
        ag = self._checa_agencia(conta)
        cl = self._checa_cliente(cliente)
        c = self._checa_conta(conta)

        if ag and cl and c and c_is_con:
            return "Autenticou"
        return "não autorizado"


if __name__ == "__main__":
    cp1 = ContaPoupanca(123, 321123, 0)
    cp1.depositar(5)
    print(cp1._saldo)
    cc1 = ContaCorrente(1, 432, 20, 100)
    cc1.depositar(5)
    p1 = Cliente("Márcio", 21, cc1)
    b = Banco()
    b.clientes.extend([p1])
    b.contas.extend([cc1])
    b.agencias.extend([1])
    print(b.autenticar(p1, cp1))
