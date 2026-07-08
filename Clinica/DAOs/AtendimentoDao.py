from DAOs.DAO import DAO
from Entidades.Atendimento import Atendimento

class AtendimentoDAO(DAO):
    def __init__(self):
        super().__init__('atendimentos.pkl')

    def add(self, atendimento: Atendimento):
        if (atendimento is not None) and isinstance(atendimento, Atendimento) and isinstance(atendimento.id, int):
            super().add(atendimento.id, atendimento)

    def update(self, atendimento: Atendimento):
        if (atendimento is not None) and isinstance(atendimento, Atendimento) and isinstance(atendimento.id, int):
            super().add(atendimento.id, atendimento)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            super().remove(key)