from enum import Enum

class TipoAtendimento(Enum):
    CONSULTA = 1
    RETORNO = 2
    EXAME = 3 
    PROCEDIMENTO = 4 
    EMERGÊNCIA = 5