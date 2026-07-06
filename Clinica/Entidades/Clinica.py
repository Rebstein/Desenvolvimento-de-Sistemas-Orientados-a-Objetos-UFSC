class Clinica:
  def __init__(self, nome: str, cidade: str, descricao: str, horario_inicio: str, horario_fim: str):
    self.__nome = nome
    self.__cidade = cidade
    self.__descricao = descricao
    self.__horario_funcionamento_inicio = horario_inicio
    self.__horario_funcionamento_fim = horario_fim

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
    self.__cidade = cidade
  
  @property
  def descricao(self) -> str:
    return self.__descricao
  
  @descricao.setter
  def descricao(self, descricao: str):
    self.__descricao = descricao

  @property
  def horario_funcionamento_inicio(self) -> str:
    return self.__horario_funcionamento_inicio

  @horario_funcionamento_inicio.setter
  def horario_funcionamento_inicio(self, horario_inicio: str):
    self.__horario_funcionamento_inicio = horario_inicio

  @property
  def horario_funcionamento_fim(self) -> str:
    return self.__horario_funcionamento_fim

  @horario_funcionamento_fim.setter
  def horario_funcionamento_fim(self, horario_fim: str):
    self.__horario_funcionamento_fim = horario_fim

  @property
  def atendimentos(self) -> list:
    return self.__atendimentos
  
  @atendimentos.setter
  def atendimentos(self, atendimentos: list):
    self.__atendimentos = atendimentos