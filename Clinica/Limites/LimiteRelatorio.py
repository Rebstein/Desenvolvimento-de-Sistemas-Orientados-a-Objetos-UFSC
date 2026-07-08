import PySimpleGUI as sg

class LimiteRelatorio:
    def tela_opcoes(self):
        sg.theme('BlueMono')
        
        # Padrão para botões (mais simples de fazer alterações)
        fonte_botoes = ("Courier New", 12)
        tamanho_botoes = (48, 1) 
        
        layout = [
            [sg.Text("RELATÓRIOS", font=("Courier New", 16, "bold"), text_color='white', pad=(0, 15))],
            [sg.Button("Clínicas com maior número de atendimentos", key=1, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Atendimentos mais caros e mais baratos", key=2, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Procedimentos mais populares", key=3, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Procedimentos mais caros e mais baratos", key=4, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Retornar", key=0, size=tamanho_botoes, font=fonte_botoes, button_color=('white', 'blue'), pad=(0, 15))]
        ]
        window = sg.Window("Relatórios", layout, element_justification='c')
        evento, _ = window.read()
        window.close()

        # Caso o usuário selecione 'X' (-1) ele fecha o sistema
        if evento is None or evento == -1:
            return -1
        return evento

    # Função para mostrar o ranking de clínicas com mais atendimentos
    def mostrar_relatorio_clinicas(self, ranking: list):
        texto = "CLÍNICAS COM MAIS ATENDIMENTOS\n\n"
        for posicao, (clinica, quantidade) in enumerate(ranking, start=1):
            texto += f"{posicao}º - {clinica}: {quantidade} atendimento(s)\n"
        sg.popup_scrolled(texto, title="Relatório Clínicas", size=(55, 12), font=("Courier New", 12), text_color="black")

    # Função para mostrar os atendimentos mais caros e mais baratos
    def mostrar_relatorio_atendimentos_extremos(self, dados: dict):
        texto = "ATENDIMENTOS EXTREMOS\n\n"
        texto += "ATENDIMENTOS MAIS CAROS:\n"
        texto += f"   ID: {dados['caro_id']} | Data: {dados['caro_data']} | Valor: R${dados['caro_valor']:.2f}\n\n"
        texto += "ATENDIMENTOS MAIS BARATOS:\n"
        texto += f"   ID: {dados['barato_id']} | Data: {dados['barato_data']} | Valor: R${dados['barato_valor']:.2f}\n"
        sg.popup_scrolled(texto, title="Relatório Atendimentos Extremos", size=(55, 12), font=("Courier New", 12), text_color="black")

    # Função para mostrar os procedimentos mais populares
    def mostrar_relatorio_procedimentos_populares(self, ranking: list):
        texto = "PROCEDIMENTOS MAIS POPULARES\n\n"
        for posicao, (proc, quantidade) in enumerate(ranking, start=1):
            texto += f"{posicao}º - {proc}: realizado {quantidade} vez(es)\n"
        sg.popup_scrolled(texto, title="Relatório Procedimentos Populares", size=(55, 12), font=("Courier New", 12), text_color="black")

    # Função para mostrar os procedimentos mais caros e mais baratos
    def mostrar_relatorio_procedimentos_extremos(self, dados: dict):
        texto = "PROCEDIMENTOS EXTREMOS\n\n"
        texto += "PROCEDIMENTOS MAIS CAROS:\n"
        texto += f"   {dados['caro_desc']} - Custo: R${dados['caro_custo']:.2f}\n\n"
        texto += "PROCEDIMENTOS MAIS BARATOS:\n"
        texto += f"   {dados['barato_desc']} - Custo: R${dados['barato_custo']:.2f}\n"
        sg.popup_scrolled(texto, title="Relatório Procedimentos Extremos", size=(55, 12), font=("Courier New", 12), text_color="black")
    
    # Padrão para mensagens do controlador
    def mostrar_mensagem(self, msg: str):
        sg.popup(f"[RELATÓRIO]: {msg}", title="Módulo Relatórios", text_color='white', font=("Courier New", 12))