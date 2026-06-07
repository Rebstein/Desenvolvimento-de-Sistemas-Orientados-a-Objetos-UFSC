from datetime import date
from Pessoa import Pessoa

class Paciente(Pessoa):
  def __init__(self, nome: str, cpf:str, celular: str, data_nascimento: date):
    super().__init__(nome, cpf, celular)
    self.__data_nascimento = data_nascimento

  @property
  def data_nascimento(self) -> date:
    return self.__data_nascimento
  
  @data_nascimento.setter
  def data_nascimento(self, data_nascimento: date):
    self.__data_nascimento = data_nascimento

  # Método abstrato
  def get_tipo(self) -> str:
    return "Paciente"
