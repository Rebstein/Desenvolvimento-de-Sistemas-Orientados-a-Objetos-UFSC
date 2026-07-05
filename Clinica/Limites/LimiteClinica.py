import PySimpleGUI as sg

class LimiteClinica:
    def tela_opcoes(self):
        sg.theme('LightGrey1')
        layout = [
            [sg.Text("CLÍNICAS", font=("Helvetica", 12, "bold"), pad=(0, 10))],
            [sg.Button("Cadastrar Clínica", key=1, size=(22, 1))],
            [sg.Button("Listar Clínicas", key=2, size=(22, 1))],
            [sg.Button("Alterar Clínica", key=3, size=(22, 1))],
            [sg.Button("Excluir Clínica", key=4, size=(22, 1))],
            [sg.Button("Retornar", key=0, size=(22, 1), pad=(0, 10))]
        ]
        window = sg.Window("Módulo Clínicas", layout, element_justification='c')
        evento, _ = window.read()
        window.close()
        return evento if evento is not None else -1

    def pegar_dados_clinica(self):
        layout = [
            [sg.Text("Dados da Clínica", font=("Helvetica", 12, "bold"), pad=(0, 10))],
            [sg.Text("Nome da Clínica:", size=(15, 1)), sg.InputText(key="nome")],
            [sg.Text("Cidade:", size=(15, 1)), sg.InputText(key="cidade")],
            [sg.Text("Descrição:", size=(15, 1)), sg.InputText(key="descricao")],
            [sg.Button("Confirmar", key="OK", size=(10, 1)), sg.Button("Cancelar", key="CANCEL", size=(10, 1))]
        ]
        window = sg.Window("Formulário Clínica", layout)
        evento, valores = window.read()
        window.close()
        
        if evento == "OK":
            return valores
        return {"nome": "", "cidade": "", "descricao": ""}

    def selecionar_clinica(self):
        layout = [
            [sg.Text("Digite o NOME da Clínica que deseja selecionar:")],
            [sg.InputText(key="nome")],
            [sg.Button("Selecionar", key="OK"), sg.Button("Cancelar", key="CANCEL")]
        ]
        window = sg.Window("Selecionar", layout)
        evento, valores = window.read()
        window.close()
        return valores["nome"] if evento == "OK" else ""

    def mostrar_clinicas(self, dados_clinicas):
        texto = "Clínicas Cadastradas\n\n"
        if not dados_clinicas:
            texto += "Nenhuma clínica registada."
        for clinica in dados_clinicas:
            texto += f"Nome: {clinica['nome']} | Cidade: {clinica['cidade']}\n"
            texto += f"Descrição: {clinica['descricao']}\n"
            texto += "-" * 45 + "\n"
        
        sg.popup_scrolled(texto, title="Lista de Clínicas", size=(50, 12))

    def mostrar_mensagem(self, msg: str):
        sg.popup(f"[CLÍNICA]: {msg}", title="Clínicas")