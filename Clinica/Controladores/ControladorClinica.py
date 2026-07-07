from Entidades.Clinica import Clinica
from Limites.LimiteClinica import LimiteClinica
from DAOs.ClinicaDao import ClinicaDao

class ControladorClinica:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__clinica_dao = ClinicaDao()
        self.__limite_clinica = LimiteClinica()

    def buscar_clinica_por_nome(self, nome: str) -> Clinica | None:
        if not nome:  # Proteção extra contra buscas vazias
            return None
        return self.__clinica_dao.get(nome)

    def incluir_clinica(self):
        dados_clinica = self.__limite_clinica.pegar_dados_clinica()
        
        if dados_clinica is None:
            return

        if self.buscar_clinica_por_nome(dados_clinica["nome"]) is not None:
            self.__limite_clinica.mostrar_mensagem("Erro: Já existe uma clínica cadastrada com este nome!")
            return

        try:
            nova_clinica = Clinica(
                dados_clinica["nome"],
                dados_clinica["cidade"],
                dados_clinica["descricao"],
                dados_clinica["horario_inicio"],
                dados_clinica["horario_fim"]
                )
            self.__clinica_dao.add(nova_clinica)
            self.__limite_clinica.mostrar_mensagem("Clínica cadastrada com sucesso!")
        except Exception as e:
            self.__limite_clinica.mostrar_mensagem(f"Erro inesperado ao cadastrar a clínica: {e}")

    def listar_clinicas(self):
        # Substituímos a lista self.__clinicas pelo get_all() do DAO
        clinicas = self.__clinica_dao.get_all()
        
        if len(clinicas) == 0:
            self.__limite_clinica.mostrar_mensagem("Nenhuma clínica cadastrada no sistema.")
            return

        dados_clinicas = []
        for clinica in clinicas:
            dados_clinicas.append({
                "nome": clinica.nome,
                "cidade": clinica.cidade,
                "descricao": clinica.descricao,
                "horario_inicio": clinica.horario_funcionamento_inicio,
                "horario_fim": clinica.horario_funcionamento_fim
            })
            
        self.__limite_clinica.mostrar_clinicas(dados_clinicas)

    def alterar_clinica(self):
        clinicas = self.__clinica_dao.get_all()
        if len(clinicas) == 0:
            self.__limite_clinica.mostrar_mensagem("Nenhuma clínica cadastrada no sistema.")
            return

        nome_clinica = self.__limite_clinica.selecionar_clinica()
        
        if nome_clinica is None:
            return

        clinica = self.buscar_clinica_por_nome(nome_clinica)
        if clinica is None:
            self.__limite_clinica.mostrar_mensagem("Erro: Clínica não encontrada!")
            return

        novos_dados = self.__limite_clinica.pegar_dados_clinica()
        
        if novos_dados is None:
            return

        if novos_dados["nome"].upper() != clinica.nome.upper():
            if self.buscar_clinica_por_nome(novos_dados["nome"]) is not None:
                self.__limite_clinica.mostrar_mensagem("Erro: Já existe outra clínica com este novo nome!")
                return
            # Remove a clínica do dicionário com o nome antigo
            self.__clinica_dao.remove(clinica.nome)

        clinica.nome = novos_dados["nome"]
        clinica.cidade = novos_dados["cidade"]
        clinica.descricao = novos_dados["descricao"]
        clinica.horario_funcionamento_inicio = novos_dados["horario_inicio"]
        clinica.horario_funcionamento_fim = novos_dados["horario_fim"]

        self.__clinica_dao.update(clinica)
        
        self.__limite_clinica.mostrar_mensagem("Dados da clínica alterados com sucesso!")

    def excluir_clinica(self):
        clinicas = self.__clinica_dao.get_all()
        if len(clinicas) == 0:
            self.__limite_clinica.mostrar_mensagem("Nenhuma clínica cadastrada no sistema.")
            return

        nome_clinica = self.__limite_clinica.selecionar_clinica()
        
        if nome_clinica is None:
            return

        clinica = self.buscar_clinica_por_nome(nome_clinica)
        if clinica is None:
            self.__limite_clinica.mostrar_mensagem("Erro: Clínica não encontrada!")
        else:
            self.__clinica_dao.remove(clinica.nome)
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
            
            if opcao == -1:
                self.__controlador_sistema.encerrar_sistema()
                break

            funcao_escolhida = opcoes.get(opcao)
            
            if funcao_escolhida:
                funcao_escolhida()
                if opcao == 0:
                    break
            else:
                self.__limite_clinica.mostrar_mensagem("Opção inválida! Digite um número válido.")

    def retornar(self):
        pass