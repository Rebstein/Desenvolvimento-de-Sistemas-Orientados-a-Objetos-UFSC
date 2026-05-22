from datetime import date
import Pessoa

class Paciente(Pessoa):
  def __init__(self, nome: str, cpf:str, celular: str, data_nascimento: date):
    super().__init__(nome, cpf, celular)
    self.__data_nascimento = data_nascimento

  @property
  def data_nascimeto(self) -> date:
    return self.__data_nascimento
  
  @data_nascimeto.setter
  def data_nascimento(self, data: date):
    self.__data_nascimento = data
