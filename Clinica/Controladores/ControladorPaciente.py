from Entidades.Paciente import Paciente

class ControladorPaciente:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__pacientes = []

    def buscar_paciente_por_cpf(self, cpf: str) -> Paciente | None:
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                return paciente
        return None
    
    # Para incluir um paciente, verificamos se o CPF já existe na lista de pacientes. 
    # Se existir, lançamos uma exceção para evitar a duplicidade de pacientes.

    def incluir_paciente(self, nome, cpf, telefone, data_nascimento):
        paciente = Paciente(nome, cpf, telefone, data_nascimento)

        if self.buscar_paciente_por_cpf(cpf) is not None:
            raise ValueError("Paciente com CPF já cadastrado.")
            return
        try:
            paciente = Paciente(nome, cpf, telefone, data_nascimento)
            self.__pacientes.append(paciente)
            self.__tela_paciente.mostrar_mensagem("Paciente cadastrado com sucesso!")  
        except ValueError as e:
            pass #revisar depois


    # Para listar os pacientes, englobamos os dados em um dicionário para facilitar a vizualização dos dados na tela.
    def listar_pacientes(self):

        dados_pacientes = []

        for paciente in self.__pacientes:
            dados_pacientes.append({"nome": paciente.nome, 
                                    "cpf": paciente.cpf, 
                                    "telefone": paciente.celular, 
                                    "data_nascimento": paciente.data_nascimento})
            
        self.__tela_paciente.mostrar_pacientes(dados_pacientes)