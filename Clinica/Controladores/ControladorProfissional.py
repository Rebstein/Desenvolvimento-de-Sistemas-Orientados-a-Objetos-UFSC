from Entidades.Profissional import Profissional
from Limites.LimiteProfissional import LimiteProfissional

class ControladorProfissional:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__profissionais = []
        self.__limite_profissional = LimiteProfissional()

    def buscar_profissional_por_cpf(self, cpf: str) -> Profissional | None:
        """Busca um profissional pelo CPF e retorna o objeto. Retorna None se não encontrar."""
        for profissional in self.__profissionais:
            if profissional.cpf == cpf:
                return profissional
        return None

    def incluir_profissional(self):
        dados_profissional = self.__limite_profissional.pegar_dados_profissional()
        
        # Validação de unicidade pelo CPF
        if self.buscar_profissional_por_cpf(dados_profissional["cpf"]) is not None:
            self.__limite_profissional.mostrar_mensagem("Erro: Já existe um profissional cadastrado com este CPF!")
            return

        try:
            # Instancia a Entidade com os dados da classe mãe (Pessoa) e os específicos (Profissional)
            novo_profissional = Profissional(
                dados_profissional["nome"],
                dados_profissional["cpf"],
                dados_profissional["celular"],
                dados_profissional["especialidade"],
                dados_profissional["registro_profissional"]
            )
            self.__profissionais.append(novo_profissional)
            self.__limite_profissional.mostrar_mensagem("Profissional cadastrado com sucesso!")
        except Exception as e:
            self.__limite_profissional.mostrar_mensagem(f"Erro inesperado ao cadastrar profissional: {e}")

    def listar_profissionais(self):
        if len(self.__profissionais) == 0:
            self.__limite_profissional.mostrar_mensagem("Nenhum profissional cadastrado no sistema.")
            return

        # Preparar os dados para enviar à Tela, mantendo o encapsulamento dos objetos
        dados_profissionais = []
        for profissional in self.__profissionais:
            dados_profissionais.append({
                "nome": profissional.nome,
                "celular": profissional.celular,
                "cpf": profissional.cpf,
                "especialidade": profissional.especialidade,
                "registro_profissional": profissional.registro_profissional
            })
            
        self.__limite_profissional.mostrar_profissionais(dados_profissionais)

    def alterar_profissional(self):
        self.listar_profissionais()
        if len(self.__profissionais) == 0:
            return

        cpf_profissional = self.__limite_profissional.selecionar_profissional()
        profissional = self.buscar_profissional_por_cpf(cpf_profissional)

        if profissional is None:
            self.__limite_profissional.mostrar_mensagem("Erro: Profissional não encontrado!")
            return

        self.__limite_profissional.mostrar_mensagem(f"Alterando dados do profissional: {profissional.nome}")
        novos_dados = self.__limite_profissional.pegar_dados_profissional()

        # Verifica se o CPF foi alterado para um que já existe
        if novos_dados["cpf"] != profissional.cpf:
            if self.buscar_profissional_por_cpf(novos_dados["cpf"]) is not None:
                self.__limite_profissional.mostrar_mensagem("Erro: Já existe outro profissional com este novo CPF!")
                return

        # Atualizando os dados através dos setters
        profissional.nome = novos_dados["nome"]
        profissional.celular = novos_dados["celular"]
        profissional.cpf = novos_dados["cpf"]
        profissional.especialidade = novos_dados["especialidade"]
        profissional.registro_profissional = novos_dados["registro_profissional"]
        
        self.__limite_profissional.mostrar_mensagem("Dados do profissional alterados com sucesso!")

    def excluir_profissional(self):
        self.listar_profissionais()
        if len(self.__profissionais) == 0:
            return

        cpf_profissional = self.__limite_profissional.selecionar_profissional()
        profissional = self.buscar_profissional_por_cpf(cpf_profissional)

        if profissional is None:
            self.__limite_profissional.mostrar_mensagem("Erro: Profissional não encontrado!")
        else:
            self.__profissionais.remove(profissional)
            self.__limite_profissional.mostrar_mensagem(f"Profissional '{profissional.nome}' excluído com sucesso!")

    def abrir_menu(self):
        opcoes = {
            1: self.incluir_profissional,
            2: self.listar_profissionais,
            3: self.alterar_profissional,
            4: self.excluir_profissional,
            0: self.retornar
        }

        while True:
            opcao = self.__limite_profissional.tela_opcoes()
            funcao_escolhida = opcoes.get(opcao)
            
            if funcao_escolhida:
                funcao_escolhida()
                if opcao == 0:
                    break
            else:
                self.__limite_profissional.mostrar_mensagem("Opção inválida! Digite um número válido.")

    def retornar(self):
        # Encerra o loop e volta para o menu principal
        pass