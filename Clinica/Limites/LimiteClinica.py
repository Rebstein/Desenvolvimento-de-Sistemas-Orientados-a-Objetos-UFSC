import PySimpleGUI as sg

class LimiteClinica:
    def tela_opcoes(self):
        sg.theme('BlueMono')
        
        # Padrão de tamanho calibrado para o menu
        fonte_botoes = ("Courier New New", 12)
        tamanho_botoes = (28, 1)
        
        layout = [
            [sg.Text("CLÍNICAS", font=("Courier New New", 16, "bold"), text_color='white', pad=(0, 15))],
            [sg.Button("Cadastrar Clínica", key=1, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Listar Clínicas", key=2, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Alterar Clínica", key=3, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Excluir Clínica", key=4, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Retornar", key=0, size=tamanho_botoes, font=fonte_botoes, button_color=('white', 'blue'), pad=(0, 15))]
        ]
        window = sg.Window("Módulo Clínicas", layout, element_justification='c')
        evento, _ = window.read()
        window.close()
    
        if evento is None or evento == -1:
            return -1
        return evento

    def pegar_dados_clinica(self):
        fonte_texto = ("Courier New", 12)
        tamanho_label = (15, 1)
        
        layout = [
            [sg.Text("Dados da Clínica", font=("Courier New", 16, "bold"), text_color='white', pad=(0, 15))],
            [sg.Text("Nome da Clínica*:", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="nome", font=fonte_texto)],
            [sg.Text("Cidade*:", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="cidade", font=fonte_texto)],
            [sg.Text("Descrição:", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="descricao", font=fonte_texto)],
            [sg.Text("Horário Início:", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="horario_inicio", font=fonte_texto)],
            [sg.Text("Horário Fim:", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="horario_fim", font=fonte_texto)],
            [
                sg.Push(),
                sg.Button("Confirmar", key="OK", font=fonte_texto, size=(12, 1), button_color=('white', 'blue'), pad=(10, 15)), 
             sg.Button("Cancelar", key="CANCEL", font=fonte_texto, size=(12, 1), button_color=('white', 'red'), pad=(10, 15))]
        ]
        window = sg.Window("Formulário Clínica", layout)
        
        while True:
            evento, valores = window.read()
            
            if evento in (None, "CANCEL"):
                window.close()
                return None
                
            if evento == "OK":
                if valores["nome"].strip() == "" or valores["cidade"].strip() == "":
                    sg.popup_error("Erro: Os campos Nome e Cidade são obrigatórios!", title="Campos Vazios", text_color='white', font=fonte_texto)
                    continue
                
                window.close()
                return valores

    def selecionar_clinica(self):
        fonte_texto = ("Courier New", 12)
        layout = [
            [sg.Text("Digite o NOME da Clínica que deseja selecionar:", font=fonte_texto, text_color='white', pad=(0, 10))],
            [sg.InputText(key="nome", font=fonte_texto, text_color='black', pad=(0, 10))],
            [
                sg.Push(),
                sg.Button("Selecionar", key="OK", font=fonte_texto, button_color=('white', 'blue'), size=(12, 1)), 
                sg.Button("Cancelar", key="CANCEL", font=fonte_texto, button_color=('white', 'red'), size=(12, 1))]
        ]
        window = sg.Window("Selecionar", layout, element_justification='c')
        evento, valores = window.read()
        window.close()
        
        if evento == "OK" and valores["nome"].strip() != "":
            return valores["nome"]
        return None

    def mostrar_clinicas(self, dados_clinicas):
        texto = "Clínicas Cadastradas\n\n"
        if not dados_clinicas:
            texto += "Nenhuma clínica cadastrada."
        for clinica in dados_clinicas:
            texto += f"Nome: {clinica['nome']} | Cidade: {clinica['cidade']}\n"
            texto += f"Descrição: {clinica['descricao']}\n"
            texto += f"Horário de Funcionamento: {clinica['horario_inicio']} - {clinica['horario_fim']}\n"
            texto += "-" * 45 + "\n"
        
        # Janela de rolagem ampliada para acompanhar a fonte
        sg.popup_scrolled(texto, title="Lista de Clínicas", size=(60, 14), font=("Courier New New", 12))

    def mostrar_mensagem(self, msg: str):
        sg.popup(f"[CLÍNICA]: {msg}", title="Clínicas", text_color='white', font=("Courier New New", 12))