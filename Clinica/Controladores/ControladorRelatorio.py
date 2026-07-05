from Limites.LimiteRelatorio import LimiteRelatorio

class ControladorRelatorio:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__limite_relatorio = LimiteRelatorio()

    def __obter_atendimentos(self):
        """Busca a lista de instâncias de Atendimento através do ControladorSistema."""
        try:
            return self.__controlador_sistema.controlador_atendimentos.atendimentos
        except AttributeError:
            return []

    def emitir_clinicas_mais_atendimentos(self):
        atendimentos = self.__obter_atendimentos()
        if not atendimentos or len(atendimentos) == 0:
            self.__limite_relatorio.mostrar_mensagem("Não há atendimentos registrados para gerar o relatório de clínicas.")
            return

        contagem_clinicas = {}
        for at in atendimentos:
            if at.clinica and at.clinica.nome:
                nome_clinica = at.clinica.nome
                contagem_clinicas[nome_clinica] = contagem_clinicas.get(nome_clinica, 0) + 1

        if not contagem_clinicas:
            self.__limite_relatorio.mostrar_mensagem("Nenhum dado válido de clínicas foi encontrado.")
            return

        ranking = sorted(contagem_clinicas.items(), key=lambda item: item[1], reverse=True)
        self.__limite_relatorio.mostrar_relatorio_clinicas(ranking)

    def emitir_atendimentos_extremos(self):
        atendimentos = self.__obter_atendimentos()
        if not atendimentos or len(atendimentos) == 0:
            self.__limite_relatorio.mostrar_mensagem("Não há atendimentos registrados para gerar o relatório de extremos.")
            return

        mais_caro = atendimentos[0]
        mais_barato = atendimentos[0]

        for at in atendimentos:
            if at.valor_total > mais_caro.valor_total:
                mais_caro = at
            if at.valor_total < mais_barato.valor_total:
                mais_barato = at

        dados = {
            "caro_id": atendimentos.index(mais_caro),
            "caro_valor": mais_caro.valor_total,
            "caro_data": mais_caro.data,
            "barato_id": atendimentos.index(mais_barato),
            "barato_valor": mais_barato.valor_total,
            "barato_data": mais_barato.data
        }
        self.__limite_relatorio.mostrar_relatorio_atendimentos_extremos(dados)

    def emitir_procedimentos_populares(self):
        atendimentos = self.__obter_atendimentos()
        if not atendimentos or len(atendimentos) == 0:
            self.__limite_relatorio.mostrar_mensagem("Não há atendimentos registrados para analisar procedimentos.")
            return

        contagem_procedimentos = {}
        for at in atendimentos:
            for proc in at.procedimentos: 
                desc = proc.descricao
                contagem_procedimentos[desc] = contagem_procedimentos.get(desc, 0) + 1

        if not contagem_procedimentos:
            self.__limite_relatorio.mostrar_mensagem("Nenhum procedimento foi registrado nos atendimentos até o momento.")
            return

        ranking = sorted(contagem_procedimentos.items(), key=lambda item: item[1], reverse=True)
        self.__limite_relatorio.mostrar_relatorio_procedimentos_populares(ranking)

    def emitir_procedimentos_extremos(self):
        atendimentos = self.__obter_atendimentos()
        if not atendimentos or len(atendimentos) == 0:
            self.__limite_relatorio.mostrar_mensagem("Não há atendimentos para analisar o custo de procedimentos.")
            return

        todos_procedimentos = []
        for at in atendimentos:
            todos_procedimentos.extend(at.procedimentos)

        if not todos_procedimentos:
            self.__limite_relatorio.mostrar_mensagem("Nenhum procedimento foi encontrado para análise de valores.")
            return

        mais_caro = todos_procedimentos[0]
        mais_barato = todos_procedimentos[0]

        for proc in todos_procedimentos:
            if proc.custo > mais_caro.custo:
                mais_caro = proc
            if proc.custo < mais_barato.custo:
                mais_barato = proc

        dados = {
            "caro_desc": mais_caro.descricao,
            "caro_custo": mais_caro.custo,
            "barato_desc": mais_barato.descricao,
            "barato_custo": mais_barato.custo
        }
        self.__limite_relatorio.mostrar_relatorio_procedimentos_extremos(dados)

    def abrir_menu(self):
        opcoes = {
            1: self.emitir_clinicas_mais_atendimentos,
            2: self.emitir_atendimentos_extremos,
            3: self.emitir_procedimentos_populares,
            4: self.emitir_procedimentos_extremos,
            0: self.retornar
        }

        while True:
            opcao = self.__limite_relatorio.tela_opcoes()
            
            # Se fechar a janela no X ou Cancelar (-1 ou None), sai do menu ou trata adequadamente
            if opcao == 0:
                break
            elif opcao in [1, 2, 3, 4]:
                opcoes[opcao]()
            else:
                # Evita loops infinitos de popups se a janela for fechada incorretamente
                if opcao is None or opcao == -1:
                    break
                self.__limite_relatorio.mostrar_mensagem("Opção inválida!")

    def retornar(self):
        pass