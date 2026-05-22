from datetime import date
import Clinica.Entidades.Pagamento.Pagamento as Pagamento

class PagamentoPix(Pagamento):
    def __init__(self, data: date, valor_pago: float, cpf_pagador: str):
        super().__init__(data, valor_pago)
        self.__cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self): 
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, cpf: str): 
        self.__cpf_pagador = cpf