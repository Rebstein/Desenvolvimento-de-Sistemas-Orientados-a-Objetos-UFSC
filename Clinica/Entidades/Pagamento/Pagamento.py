from abc import ABC, abstractmethod
from datetime import date
from Entidades.Atendimento import Atendimento
from Entidades.Paciente import Paciente

class Pagamento(ABC):
    def __init__(self, data: date, atendimento: Atendimento, paciente: Paciente, valor_pago: float):
        self.__data = data
        self.__atendimento = atendimento
        self.__paciente = paciente
        self.__valor_pago = valor_pago

    @property
    def data(self): 
        return self.__data

    @data.setter
    def data(self, data: date): 
        self.__data = data

    @property
    def atendimento(self): 
        return self.__atendimento

    @atendimento.setter
    def atendimento(self, atendimento: Atendimento): 
        self.__atendimento = atendimento

    @property
    def paciente(self): 
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente): 
        self.__paciente = paciente

    @property
    def valor_pago(self): 
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, valor_pago: float): 
        self.__valor_pago = valor_pago

    @abstractmethod
    def detalhar_pagamento(self) -> str:
        pass