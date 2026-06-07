from datetime import date
from Entidades.Pagamento import Pagamento
from Entidades.Atendimento import Atendimento
from Entidades.Paciente import Paciente

class PagamentoCartao(Pagamento):
    def __init__(self, data: date, atendimento: Atendimento, paciente: Paciente, valor_pago: float, numero: int, bandeira: str):
        super().__init__(data, atendimento, paciente, valor_pago)
        self.__numero = numero
        self.__bandeira = bandeira

    @property
    def numero(self): 
        return self.__numero

    @numero.setter
    def numero(self, numero: int): 
        self.__numero = numero

    @property
    def bandeira(self): 
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, bandeira: str): 
        self.__bandeira = bandeira

    # Método abstrato
    def detalhar_pagamento(self) -> str:
        return f"Pagamento via Cartão {self.bandeira} no valor de R${self.valor_pago:.2f} efetuado."
