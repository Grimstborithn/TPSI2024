class Pilha:
    def __init__(self):
        self.conteudo = []
        self.tipo = None

    def esta_vazia(self):
        return len(self.conteudo) == 0

    def pilha(self, data):
        if self.tipo is None:
            self.tipo = type(data)
        elif type(data) != self.tipo:
            raise TypeError(f"Tipo de dados incorreto. \n Esperado: {self.tipo} \n  Recebido: {type(data)}")
        self.itens.append(data)

    def desempilhar(self):
        if self.esta_vazia():
            raise TypeError(f"A pilha está vazia!")
        return self.conteudo.pop()

    def topo(self):
        if self.esta_vazia():
            raise TypeError(f"A pilha está vazia!")
        return self.conteudo[-1]

    def tamanho(self):
        return len(self.conteudo)



class Fila:
    def __init__(self):
        self.conteudo = []
        self.tipo = None

    def esta_vazia(self):
        return len(self.conteudo) == 0

    def em_fila(self, data):
        if self.tipo is None:
            self.tipo = type(data)
        elif type(data) != self.tipo:
            raise TypeError(f"Tipo incorreto. Esperado: {self.tipo}, Recebido: {type(data)}")
        self.itens.append(data)

    def retirar(self):
        if self.esta_vazia():
            raise TypeError(f"A pilha está vazia!")
        return self.conteudo.pop(0)

    def primeiro(self):
        if self.esta_vazia():
            raise TypeError(f"A pilha está vazia!")
        return self.conteudo[0]

    def ultimo(self):
        if self.esta_vazia():
            raise TypeError(f"A pilha está vazia!")
        return self.conteudo[-1]

    def tamanho(self):
        return len(self.conteudo)


