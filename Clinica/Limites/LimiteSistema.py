import PySimpleGUI as sg

class LimiteSistema:
    def tela_opcoes(self):
        sg.theme('LightGrey1')
        
        layout = [
            [sg.Text("BEM-VINDO AO SISTEMA DE CLÍNICAS", font=("Helvetica", 14, "bold"), pad=(0, 10))],
            [sg.Button("Clínicas", key=1, size=(25, 1))],
            [sg.Button("Pacientes", key=2, size=(25, 1))],
            [sg.Button("Profissionais", key=3, size=(25, 1))],
            [sg.Button("Atendimentos", key=4, size=(25, 1))],
            [sg.Button("Relatórios", key=5, size=(25, 1))],
            [sg.Button("Encerrar Sistema", key=0, button_color=('white', 'red'), size=(25, 1), pad=(0, 15))]
        ]
        
        window = sg.Window("Menu Principal", layout, element_justification='c', finalize=True)
        evento, _ = window.read()
        window.close()
        
        if evento is None or evento == -1:
            return -1
        return evento
                
    def mostrar_mensagem(self, msg: str):
        sg.popup(f"[SISTEMA]: {msg}", title="Notificação do Sistema")