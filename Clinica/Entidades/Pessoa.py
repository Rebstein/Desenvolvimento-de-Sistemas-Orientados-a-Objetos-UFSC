from abc import ABC, abstractmethod

class Pessoa(ABC):
  def __init__(self, nome: str, cpf: str, celular: str):
    self.__nome = nome
    self.__cpf = cpf
    self.__celular = celular

  @property
  def nome(self) -> str:
    return self.__nome
  
  @nome.setter
  def nome(self, nome: str):
    self.__nome = nome

  @property
  def cpf(self) -> str:
    return self.__cpf
  
  @cpf.setter
  def cpf(self, cpf: str):
    self.__cpf = cpf

  @property
  def celular(self) -> str:
    return self.__celular
  
  @celular.setter
  def celular (self, celular: str):
    self.__celular = celular
