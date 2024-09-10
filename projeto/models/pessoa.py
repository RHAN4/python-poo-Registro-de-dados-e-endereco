from models.enums.generos import Generos
from models.endereco import Endereco

class Pessoa:
    def __init__(self, id: int, nome: str, dataNascimento: str, telefone: str,
                 email: str, generos: Generos, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.telefone = telefone
        self.email = email
        self.generos = generos
        self.endereco = endereco

    def __str__(self) -> str:
        return("\nDados da pessoa: "
               f"\nNome: {self.nome}"
               f"\nData de nascimento: {self.dataNascimento}"
               f"\nTelefone: {self.telefone}"
               f"\nE-mail: {self.email}"
               f"\nGênero: {self.generos}"
               f"\n{self.endereco}")