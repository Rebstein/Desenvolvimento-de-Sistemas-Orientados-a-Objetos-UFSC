import sys

from .ControladorPaciente import ControladorPaciente
from .ControladorAtendimento import ControladorAtendimento

class ControladorSistema:
    def __init__(self):
        self.__controlador_pacientes = ControladorPaciente(self)
        self.__controlador_atendimentos = ControladorAtendimento(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_paciente(self):
        return self.__controlador_pacientes
    
    def inicializar_sistema(self):
        self.controlador_paciente.abrir_tela_paciente()

    def encerrar_sistema(self):
        sys.exit(0)
        

    