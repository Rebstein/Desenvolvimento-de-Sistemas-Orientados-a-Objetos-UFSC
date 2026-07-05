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
        
        if evento is None or evento == -1:
            return -1
        return evento

    def pegar_dados_paciente(self):
        layout = [
            [sg.Text("Dados do Paciente", font=("Helvetica", 12, "bold"), pad=(0, 10))],
            [sg.Text("Nome*:", size=(12, 1)), sg.InputText(key="nome")],
            [sg.Text("CPF*:", size=(12, 1)), sg.InputText(key="cpf")],
            [sg.Text("Celular:", size=(12, 1)), sg.InputText(key="celular")],
            [sg.Text("Nascimento*:", size=(12, 1)), sg.InputText(key="data_nascimento"), sg.Text("(DD-MM-YYYY)", font=("Helvetica", 8, "italic"))],
            [sg.Button("Confirmar", key="OK"), sg.Button("Cancelar", key="CANCEL")]
        ]
        window = sg.Window("Formulário Paciente", layout)
        
        while True:
            evento, valores = window.read()
            
            if evento in (None, "CANCEL"):
                window.close()
                return None
                
            if evento == "OK":
                if valores["nome"].strip() == "" or valores["cpf"].strip() == "" or valores["data_nascimento"].strip() == "":
                    sg.popup_error("Erro: Nome, CPF e Data de Nascimento são obrigatórios!", title="Campos Vazios")
                    continue
                
                window.close()
                return valores

    def selecionar_paciente(self):
        layout = [
            [sg.Text("Digite o CPF do Paciente que deseja selecionar:")],
            [sg.InputText(key="cpf")],
            [sg.Button("Selecionar", key="OK"), sg.Button("Cancelar", key="CANCEL")]
        ]
        window = sg.Window("Selecionar", layout)
        evento, valores = window.read()
        window.close()
        
        # Só valida se confirmou e o CPF não está em branco
        if evento == "OK" and valores["cpf"].strip() != "":
            return valores["cpf"]
        return None  # Retorna None se desistiu

    def mostrar_pacientes(self, dados_pacientes):
        texto = "Pacientes Cadastrados\n\n"
        if not dados_pacientes:
            texto += "Nenhum paciente cadastrado."
        for p in dados_pacientes:
            texto += f"Nome: {p['nome']} | CPF: {p['cpf']}\n"
            texto += f"Celular: {p['celular']} | Nasc: {p['data_nascimento']}\n"
            texto += "-" * 45 + "\n"
        
        sg.popup_scrolled(texto, title="Lista de Pacientes", size=(50, 12))

    def mostrar_mensagem(self, msg: str):
        sg.popup(f"[PACIENTE]: {msg}", title="Pacientes")