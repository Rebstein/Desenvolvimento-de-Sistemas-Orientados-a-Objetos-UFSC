from Entidades.Paciente import Paciente
from Limites.LimitePaciente import LimitePaciente
from DAOs.PacienteDao import PacienteDAO


class ControladorPaciente:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__paciente_dao = PacienteDAO()
        self.__limite_paciente = LimitePaciente()

    def buscar_paciente_por_cpf(self, cpf: str) -> Paciente | None:
        if not cpf:  # Proteção extra contra buscas vazias
            return None
        return self.__paciente_dao.get(cpf)

    def incluir_paciente(self):
        dados_paciente = self.__limite_paciente.pegar_dados_paciente()
        
        # Cancelar operação se retornar None
        if dados_paciente is None:
            return
        
        if self.buscar_paciente_por_cpf(dados_paciente["cpf"]) is not None:
            self.__limite_paciente.mostrar_mensagem("Erro: Já existe um paciente cadastrado com este CPF!")
            return

        try:
            novo_paciente = Paciente(
                dados_paciente["nome"],
                dados_paciente["cpf"],
                dados_paciente["celular"],
                dados_paciente["data_nascimento"]
            )
            self.__paciente_dao.add(novo_paciente)
            self.__limite_paciente.mostrar_mensagem("Paciente cadastrado com sucesso!")
        except Exception as e:
            self.__limite_paciente.mostrar_mensagem(f"Erro inesperado ao cadastrar paciente: {e}")

    def listar_pacientes(self):
        pacientes = self.__paciente_dao.get_all()
        if len(pacientes) == 0:
            self.__limite_paciente.mostrar_mensagem("Nenhum paciente cadastrado no sistema.")
            return

        dados_pacientes = []
        for paciente in pacientes:
            dados_pacientes.append({
                "nome": paciente.nome,
                "celular": paciente.celular,
                "cpf": paciente.cpf,
                "data_nascimento": paciente.data_nascimento
            })
            
        self.__limite_paciente.mostrar_pacientes(dados_pacientes)

    def alterar_paciente(self):
        pacientes = self.__paciente_dao.get_all()
        if len(pacientes) == 0:
            self.__limite_paciente.mostrar_mensagem("Nenhum paciente cadastrado no sistema.")
            return

        cpf_paciente = self.__limite_paciente.selecionar_paciente()
        
        # Cancelar se a seleção retornar None
        if cpf_paciente is None:
            return

        paciente = self.buscar_paciente_por_cpf(cpf_paciente)
        if paciente is None:
            self.__limite_paciente.mostrar_mensagem("Erro: Paciente não encontrado!")
            return

        novos_dados = self.__limite_paciente.pegar_dados_paciente()
        
        # Cancelar se o formulário retornar None
        if novos_dados is None:
            return

        if novos_dados["cpf"] != paciente.cpf:
            if self.buscar_paciente_por_cpf(novos_dados["cpf"]) is not None:
                self.__limite_paciente.mostrar_mensagem("Erro: Já existe outro paciente com este novo CPF!")
                return
            self.__paciente_dao.remove(paciente.cpf)

        paciente.nome = novos_dados["nome"]
        paciente.celular = novos_dados["celular"]
        paciente.cpf = novos_dados["cpf"]
        paciente.data_nascimento = novos_dados["data_nascimento"]
        
        self.__paciente_dao.update(paciente)

        self.__limite_paciente.mostrar_mensagem("Dados do paciente alterados com sucesso!")

    def excluir_paciente(self):
        pacientes = self.__paciente_dao.get_all()
        if len(pacientes) == 0:
            self.__limite_paciente.mostrar_mensagem("Nenhum paciente cadastrado no sistema.")
            return

        cpf_paciente = self.__limite_paciente.selecionar_paciente()
        
        # Cancelar se a seleção retornar None
        if cpf_paciente is None:
            return

        paciente = self.buscar_paciente_por_cpf(cpf_paciente)
        if paciente is None:
            self.__limite_paciente.mostrar_mensagem("Erro: Paciente não encontrado!")
        else:
            self.__paciente_dao.remove(paciente.cpf)
            self.__limite_paciente.mostrar_mensagem(f"Paciente '{paciente.nome}' excluído com sucesso!")

    def abrir_menu(self):
        opcoes = {
            1: self.incluir_paciente,
            2: self.listar_pacientes,
            3: self.alterar_paciente,
            4: self.excluir_paciente,
            0: self.retornar
        }

        while True:
            opcao = self.__limite_paciente.tela_opcoes()
            if opcao == -1:
                self.__controlador_sistema.encerrar_sistema()
                break

            funcao_escolhida = opcoes.get(opcao)
            
            if funcao_escolhida:
                funcao_escolhida()
                if opcao == 0:  
                    break
            else:
                self.__limite_paciente.mostrar_mensagem("Opção inválida! Digite um número válido.")

    def retornar(self):
        pass