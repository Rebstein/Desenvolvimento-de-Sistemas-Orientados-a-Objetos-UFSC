import PySimpleGUI as sg

class LimiteSistema:
    def tela_opcoes(self):
        sg.theme('BlueMono')  # Define o tema da interface
    
        # Padrão de tamanho e fonte para os botões
        fonte_botoes = ("Courier New", 12)
        tamanho_botoes = (28, 1) 
        
        # Layout do menu principal com botões centralizados
        layout = [
            [sg.Text("BEM-VINDO AO SISTEMA DE CLÍNICAS", font=("Courier New", 16, "bold"), text_color='white', pad=(0, 15))],
            [sg.Button("Clínicas", key=1, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Pacientes", key=2, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Profissionais", key=3, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Atendimentos", key=4, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Relatórios", key=5, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Encerrar Sistema", key=0, button_color=('white', 'red'), size=tamanho_botoes, font=fonte_botoes, pad=(0, 15))]
        ]
        
        window = sg.Window("Menu Principal", layout, element_justification='c')
        evento, _ = window.read()
        window.close()
        
        # Retorna -1 se o usuário fechar a janela (X) ou clicar em "Encerrar Sistema"
        if evento is None or evento == -1:
            return -1
        return evento
    
    # Popup para exibir mensagens do sistema
    def mostrar_mensagem(self, msg: str):
        sg.popup(f"[SISTEMA]: {msg}", title="Notificação do Sistema", font=("Courier New", 12), text_color='white')