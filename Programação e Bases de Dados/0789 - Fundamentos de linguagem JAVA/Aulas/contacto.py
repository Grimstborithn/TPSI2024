@dataclass()
class Morada:
    localidade: str
    teste: str
    def __init__(self, localidade: str):
        self.localidade = localidade
        self.teste = "txt"


class Contacto:
    def __init__(self, nome, telefone=None, data_nascimento=None):
        self.nome = nome
        self.telefones = []
        if telefone:
            self.adicionar_telefone(telefone)
        self.morada = morada
        self.data_nascimento = data_nascimento
    
    def adicionar_telefone(self, telefone):
        self.telefones.append(telefone)
    
    def remover_telefone(self, telefone):
        if telefone in self.telefones:
            self.telefones.remove(telefone)
    
    def __str__(self):
        telefone_str = ', '.join(self.telefones)
        return f"Nome: {self.nome}, Telefones: {telefone_str}, Morada: {self.morada}, Data de Nascimento: {self.data_nascimento}"
