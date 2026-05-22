from datetime import date
from datetime import time
import Clinica
import Paciente
import Profissional

class Atendimento:
    def __init__(self, clinica: Clinica, paciente: Paciente, profissional: Profissional, 
                 data_atendimento: date, horario_inicio: time, horario_fim: time, 
                 tipo_atendimento: str, valor_total: float):
        
        # atributos de Associação 
        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        
        # atributos Próprios
        self.__data_atendimento = data_atendimento
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__tipo_atendimento = tipo_atendimento
        self.__valor_total = valor_total
        
        # relações 0..* e 1..* (Composição)
        self.__procedimentos = []
        self.__pagamentos = []

    @property
    def clinica(self): 
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica: Clinica):
        self.__clinica = clinica

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente): 
        self.__paciente = paciente

    @property
    def profissional(self): 
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: Profissional): 
        self.__profissional = profissional

    @property
    def data_atendimento(self): 
        return self.__data_atendimento

    @data_atendimento.setter
    def data_atendimento(self, data: date): 
        self.__data_atendimento = data

    @property
    def horario_inicio(self): 
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, horario: time): 
        self.__horario_inicio = horario

    @property
    def horario_fim(self): 
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario: time): 
        self.__horario_fim = horario

    @property
    def tipo_atendimento(self): 
        return self.__tipo_atendimento

    @tipo_atendimento.setter
    def tipo_atendimento(self, tipo: str): 
        self.__tipo_atendimento = tipo

    @property
    def valor_total(self): 
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, valor: float): 
        self.__valor_total = valor

    @property
    def procedimentos(self): 
        return self.__procedimentos

    @procedimentos.setter
    def procedimentos(self, procedimentos: list): 
        self.__procedimentos = procedimentos

    @property
    def pagamentos(self): 
        return self.__pagamentos

    @pagamentos.setter
    def pagamentos(self, pagamentos: list): 
        self.__pagamentos = pagamentos