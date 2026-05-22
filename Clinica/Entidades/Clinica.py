class Clinica:
  def __init__(self, nome: str, cidade: str, descricao: str):
    self.__nome = nome
    self.__cidade = cidade
    self.__descricao = descricao

    #agregação com classe atendimentos
    self.__atendimentos = []
  
  @property
  def nome(self) -> str:
    return self.__nome
  
  @nome.setter
  def nome(self, nome: str):
    self.__nome = nome

  @property
  def cidade(self) -> str:
    return self.__cidade
  
  @cidade.setter
  def cidade(self, cidade: str):
    self._cidade = cidade
  
  @property
  def descricao(self) -> str:
    return self.__descricao
  
  @descricao.setter
  def descricao(self, descricao: str):
    self.__descricao = descricao

  @property
  def atendimentos(self) -> str:
    return self.__atendimentos
  
  @descricao.setter
  def atendimentos(self, atendimentos: str):
    self.__atendimentos = atendimentos