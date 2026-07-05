import PySimpleGUI as sg

class LimiteSistema:
    def tela_opcoes(self):
        sg.theme('BlueMono')  # Define o tema da interface
    
        # Ajustado para um meio-termo ideal
        fonte_botoes = ("Helvetica", 12)
        tamanho_botoes = (28, 1)  # Um pouco maiores que o original, mas sem exagero
        
        layout = [
            # Título reduzido de 22 para 16 e menos espaço vertical
            [sg.Text("BEM-VINDO AO SISTEMA DE CLÍNICAS", font=("Helvetica", 16, "bold"), text_color='white', pad=(0, 15))],
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
        
        if evento is None or evento == -1:
            return -1
        return evento
                
    def mostrar_mensagem(self, msg: str):
        # Popup com fonte tamanho 12 (legível e discreto)
        sg.popup(f"[SISTEMA]: {msg}", title="Notificação do Sistema", font=("Helvetica", 12))