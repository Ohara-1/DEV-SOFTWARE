class Conta:
    def __init__(self, saldo: float, numero: int, agencia: str, cliente, historico):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico
    
    def info_saldo(self):
        return self.saldo
    
    def nova_conta(self, cliente, numero: int, agencia: str):
        return Conta(0.0, numero, agencia, cliente, Historico())

    def sacar(self, valor: float):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.historico.adicionar_transacao(f"Saque de {valor}")
            return True
        return False

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(f"Depósito de {valor}")
            return True
        return False


class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, limite: float, limite_saque: float):
        super().__init__(saldo, numero, agencia, cliente, Historico())
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self, valor: float):
        if valor > 0 and valor <= self.saldo + self.limite and valor <= self.limite_saque:
            self.saldo -= valor
            self.historico.adicionar_transacao(f"Saque de {valor:.2f}")
            return True
        return False


class Historico:
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacao(self, descricao: str):
        self.transacoes.append(descricao)
    
    def listar_transacoes(self):
        return self.transacoes


class Cliente:
    def __init__(self, endereco: str, contas: list):
        self.endereco = endereco
        self.contas = contas
    
    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco, contas, cpf: str, nome: str):
        super().__init__(endereco, contas)
        self.cpf = cpf
        self.nome = nome


class Transacao:
    def registrar_transacao(self, conta: Conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor
    
    def registrar_transacao(self, conta: Conta):
        return conta.depositar(self.valor)


class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor
    
    def registrar_transacao(self, conta: Conta):
        return conta.sacar(self.valor)