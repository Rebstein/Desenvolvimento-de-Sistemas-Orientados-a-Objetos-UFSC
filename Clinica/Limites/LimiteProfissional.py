import PySimpleGUI as sg

class LimiteProfissional:
    def tela_opcoes(self):
        sg.theme('BlueMono')
        
        # Padrão para botões (mais simples de fazer alterações)
        fonte_botoes = ("Courier New", 12)
        tamanho_botoes = (28, 1)
        
        layout = [
            [sg.Text("PROFISSIONAIS", font=("Courier New", 16, "bold"), text_color='white', pad=(0, 15))],
            [sg.Button("Cadastrar Profissional", key=1, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Listar Profissionais", key=2, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Alterar Profissional", key=3, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Excluir Profissional", key=4, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Retornar", key=0, size=tamanho_botoes, font=fonte_botoes, button_color=('white', 'blue'), pad=(0, 15))]
        ]
        window = sg.Window("Módulo Profissionais", layout, element_justification='c')
        evento, _ = window.read()
        window.close()
        
        # Caso o usuário selecione 'X' (-1) ele fecha o sistema
        if evento is None or evento == -1:
            return -1
        return evento

    # Função para criar um profissional no sistema
    def pegar_dados_profissional(self):
  
        fonte_texto = ("Courier New", 12)
        tamanho_label = (18, 1) 
        
        layout = [
            [sg.Text("Dados do Profissional", font=("Courier New", 16, "bold"), text_color='white', pad=(0, 15))],
            [sg.Text("Nome*:", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="nome", font=fonte_texto)],
            [sg.Text("CPF*:", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="cpf", font=fonte_texto)],
            [sg.Text("Celular:", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="celular", font=fonte_texto)],
            [sg.Text("Especialidade:", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="especialidade", font=fonte_texto)],
            [sg.Text("Reg. Profissional*:", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="registro_profissional", font=fonte_texto)],
            [sg.Push(),
             sg.Button("Confirmar", key="OK", font=fonte_texto, size=(12, 1), button_color=('white', 'blue'), pad=(10, 15)), 
             sg.Button("Cancelar", key="CANCEL", font=fonte_texto, size=(12, 1), button_color=('white', 'red'), pad=(10, 15))]
        ]
        window = sg.Window("Formulário Profissional", layout)
        
        while True:
            evento, valores = window.read()
            # Caso o usuário selecione "Cancelar", fecha a janela e retorna None
            if evento in (None, "CANCEL"):
                window.close()
                return None
            # Verifica se os campos obrigatórios estão preenchidos
            if evento == "OK":
                if valores["nome"].strip() == "" or valores["cpf"].strip() == "" or valores["registro_profissional"].strip() == "":
                    sg.popup_error("Erro: Nome, CPF e Registro Profissional são obrigatórios!", title="Campos Vazios", font=fonte_texto)
                    continue
                
                window.close()
                return valores

    # Função para selecionar um profissional (solicitando o CPF do profissional)
    def selecionar_profissional(self):
        fonte_texto = ("Courier New", 12)
        
        layout = [
            [sg.Text("Digite o CPF do Profissional que deseja selecionar:", font=fonte_texto, text_color='white', pad=(0, 10))],
            [sg.InputText(key="cpf", font=fonte_texto, text_color='black', pad=(0, 10))],
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

    # Função para mostrar os profissionais cadastrados no sistema
    def mostrar_profissionais(self, dados_profissionais):
        texto = "Profissionais Cadastrados\n\n"
        if not dados_profissionais:
            texto += "Nenhum profissional cadastrado."
        for prof in dados_profissionais:
            texto += f"Nome: {prof['nome']} | CPF: {prof['cpf']} | Reg: {prof['registro_profissional']}\n"
            texto += f"Celular: {prof['celular']} | Especialidade: {prof['especialidade']}\n"
            texto += "-" * 50 + "\n"
        
        sg.popup_scrolled(texto, title="Lista de Profissionais", size=(65, 15), font=("Courier New", 12))

    # Padrão para mensagens do controlador
    def mostrar_mensagem(self, msg: str):
        sg.popup(f"[PROFISSIONAL]: {msg}", title="Profissionais", text_color='white', font=("Courier New", 12))