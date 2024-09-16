import pytest
from ..models.pessoa import Pessoa # Caminho relativo
from projeto.models.endereco import Endereco # Caminho absoluto
from projeto.models.enums.generos import Generos
from projeto.models.enums.unidadefederativa import UnidadeFederativa

# Modelo:
@pytest.fixture
def criar_pessoa():
    pessoaUm = Pessoa(4525, "Marta", "14/08/1999", "(71) 9 8844-5720", "marta@hotmail.com", 
                  Generos.FEMININO, Endereco("Avenida Afonso", "58", "Ao lado do posto", 
                                             "45871-589", "Salvador", UnidadeFederativa.BAHIA))
    return pessoaUm

def test_pessoa_atributo_nome(criar_pessoa):
    assert criar_pessoa.nome == "Marta"

def test_pessoa_atributo_id(criar_pessoa):
    assert criar_pessoa.id == 4525
