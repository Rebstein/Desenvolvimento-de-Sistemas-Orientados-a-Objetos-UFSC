from datetime import date
from Entidades.Pagamento.Pagamento import Pagamento
from Entidades.Atendimento import Atendimento
from Entidades.Paciente import Paciente

class PagamentoDinheiro(Pagamento):
    def __init__(self, data: date, atendimento: Atendimento, paciente: Paciente, valor_pago: float):
        super().__init__(data, atendimento, paciente, valor_pago)

    # Método abstrato
    def detalhar_pagamento(self) -> str:
        return f"Pagamento em dinheiro no valor de R${self.valor_pago:.2f} efetuado."