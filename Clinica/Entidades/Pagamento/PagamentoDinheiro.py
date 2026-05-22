from datetime import date
import Clinica.Entidades.Pagamento.Pagamento as Pagamento

class PagamentoDinheiro(Pagamento):
    def __init__(self, data: date, valor_pago: float):
        super().__init__(data, valor_pago)