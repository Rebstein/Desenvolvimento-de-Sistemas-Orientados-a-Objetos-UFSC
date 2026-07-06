import PySimpleGUI as sg

class LimiteRelatorio:
    def tela_opcoes(self):
        sg.theme('BlueMono')
        
        # Padrão de tamanho e fonte para os botões
        fonte_botoes = ("Courier New", 12)
        tamanho_botoes = (48, 1) 
        
        layout = [
            [sg.Text("RELATÓRIOS", font=("Courier New", 16, "bold"), text_color='white', pad=(0, 15))],
            [sg.Button("Clínicas com maior número de atendimentos", key=1, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Atendimentos mais caros e mais baratos", key=2, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Procedimentos mais populares", key=3, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Procedimentos mais caros e mais baratos", key=4, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Retornar", key=0, size=tamanho_botoes, font=fonte_botoes, button_color=('white', 'darkblue'), pad=(0, 15))]
        ]
        window = sg.Window("Relatórios", layout, element_justification='c')
        evento, _ = window.read()
        window.close()
        
        if evento is None or evento == -1:
            return -1
        return evento

    # Mensagem de popup
    def mostrar_mensagem(self, msg: str):
        sg.popup(f"[RELATÓRIO]: {msg}", title="Módulo Relatórios", color='white', font=("Courier New", 12))

    def mostrar_relatorio_clinicas(self, ranking: list):
        texto = "CLÍNICAS COM MAIS ATENDIMENTOS\n\n"
        for posicao, (clinica, quantidade) in enumerate(ranking, start=1):
            texto += f"{posicao}º - {clinica}: {quantidade} atendimento(s)\n"
        sg.popup_scrolled(texto, title="Relatório Clínicas", size=(55, 12), text_color='white', font=("Courier New", 12))

    def mostrar_relatorio_atendimentos_extremos(self, dados: dict):
        texto = "ATENDIMENTOS EXTREMOS\n\n"
        texto += "-> MAIS CARO:\n"
        texto += f"   ID: {dados['caro_id']} | Data: {dados['caro_data']} | Valor: R${dados['caro_valor']:.2f}\n\n"
        texto += "-> MAIS BARATO:\n"
        texto += f"   ID: {dados['barato_id']} | Data: {dados['barato_data']} | Valor: R${dados['barato_valor']:.2f}\n"
        sg.popup(texto, title="Relatório Atendimentos Extremos", text_color='white', font=("Courier New", 12))

    def mostrar_relatorio_procedimentos_populares(self, ranking: list):
        texto = "PROCEDIMENTOS MAIS POPULARES\n\n"
        for posicao, (proc, quantidade) in enumerate(ranking, start=1):
            texto += f"{posicao}º - {proc}: realizado {quantidade} vez(es)\n"
        sg.popup_scrolled(texto, title="Relatório Procedimentos Populares", size=(55, 12), text_color='white', font=("Courier New", 12))

    def mostrar_relatorio_procedimentos_extremos(self, dados: dict):
        texto = "PROCEDIMENTOS EXTREMOS\n\n"
        texto += "-> MAIS CARO:\n"
        texto += f"   {dados['caro_desc']} - Custo: R${dados['caro_custo']:.2f}\n\n"
        texto += "-> MAIS BARATO:\n"
        texto += f"   {dados['barato_desc']} - Custo: R${dados['barato_custo']:.2f}\n"
        sg.popup(texto, title="Relatório Procedimentos Extremos", text_color='white', font=("Courier New", 12))