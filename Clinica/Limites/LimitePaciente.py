import PySimpleGUI as sg

class LimitePaciente:
    def tela_opcoes(self):
        sg.theme('BlueMono')
        
        # Padrão para botões (mais simples de fazer alterações)
        fonte_botoes = ("Courier New", 12)
        tamanho_botoes = (28, 1)
        
        layout = [
            [sg.Text("PACIENTES", font=("Courier New", 16, "bold"), text_color='white', pad=(0, 15))],
            [sg.Button("Cadastrar Paciente", key=1, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Listar Pacientes", key=2, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Alterar Paciente", key=3, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Excluir Paciente", key=4, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Retornar", key=0, size=tamanho_botoes, font=fonte_botoes, button_color=('white', 'blue'), pad=(0, 15))]
        ]
        window = sg.Window("Módulo Pacientes", layout, element_justification='c')
        evento, _ = window.read()
        window.close()
        
        # Caso o usuário selecione 'X' (-1) ele fecha o sistema
        if evento is None or evento == -1:
            return -1
        return evento

    # Função para criar um paciente no sistema
    def pegar_dados_paciente(self):
        fonte_texto = ("Courier New", 12)
        tamanho_label = (15, 1) 
        
        layout = [
            [sg.Text("Dados do Paciente", font=("Courier New", 16, "bold"), text_color='white', pad=(0, 15))],
            [sg.Text("Nome*:", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="nome", font=fonte_texto)],
            [sg.Text("CPF*:", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="cpf", font=fonte_texto)],
            [sg.Text("Celular:", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="celular", font=fonte_texto)],
            [sg.Text("Nascimento*:", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="data_nascimento", font=fonte_texto), sg.Text("(DD/MM/YYYY)", font=("Courier New", 10, "italic"), text_color='white')],
            [sg.Push(),
             sg.Button("Confirmar", key="OK", font=fonte_texto, size=(12, 1), button_color=('white', 'blue'), pad=(10, 15)), 
             sg.Button("Cancelar", key="CANCEL", font=fonte_texto, size=(12, 1), button_color=('white', 'red'), pad=(10, 15))]
        ]
        window = sg.Window("Formulário Paciente", layout)
        
        while True:
            evento, valores = window.read()
            # Caso o usuário selecione "Cancelar", fecha a janela e retorna None
            if evento in (None, "CANCEL"):
                window.close()
                return None
            # Verifica se os campos obrigatórios estão preenchidos
            if evento == "OK":
                if valores["nome"].strip() == "" or valores["cpf"].strip() == "" or valores["data_nascimento"].strip() == "":
                    sg.popup_error("Erro: Nome, CPF e Data de Nascimento são obrigatórios!", title="Campos Vazios", font=fonte_texto)
                    continue
                
                window.close()
                return valores

    # FUnção para selecionar um paciente (solicitando o CPF do paciente)
    def selecionar_paciente(self):
        fonte_texto = ("Courier New", 12)
        
        layout = [
            [sg.Text("Digite o CPF do Paciente que deseja selecionar:", font=fonte_texto, pad=(0, 10), text_color='white')],
            [sg.InputText(key="cpf", font=fonte_texto, pad=(0, 10))],
            [sg.Push(),
             sg.Button("Selecionar", key="OK", font=fonte_texto, button_color=('white', 'blue'), size=(12, 1)), 
             sg.Button("Cancelar", key="CANCEL", font=fonte_texto, button_color=('white', 'red'), size=(12, 1))]
        ]
        window = sg.Window("Selecionar", layout, element_justification='c')
        evento, valores = window.read()
        window.close()
        
        if evento == "OK" and valores["cpf"].strip() != "":
            return valores["cpf"]
        return None

    # Função para mostrar os pacientes cadastrados no sistema
    def mostrar_pacientes(self, dados_pacientes):
        texto = "Pacientes Cadastrados\n\n"
        if not dados_pacientes:
            texto += "Nenhum paciente cadastrado."
        for p in dados_pacientes:
            texto += f"Nome: {p['nome']} | CPF: {p['cpf']}\n"
            texto += f"Celular: {p['celular']} | Nasc: {p['data_nascimento']}\n"
            texto += "-" * 45 + "\n"
        
        sg.popup_scrolled(texto, title="Lista de Pacientes", size=(60, 14), font=("Courier New", 12))

    # Padrão para mensagens do controlador
    def mostrar_mensagem(self, msg: str):
        sg.popup(f"[PACIENTE]: {msg}", title="Pacientes", font=("Courier New", 12), text_color='white')