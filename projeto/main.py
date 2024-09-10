from models.pessoa import Pessoa
from models.enums.generos import Generos
from models.endereco import Endereco
from models.enums.unidadefederativa import UnidadeFederativa

import os

os.system ("cls || clear")

pessoaUm = Pessoa(4525, "Marta", "14/08/1999", "71988445720", "marta@hotmail.com", 
                  Generos.FEMININO, Endereco("Avenida Afonso", "58", "Ao lado do posto", 
                                             "45871-589", "Salvador", UnidadeFederativa.BAHIA))

print(pessoaUm)


