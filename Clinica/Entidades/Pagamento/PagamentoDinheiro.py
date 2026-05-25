from datetime import date
from Pagamento import Pagamento

class PagamentoDinheiro(Pagamento):
    def __init__(self, data: date, atendimento: Atendimento, paciente: Paciente, valor_pago: float):
        super().__init__(data, atendimento, paciente, valor_pago)
