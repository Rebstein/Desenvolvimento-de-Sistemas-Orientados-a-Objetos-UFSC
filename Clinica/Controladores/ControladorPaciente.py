from Entidades.Paciente import Paciente
from Limites.LimitePaciente import LimitePaciente

class ControladorPaciente:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__pacientes = []
        self.__limite_paciente = LimitePaciente()

    def buscar_paciente_por_cpf(self, cpf: str) -> Paciente | None:
        """Busca um paciente pelo CPF e retorna o objeto. Retorna None se não encontrar."""
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                return paciente
        return None

    def incluir_paciente(self):
        dados_paciente = self.__limite_paciente.pegar_dados_paciente()
        
        # Validação de unicidade: O CPF é a chave primária
        if self.buscar_paciente_por_cpf(dados_paciente["cpf"]) is not None:
            self.__limite_paciente.mostrar_mensagem("Erro: Já existe um paciente cadastrado com este CPF!")
            return

        try:
            # Lembre-se que Paciente herda de Pessoa, então recebe os atributos da classe mãe também
            novo_paciente = Paciente(
                dados_paciente["nome"],
                dados_paciente["celular"],
                dados_paciente["cpf"],
                dados_paciente["data_nascimento"]
            )
            self.__pacientes.append(novo_paciente)
            self.__limite_paciente.mostrar_mensagem("Paciente cadastrado com sucesso!")
        except Exception as e:
            self.__limite_paciente.mostrar_mensagem(f"Erro inesperado ao cadastrar paciente: {e}")

    def listar_pacientes(self):
        if len(self.__pacientes) == 0:
            self.__limite_paciente.mostrar_mensagem("Nenhum paciente cadastrado no sistema.")
            return

        # Preparar os dados em formato de dicionário para enviar à Tela
        dados_pacientes = []
        for paciente in self.__pacientes:
            dados_pacientes.append({
                "nome": paciente.nome,
                "celular": paciente.celular,
                "cpf": paciente.cpf,
                "data_nascimento": paciente.data_nascimento
            })
            
        self.__limite_paciente.mostrar_pacientes(dados_pacientes)

    def alterar_paciente(self):
        self.listar_pacientes()
        if len(self.__pacientes) == 0:
            return

        cpf_paciente = self.__limite_paciente.selecionar_paciente()
        paciente = self.buscar_paciente_por_cpf(cpf_paciente)

        if paciente is None:
            self.__limite_paciente.mostrar_mensagem("Erro: Paciente não encontrado!")
            return

        self.__limite_paciente.mostrar_mensagem(f"Alterando dados do paciente: {paciente.nome}")
        novos_dados = self.__limite_paciente.pegar_dados_paciente()

        # Verifica se o usuário tentou alterar o CPF para um que já pertence a outra pessoa
        if novos_dados["cpf"] != paciente.cpf:
            if self.buscar_paciente_por_cpf(novos_dados["cpf"]) is not None:
                self.__limite_paciente.mostrar_mensagem("Erro: Já existe outro paciente com este novo CPF!")
                return

        # Atualizando os dados usando os setters da entidade
        paciente.nome = novos_dados["nome"]
        paciente.celular = novos_dados["celular"]
        paciente.cpf = novos_dados["cpf"]
        paciente.data_nascimento = novos_dados["data_nascimento"]
        
        self.__limite_paciente.mostrar_mensagem("Dados do paciente alterados com sucesso!")

    def excluir_paciente(self):
        self.listar_pacientes()
        if len(self.__pacientes) == 0:
            return

        cpf_paciente = self.__limite_paciente.selecionar_paciente()
        paciente = self.buscar_paciente_por_cpf(cpf_paciente)

        if paciente is None:
            self.__limite_paciente.mostrar_mensagem("Erro: Paciente não encontrado!")
        else:
            self.__pacientes.remove(paciente)
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
            funcao_escolhida = opcoes.get(opcao)
            
            if funcao_escolhida:
                funcao_escolhida()
                if opcao == 0:
                    break
            else:
                self.__limite_paciente.mostrar_mensagem("Opção inválida! Digite um número válido.")

    def retornar(self):
        pass