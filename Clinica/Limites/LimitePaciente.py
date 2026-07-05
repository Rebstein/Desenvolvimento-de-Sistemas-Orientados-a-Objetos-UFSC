import PySimpleGUI as sg

class LimitePaciente:
    def tela_opcoes(self):
        sg.theme('LightGrey1')
        layout = [
            [sg.Text("PACIENTES", font=("Helvetica", 12, "bold"), pad=(0, 10))],
            [sg.Button("Cadastrar Paciente", key=1, size=(22, 1))],
            [sg.Button("Listar Pacientes", key=2, size=(22, 1))],
            [sg.Button("Alterar Paciente", key=3, size=(22, 1))],
            [sg.Button("Excluir Paciente", key=4, size=(22, 1))],
            [sg.Button("Retornar", key=0, size=(22, 1), pad=(0, 10))]
        ]
        window = sg.Window("Módulo Pacientes", layout, element_justification='c')
        evento, _ = window.read()
        window.close()
        return evento if evento is not None else -1

    def pegar_dados_paciente(self):
        layout = [
            [sg.Text("Dados do Paciente", font=("Helvetica", 12, "bold"), pad=(0, 10))],
            [sg.Text("Nome:", size=(12, 1)), sg.InputText(key="nome")],
            [sg.Text("CPF:", size=(12, 1)), sg.InputText(key="cpf")],
            [sg.Text("Celular:", size=(12, 1)), sg.InputText(key="celular")],
            [sg.Text("Nascimento:", size=(12, 1)), sg.InputText(key="data_nascimento"), sg.Text("(DD-MM-YYYY)", font=("Helvetica", 8, "italic"))],
            [sg.Button("Confirmar", key="OK"), sg.Button("Cancelar", key="CANCEL")]
        ]
        window = sg.Window("Formulário Paciente", layout)
        evento, valores = window.read()
        window.close()
        
        if evento == "OK":
            return valores
        return {"nome": "", "cpf": "", "celular": "", "data_nascimento": ""}

    def selecionar_paciente(self):
        layout = [
            [sg.Text("Digite o CPF do Paciente que deseja selecionar:")],
            [sg.InputText(key="cpf")],
            [sg.Button("Selecionar", key="OK"), sg.Button("Cancelar", key="CANCEL")]
        ]
        window = sg.Window("Selecionar", layout)
        evento, valores = window.read()
        window.close()
        return valores["cpf"] if evento == "OK" else ""

    def mostrar_pacientes(self, dados_pacientes):
        texto = "Pacientes Cadastrados\n\n"
        if not dados_pacientes:
            texto += "Nenhum paciente registado."
        for p in dados_pacientes:
            texto += f"Nome: {p['nome']} | CPF: {p['cpf']}\n"
            texto += f"Celular: {p['celular']} | Nasc: {p['data_nascimento']}\n"
            texto += "-" * 45 + "\n"
        
        sg.popup_scrolled(texto, title="Lista de Pacientes", size=(50, 12))

    def mostrar_mensagem(self, msg: str):
        sg.popup(f"[PACIEINTE]: {msg}", title="Pacientes")