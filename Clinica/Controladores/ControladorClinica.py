from Entidades.Clinica import Clinica
from Limites.LimitesClinica import LimiteClinica

class ControladorCLinica:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        #onde as clinicas vão ser armazenadas
        self.__clinicas = []
        #relação com a tela clinica
        self.__limite_clinica = LimiteClinica()

    def buscar_clinica_por_nome(self, nome: str) -> Clinica | None:
        """busca uma clínica pelo nome e retorna o objeto. Retorna None se não encontrar."""
        for clinica in self.__clinicas:
            if clinica.nome.upper() == nome.upper():
                return clinica
        return None

    def incluir_clinica(self):
        dados_clinica = self.__limite_clinica.pegar_dados_clinica()
        
        # Validação de unicidade
        if self.buscar_clinica_por_nome(dados_clinica["nome"]) is not None:
            self.__limite_clinica.mostrar_mensagem("Erro: Já existe uma clínica cadastrada com este nome!")
            return

        try:
            nova_clinica = Clinica(
                dados_clinica["nome"],
                dados_clinica["cidade"],
                dados_clinica["descricao"]
            )
            self.__clinicas.append(nova_clinica)
            self.__limite_clinica.mostrar_mensagem("Clínica cadastrada com sucesso!")
        except Exception as e:
            self.__limite_clinica.mostrar_mensagem(f"Erro inesperado ao cadastrar a clínica: {e}")

    def listar_clinicas(self):
        if len(self.__clinicas) == 0:
            self.__limite_clinica.mostrar_mensagem("Nenhuma clínica cadastrada no sistema.")
            return

        # Preparar os dados para a Tela (evitando passar o objeto Entidade direto)
        dados_clinicas = []
        for clinica in self.__clinicas:
            dados_clinicas.append({
                "nome": clinica.nome,
                "cidade": clinica.cidade,
                "descricao": clinica.descricao
            })
            
        self.__limite_clinica.mostrar_clinicas(dados_clinicas)

    def alterar_clinica(self):
        self.listar_clinicas()
        if len(self.__clinicas) == 0:
            return

        nome_clinica = self.__limite_clinica.selecionar_clinica()
        clinica = self.buscar_clinica_por_nome(nome_clinica)

        if clinica is None:
            self.__limite_clinica.mostrar_mensagem("Erro: Clínica não encontrada!")
            return

        self.__limite_clinica.mostrar_mensagem(f"Alterando dados da clínica: {clinica.nome}")
        novos_dados = self.__limite_clinica.pegar_dados_clinica()

        # Verifica se o novo nome já existe (desde que não seja o nome atual da própria clínica)
        if novos_dados["nome"].upper() != clinica.nome.upper():
            if self.buscar_clinica_por_nome(novos_dados["nome"]) is not None:
                self.__limite_clinica.mostrar_mensagem("Erro: Já existe outra clínica com este novo nome!")
                return

        # Atualizando os dados usando as propriedades (setters) da entidade
        clinica.nome = novos_dados["nome"]
        clinica.cidade = novos_dados["cidade"]
        clinica.descricao = novos_dados["descricao"]
        
        self.__limite_clinica.mostrar_mensagem("Dados da clínica alterados com sucesso!")

    def excluir_clinica(self):
        self.listar_clinicas()
        if len(self.__clinicas) == 0:
            return

        nome_clinica = self.__limite_clinica.selecionar_clinica()
        clinica = self.buscar_clinica_por_nome(nome_clinica)

        if clinica is None:
            self.__limite_clinica.mostrar_mensagem("Erro: Clínica não encontrada!")
        else:
            self.__clinicas.remove(clinica)
            self.__limite_clinica.mostrar_mensagem(f"Clínica '{clinica.nome}' excluída com sucesso!")

    def abrir_menu(self):
        opcoes = {
            1: self.incluir_clinica,
            2: self.listar_clinicas,
            3: self.alterar_clinica,
            4: self.excluir_clinica,
            0: self.retornar
        }

        while True:
            opcao = self.__limite_clinica.tela_opcoes()
            funcao_escolhida = opcoes.get(opcao)
            
            if funcao_escolhida:
                funcao_escolhida()
                if opcao == 0:
                    break
            else:
                self.__limite_clinica.mostrar_mensagem("Opção inválida! Digite um número válido.")

    def retornar(self):
        pass