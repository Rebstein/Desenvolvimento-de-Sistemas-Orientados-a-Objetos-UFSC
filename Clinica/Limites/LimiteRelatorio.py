import PySimpleGUI as sg

class LimiteRelatorio:
    def tela_opcoes(self):
        sg.theme('LightGrey1')
        layout = [
            [sg.Text("RELATÓRIOS", font=("Helvetica", 12, "bold"), pad=(0, 10))],
            [sg.Button("Clínicas com maior número de atendimentos", key=1, size=(45, 1))],
            [sg.Button("Atendimentos mais caros e mais baratos", key=2, size=(45, 1))],
            [sg.Button("Procedimentos mais populares", key=3, size=(45, 1))],
            [sg.Button("Procedimentos mais caros e mais baratos", key=4, size=(45, 1))],
            [sg.Button("Retornar", key=0, size=(45, 1), pad=(0, 10))]
        ]
        window = sg.Window("Relatórios", layout, element_justification='c')
        evento, _ = window.read()
        window.close()
        
        # Mapeia o fechamento da janela ou cancelamento para 0 (Retornar)
        if evento is None or evento == -1:
            return 0
        return evento

    def mostrar_mensagem(self, msg: str):
        sg.popup(f"[RELATÓRIO]: {msg}", title="Módulo Relatórios")

    def mostrar_relatorio_clinicas(self, ranking: list):
        texto = "CLÍNICAS COM MAIS ATENDIMENTOS\n\n"
        for posicao, (clinica, quantidade) in enumerate(ranking, start=1):
            texto += f"{posicao}º - {clinica}: {quantidade} atendimento(s)\n"
        sg.popup_scrolled(texto, title="Relatório Clínicas", size=(45, 10))

    def mostrar_relatorio_atendimentos_extremos(self, dados: dict):
        texto = "ATENDIMENTOS EXTREMOS\n\n"
        texto += "-> MAIS CARO:\n"
        texto += f"   ID: {dados['caro_id']} | Data: {dados['caro_data']} | Valor: R${dados['caro_valor']:.2f}\n\n"
        texto += "-> MAIS BARATO:\n"
        texto += f"   ID: {dados['barato_id']} | Data: {dados['barato_data']} | Valor: R${dados['barato_valor']:.2f}\n"
        sg.popup(texto, title="Relatório Atendimentos Extremos")

    def mostrar_relatorio_procedimentos_populares(self, ranking: list):
        texto = "PROCEDIMENTOS MAIS POPULARES\n\n"
        for posicao, (proc, quantidade) in enumerate(ranking, start=1):
            texto += f"{posicao}º - {proc}: realizado {quantidade} vez(es)\n"
        sg.popup_scrolled(texto, title="Relatório Procedimentos Populares", size=(45, 10))

    def mostrar_relatorio_procedimentos_extremos(self, dados: dict):
        texto = "PROCEDIMENTOS EXTREMOS\n\n"
        texto += "-> MAIS CARO:\n"
        texto += f"   {dados['caro_desc']} - Custo: R${dados['caro_custo']:.2f}\n\n"
        texto += "-> MAIS BARATO:\n"
        texto += f"   {dados['barato_desc']} - Custo: R${dados['barato_custo']:.2f}\n"
        sg.popup(texto, title="Relatório Procedimentos Extremos")