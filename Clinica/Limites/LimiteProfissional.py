import PySimpleGUI as sg

class LimiteProfissional:
    def tela_opcoes(self):
        sg.theme('LightGrey1')
        layout = [
            [sg.Text("PROFISSIONAIS", font=("Helvetica", 12, "bold"), pad=(0, 10))],
            [sg.Button("Cadastrar Profissional", key=1, size=(22, 1))],
            [sg.Button("Listar Profissionais", key=2, size=(22, 1))],
            [sg.Button("Alterar Profissional", key=3, size=(22, 1))],
            [sg.Button("Excluir Profissional", key=4, size=(22, 1))],
            [sg.Button("Retornar", key=0, size=(22, 1), pad=(0, 10))]
        ]
        window = sg.Window("Módulo Profissionais", layout, element_justification='c')
        evento, _ = window.read()
        window.close()
        return evento if evento is not None else -1

    def pegar_dados_profissional(self):
        layout = [
            [sg.Text("Dados do Profissional", font=("Helvetica", 12, "bold"), pad=(0, 10))],
            [sg.Text("Nome:", size=(18, 1)), sg.InputText(key="nome")],
            [sg.Text("CPF:", size=(18, 1)), sg.InputText(key="cpf")],
            [sg.Text("Celular:", size=(18, 1)), sg.InputText(key="celular")],
            [sg.Text("Especialidade:", size=(18, 1)), sg.InputText(key="especialidade")],
            [sg.Text("Reg. Profissional:", size=(18, 1)), sg.InputText(key="registro_profissional")],
            [sg.Button("Confirmar", key="OK"), sg.Button("Cancelar", key="CANCEL")]
        ]
        window = sg.Window("Formulário Profissional", layout)
        evento, valores = window.read()
        window.close()
        
        if evento == "OK":
            return valores
        return {"nome": "", "cpf": "", "celular": "", "especialidade": "", "registro_profissional": ""}

    def selecionar_profissional(self):
        layout = [
            [sg.Text("Digite o CPF do Profissional que deseja selecionar:")],
            [sg.InputText(key="cpf")],
            [sg.Button("Selecionar", key="OK"), sg.Button("Cancelar", key="CANCEL")]
        ]
        window = sg.Window("Selecionar", layout)
        evento, valores = window.read()
        window.close()
        return valores["cpf"] if evento == "OK" else ""

    def mostrar_profissionais(self, dados_profissionais):
        texto = "Profissionais Cadastrados\n\n"
        if not dados_profissionais:
            texto += "Nenhum profissional registado."
        for prof in dados_profissionais:
            texto += f"Nome: {prof['nome']} | CPF: {prof['cpf']} | Reg: {prof['registro_profissional']}\n"
            texto += f"Celular: {prof['celular']} | Especialidade: {prof['especialidade']}\n"
            texto += "-" * 50 + "\n"
        
        sg.popup_scrolled(texto, title="Lista de Profissionais", size=(55, 12))

    def mostrar_mensagem(self, msg: str):
        sg.popup(f"[PROFISSIONAL]: {msg}", title="Profissionais")