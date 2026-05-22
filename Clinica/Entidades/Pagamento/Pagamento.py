from abc import ABC
from datetime import date
class Pagamento(ABC):
    def __init__(self, data: date, valor_pago: float):
        self.__data = data
        self.__valor_pago = valor_pago

    @property
    def data(self): return self.__data

    @data.setter
    def data(self, data: date): self.__data = data

    @property
    def valor_pago(self): return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, valor_pago: float): self.__valor_pago = valor_pago