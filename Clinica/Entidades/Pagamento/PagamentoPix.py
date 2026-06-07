from datetime import date
from Entidades.Pagamento import Pagamento
from Entidades.Atendimento import Atendimento
from Entidades.Paciente import Paciente

class PagamentoPix(Pagamento):
    def __init__(self, data: date, atendimento: Atendimento, paciente: Paciente, valor_pago: float, cpf_pagador: str):
        super().__init__(data, atendimento, paciente, valor_pago)
        self.__cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self): 
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, cpf: str): 
        self.__cpf_pagador = cpf

    # Método abstrato
    def detalhar_pagamento(self) -> str:
        return f"Pagamento via PIX (CPF: {self.cpf_pagador}) no valor de R${self.valor_pago:.2f} efetuado."