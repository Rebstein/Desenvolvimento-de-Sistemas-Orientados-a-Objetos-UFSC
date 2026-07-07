from DAOs.DAO import DAO
from Entidades.Paciente import Paciente

class PacienteDAO(DAO):
    def __init__(self):
        super().__init__('pacientes.pkl') # Define o nome do arquivo que será salvo

    def add(self, paciente: Paciente):
        # Valida se é realmente um objeto Paciente e se tem um CPF válido
        if (paciente is not None) and isinstance(paciente, Paciente) and isinstance(paciente.cpf, str):
            super().add(paciente.cpf, paciente)

    def update(self, paciente: Paciente):
        # O update faz a mesma coisa que o add: substitui o objeto antigo pelo novo no dicionário e dá dump
        if (paciente is not None) and isinstance(paciente, Paciente) and isinstance(paciente.cpf, str):
            super().add(paciente.cpf, paciente)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)