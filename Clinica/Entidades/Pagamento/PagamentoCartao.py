from datetime import date
import Clinica.Entidades.Pagamento.Pagamento as Pagamento

class PagamentoCartao(Pagamento):
    def __init__(self, data: date, atendimento: Atendimento, paciente: Paciente, valor_pago: float, numero: int, bandeira: str):
        super().__init__(data, atendimento, paciente, valor_pago)
        self.__numero = numero
        self.__bandeira = bandeira

    @property
    def numero(self): 
        return self.__numero

    @numero.setter
    def numero(self, numero: str): 
        self.__numero = numero

    @property
    def bandeira(self): 
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, bandeira: str): 
        self.__bandeira = bandeira
