import Profissional

class Procedimento:
  def __init__(self, descricao_procedimento: str, custo: float, profissional_responsavel: Profissional):
    self.__descricao_procedimento = descricao_procedimento
    self.__custo = custo
    self.__profissional_responsavel = profissional_responsavel

  @property
  def descricao_procedimento(self) -> str:
    return self.__descricao_procedimento
  
  @descricao_procedimento.setter
  def descricao_procedimento(self, descricao_procedimento: str):
    self.__descricao_procedimento = descricao_procedimento

  @property
  def custo(self) -> float:
    return self.__custo
  
  @custo.setter
  def custo(self, custo: float):
    self.__custo = custo

  @property
  def profissional_responsavel(self): 
    return self.__profissional_responsavel

  @profissional_responsavel.setter
  def profissional_responsavel(self, profissional_responsavel: Profissional): 
    self.__profissional_responsavel = profissional_responsavel
