import PySimpleGUI as sg

class LimiteAtendimento:
    def tela_opcoes(self):
        sg.theme('LightGrey1')
        layout = [
            [sg.Text("ATENDIMENTOS", font=("Helvetica", 12, "bold"), pad=(0, 10))],
            [sg.Button("Agendar Atendimento", key=1, size=(40, 1))],
            [sg.Button("Listar Atendimentos", key=2, size=(40, 1))],
            [sg.Button("Alterar Atendimento", key=3, size=(40, 1))],
            [sg.Button("Excluir Atendimento", key=4, size=(40, 1))],
            [sg.Button("Adicionar Procedimento a um Atendimento", key=5, size=(40, 1))],
            [sg.Button("Registrar Pagamento", key=6, size=(40, 1))],
            [sg.Button("Retornar", key=0, size=(40, 1), pad=(0, 10))]
        ]
        window = sg.Window("Atendimentos", layout, element_justification='c')
        evento, _ = window.read()
        window.close()
        
        if evento is None or evento == -1:
            return -1
        return evento

    def pedir_string(self, prompt: str):
        layout = [
            [sg.Text(prompt)],
            [sg.InputText(key="resposta")],
            [sg.Button("OK", key="OK"), sg.Button("Cancelar", key="CANCEL")]
        ]
        window = sg.Window("Entrada de Dados", layout)
        evento, valores = window.read()
        window.close()
        
        # Só retorna o texto se o campo não estiver em branco e confirmou com OK
        if evento == "OK" and valores["resposta"].strip() != "":
            return valores["resposta"]
        return None  # Retorna None para abortar buscas indesejadas por strings vazias

    def pegar_dados_atendimento(self):
        layout = [
            [sg.Text("Preencha os Dados do Atendimento", font=("Helvetica", 11, "bold"), pad=(0, 10))],
            [sg.Text("Data* (DD-MM-YYYY):", size=(22, 1)), sg.InputText(key="data")],
            [sg.Text("Horário de Início* (HH:MM):", size=(22, 1)), sg.InputText(key="horario_inicio")],
            [sg.Text("Horário de Fim* (HH:MM):", size=(22, 1)), sg.InputText(key="horario_fim")],
            [sg.Text("Tipo Atendimento*:", size=(22, 1)), sg.InputText(key="tipo_atendimento")],
            [sg.Text("Valor Total (R$):", size=(22, 1)), sg.InputText(key="valor_total")],
            [sg.Button("Confirmar", key="OK"), sg.Button("Cancelar", key="CANCEL")]
        ]
        window = sg.Window("Novo Atendimento", layout)
        
        while True:
            evento, valores = window.read()
            
            if evento in (None, "CANCEL"):
                window.close()
                return None
                
            if evento == "OK":
                # Valida se os campos textuais importantes estão vazios
                campos_vazios = (valores["data"].strip() == "" or 
                                 valores["horario_inicio"].strip() == "" or 
                                 valores["horario_fim"].strip() == "" or 
                                 valores["tipo_atendimento"].strip() == "")
                                 
                if campos_vazios:
                    sg.popup_error("Erro: Data, Horários e Tipo de Atendimento são obrigatórios!", title="Campos Vazios")
                    continue
                
                try:
                    valores["valor_total"] = float(valores["valor_total"])
                except ValueError:
                    valores["valor_total"] = 0.0
                    
                window.close()
                return valores

    def pegar_dados_procedimento(self):
        layout = [
            [sg.Text("Adicionar Procedimento", font=("Helvetica", 11, "bold"), pad=(0, 10))],
            [sg.Text("Descrição:", size=(15, 1)), sg.InputText(key="descricao")],
            [sg.Text("Custo (R$):", size=(15, 1)), sg.InputText(key="custo")],
            [sg.Button("Adicionar", key="OK"), sg.Button("Cancelar", key="CANCEL")]
        ]
        window = sg.Window("Adicionar Procedimento", layout)
        evento, valores = window.read()
        window.close()
        
        if evento == "OK":
            try:
                valores["custo"] = float(valores["custo"])
            except ValueError:
                valores["custo"] = 0.0
            return valores
        return None  # Retorna None em vez de dicionário com valores fantasmas vazios

    def pegar_dados_pagamento(self):
        layout = [
            [sg.Text("Registrar Pagamento", font=("Helvetica", 11, "bold"), pad=(0, 10))],
            [sg.Text("Data Pagamento (DD-MM-YYYY):", size=(25, 1)), sg.InputText(key="data")],
            [sg.Text("Valor Pago (R$):", size=(25, 1)), sg.InputText(key="valor")],
            [sg.Frame("Tipo de Pagamento", [
                [sg.Radio("Dinheiro", "TIPO_PAG", default=True, key=1), 
                 sg.Radio("PIX", "TIPO_PAG", key=2), 
                 sg.Radio("Cartão", "TIPO_PAG", key=3)]
            ], pad=(0, 15))],
            [sg.Button("Registrar", key="OK"), sg.Button("Cancelar", key="CANCEL")]
        ]
        window = sg.Window("Registrar Pagamento", layout)
        evento, valores = window.read()
        window.close()
        
        if evento == "OK":
            try:
                valor = float(valores["valor"])
            except ValueError:
                valor = 0.0
                
            tipo_selecionado = 1
            for k in [1, 2, 3]:
                if valores[k]:
                    tipo_selecionado = k
                    
            return {"data": valores["data"], "valor": valor, "tipo_pagamento": tipo_selecionado}
        return None  # Retorna None em vez de dicionário com valores fantasmas vazios

    def mostrar_atendimentos(self, dados_atendimentos):
        texto = "Atendimentos Agendados\n\n"
        if not dados_atendimentos:
            texto += "Nenhum atendimento agendado."
        for at in dados_atendimentos:
            texto += f"ID: {at['id']} | Data: {at['data']} | Tipo: {at['tipo']}\n"
            texto += f"Paciente: {at['paciente']} | Profissional: {at['profissional']}\n"
            texto += f"Clínica: {at['clinica']}\n"
            texto += f"Valor Total: R${at['valor_total']:.2f} | Restante: R${at['valor_restante']:.2f}\n"
            texto += "-" * 55 + "\n"
        
        sg.popup_scrolled(texto, title="Lista de Atendimentos", size=(65, 15))

    def mostrar_mensagem(self, msg: str):
        sg.popup(f"[ATENDIMENTO]: {msg}", title="Atendimentos")