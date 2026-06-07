from Limites.LimiteRelatorio import LimiteRelatorio

class ControladorRelatorio:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__limite_relatorio = LimiteRelatorio()

    # --- MÉTODO AUXILIAR ---
    def __obter_atendimentos(self):
        """Busca a lista de instâncias de Atendimento através do ControladorSistema."""
        # Supondo que você criou uma @property 'controlador_atendimentos' no ControladorSistema
        # e uma @property 'atendimentos' no ControladorAtendimento que retorna a lista.
        return self.__controlador_sistema.controlador_atendimentos.atendimentos

    # --- 1. CLÍNICAS COM MAIOR NÚMERO DE ATENDIMENTOS ---
    def emitir_clinicas_mais_atendimentos(self):
        atendimentos = self.__obter_atendimentos()
        if not atendimentos:
            self.__limite_relatorio.mostrar_mensagem("Não há atendimentos para gerar relatório.")
            return

        contagem_clinicas = {}
        for at in atendimentos:
            nome_clinica = at.clinica.nome
            if nome_clinica in contagem_clinicas:
                contagem_clinicas[nome_clinica] += 1
            else:
                contagem_clinicas[nome_clinica] = 1

        # Ordena o dicionário pelo número de atendimentos (do maior para o menor)
        ranking = sorted(contagem_clinicas.items(), key=lambda item: item[1], reverse=True)
        
        # Envia a lista ordenada para a View
        self.__limite_relatorio.mostrar_relatorio_clinicas(ranking)

    # --- 2. ATENDIMENTOS MAIS CAROS E MAIS BARATOS ---
    def emitir_atendimentos_extremos(self):
        atendimentos = self.__obter_atendimentos()
        if not atendimentos:
            self.__limite_relatorio.mostrar_mensagem("Não há atendimentos para gerar relatório.")
            return

        # Inicializa com o primeiro elemento para ter uma base de comparação
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

    # --- 3. PROCEDIMENTOS MAIS REALIZADOS ---
    def emitir_procedimentos_populares(self):
        atendimentos = self.__obter_atendimentos()
        if not atendimentos:
            self.__limite_relatorio.mostrar_mensagem("Não há atendimentos para gerar relatório.")
            return

        contagem_procedimentos = {}
        for at in atendimentos:
            # Assumindo que a classe Atendimento tem uma @property 'procedimentos' que retorna a lista
            for proc in at.procedimentos: 
                desc = proc.descricao
                if desc in contagem_procedimentos:
                    contagem_procedimentos[desc] += 1
                else:
                    contagem_procedimentos[desc] = 1

        if not contagem_procedimentos:
            self.__limite_relatorio.mostrar_mensagem("Nenhum procedimento foi registrado nos atendimentos.")
            return

        # Ordena do mais popular para o menos popular
        ranking = sorted(contagem_procedimentos.items(), key=lambda item: item[1], reverse=True)
        self.__limite_relatorio.mostrar_relatorio_procedimentos_populares(ranking)

    # --- 4. PROCEDIMENTOS MAIS CAROS E MAIS BARATOS ---
    def emitir_procedimentos_extremos(self):
        atendimentos = self.__obter_atendimentos()
        if not atendimentos:
            self.__limite_relatorio.mostrar_mensagem("Não há atendimentos para gerar relatório.")
            return

        todos_procedimentos = []
        for at in atendimentos:
            todos_procedimentos.extend(at.procedimentos)

        if not todos_procedimentos:
            self.__limite_relatorio.mostrar_mensagem("Nenhum procedimento foi registrado para análise.")
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

    # --- MENU PRINCIPAL DO MÓDULO ---
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
            funcao_escolhida = opcoes.get(opcao)
            
            if funcao_escolhida:
                funcao_escolhida()
                if opcao == 0:
                    break
            else:
                self.__limite_relatorio.mostrar_mensagem("Opção inválida!")

    def retornar(self):
        pass