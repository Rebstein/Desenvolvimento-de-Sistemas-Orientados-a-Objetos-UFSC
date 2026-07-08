import PySimpleGUI as sg

class LimiteAtendimento:
    def tela_opcoes(self):
        sg.theme('BlueMono')
        
        # Padrão calibrado para menus com textos longos nos botões
        fonte_botoes = ("Courier New", 12)
        tamanho_botoes = (44, 1)
        
        layout = [
            [sg.Text("ATENDIMENTOS", font=("Courier New", 16, "bold"), text_color='white', pad=(0, 15))],
            [sg.Button("Agendar Atendimento", key=1, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Listar Atendimentos", key=2, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Alterar Atendimento", key=3, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Excluir Atendimento", key=4, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Adicionar Procedimento a um Atendimento", key=5, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Registrar Pagamento", key=6, size=tamanho_botoes, font=fonte_botoes, pad=(0, 5))],
            [sg.Button("Retornar", key=0, size=tamanho_botoes, font=fonte_botoes, button_color=('white', 'blue'), pad=(0, 15))]
        ]
        window = sg.Window("Atendimentos", layout, element_justification='c')
        evento, _ = window.read()
        window.close()
        
        if evento is None or evento == -1:
            return -1
        return evento

    def pedir_string(self, prompt: str):
        fonte_texto = ("Courier New", 12)
        
        layout = [
            [sg.Text(prompt, font=fonte_texto, pad=(0, 10), text_color='white')],
            [sg.InputText(key="resposta", font=fonte_texto, pad=(0, 10))],
            [
                sg.Push(),
                sg.Button("Confirmar", key="OK", font=fonte_texto, size=(12, 1), button_color=('white', 'blue')),
                sg.Button("Cancelar", key="CANCEL", font=fonte_texto, size=(12, 1), button_color=('white', 'red'))]
        ]
        window = sg.Window("Entrada de Dados", layout, element_justification='c')
        evento, valores = window.read()
        window.close()
        
        if evento == "OK" and valores["resposta"].strip() != "":
            return valores["resposta"]
        return None

    def pegar_dados_atendimento(self):
        fonte_texto = ("Courier New", 12)
        tamanho_label = (26, 1)
        
        layout = [
            [sg.Text("Preencha os Dados do Atendimento", font=("Courier New", 16, "bold"), pad=(0, 15), text_color='white')],
            [sg.Text("Data* (DD-MM-YYYY):", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="data", font=fonte_texto)],
            [sg.Text("Horário de Início* (HH:MM):", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="horario_inicio", font=fonte_texto)],
            [sg.Text("Horário de Fim* (HH:MM):", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="horario_fim", font=fonte_texto)],
            [sg.Text("Tipo Atendimento*:", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="tipo_atendimento", font=fonte_texto)],
            [sg.Text("Valor Total (R$):", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="valor_total", font=fonte_texto)],
            [
                sg.Push(),
                sg.Button("Confirmar", key="OK", font=fonte_texto, size=(12, 1), pad=(10, 15), button_color=('white', 'blue')), 
                sg.Button("Cancelar", key="CANCEL", font=fonte_texto, size=(12, 1), pad=(10, 15), button_color=('white', 'red'))]
        ]
        window = sg.Window("Novo Atendimento", layout)
        
        while True:
            evento, valores = window.read()
            
            if evento in (None, "CANCEL"):
                window.close()
                return None
                
            if evento == "OK":
                campos_vazios = (valores["data"].strip() == "" or 
                                 valores["horario_inicio"].strip() == "" or 
                                 valores["horario_fim"].strip() == "" or 
                                 valores["tipo_atendimento"].strip() == "")
                                 
                if campos_vazios:
                    sg.popup_error("Erro: Data, Horários e Tipo de Atendimento são obrigatórios!", title="Campos Vazios", font=fonte_texto, text_color='red')
                    continue
                
                try:
                    valores["valor_total"] = float(valores["valor_total"])
                except ValueError:
                    valores["valor_total"] = 0.0
                    
                window.close()
                return valores

    def pegar_dados_procedimento(self):
        fonte_texto = ("Courier New", 12)
        tamanho_label = (15, 1)
        
        layout = [
            [sg.Text("Adicionar Procedimento", font=("Courier New", 16, "bold"), pad=(0, 15), text_color='white')],
            [sg.Text("Descrição:", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="descricao", font=fonte_texto)],
            [sg.Text("Custo (R$):", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="custo", font=fonte_texto)],
            [sg.Button("Adicionar", key="OK", font=fonte_texto, size=(12, 1), pad=(10, 15), button_color=('white', 'blue')), 
             sg.Button("Cancelar", key="CANCEL", font=fonte_texto, size=(12, 1), pad=(10, 15), button_color=('white', 'red'))]
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
        return None

    def pegar_dados_pagamento(self):
        fonte_texto = ("Courier New", 12)
        tamanho_label = (25, 1)
        
        layout = [
            [sg.Text("Registrar Pagamento", font=("Courier New", 16, "bold"), pad=(0, 15), text_color='white')],
            [sg.Text("Data Pagamento (DD-MM-YYYY):", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="data", font=fonte_texto)],
            [sg.Text("Valor Pago (R$):", size=tamanho_label, font=fonte_texto, text_color='white'), sg.InputText(key="valor", font=fonte_texto)],
            # Adicionada a fonte e dimensionamento correto no Frame e nos Radios
            [sg.Frame("Tipo de Pagamento", [
                [sg.Radio("Dinheiro", "TIPO_PAG", default=True, key=1, font=fonte_texto), 
                 sg.Radio("PIX", "TIPO_PAG", key=2, font=fonte_texto), 
                 sg.Radio("Cartão", "TIPO_PAG", key=3, font=fonte_texto)]
            ], title_location=sg.TITLE_LOCATION_TOP, font=fonte_texto, pad=(0, 15))],
            [sg.Button("Registrar", key="OK", font=fonte_texto, size=(12, 1), button_color=('white', 'blue')), 
             sg.Button("Cancelar", key="CANCEL", font=fonte_texto, size=(12, 1), button_color=('white', 'red'))]
        ]
        window = sg.Window("Registrar Pagamento", layout, resizable=True, element_justification='c')
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
        return None

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
        
        sg.popup_scrolled(texto, title="Lista de Atendimentos", size=(70, 15), font=("Courier New", 12))

    def pedir_cpf_pix(self) -> str | None:
        return sg.popup_get_text("Digite o CPF do pagador:", title="Dados PIX")

    def pedir_dados_cartao(self) -> tuple[str, str] | None:
        num_cartao = sg.popup_get_text("Digite o número do cartão:", title="Dados Cartão")
        if num_cartao is None: return None
        bandeira = sg.popup_get_text("Digite a bandeira do cartão:", title="Dados Cartão")
        if bandeira is None: return None
        return num_cartao, bandeira

    def mostrar_mensagem(self, msg: str):
        sg.popup(f"[ATENDIMENTO]: {msg}", title="Atendimentos", font=("Courier New", 12), text_color='white')