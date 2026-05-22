class Clinica:
  def __init__(self, nome: str, cidade: str, descricao: str):
    self._nome = nome
    self._cidade = cidade
    self._descricao = descricao
  
  @property
  def nome(self) -> str:
    return self._nome
  @nome.setter
  def nome(self, nome: str):
    self._nome = nome

  @property
  def cidade(self) -> str:
    return self._cidade
  @cidade.setter
  def cidade(self, cidade: str):
    self._cidade = cidade
  
  @property
  def descricao(self) -> str:
    return self._descricao
  @descricao.setter
  def descricao(self, descricao: str):
    self._descricao = descricao
