class LimiteAtendimento:
    def tela_opcoes(self):
        print("\n--- MÓDULO DE ATENDIMENTOS ---")
        print("1 - Agendar Atendimento")
        print("2 - Listar Atendimentos")
        print("3 - Alterar Atendimento")
        print("4 - Excluir Atendimento")
        print("5 - Adicionar Procedimento a um Atendimento")
        print("6 - Registrar Pagamento")
        print("0 - Retornar")
        
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def pedir_string(self, prompt: str):
        return input(prompt)

    def pegar_dados_atendimento(self):
        print("\n--- Preencha os Dados do Atendimento ---")
        data = input("Data (YYYY-MM-DD): ")
        hora_inicio = input("Horário de Início (HH:MM): ")
        hora_fim = input("Horário de Fim (HH:MM): ")
        tipo = input("Tipo (Consulta, Retorno, Exame, Procedimento, Emergência): ")
        
        try:
            valor = float(input("Valor Base Total (R$): "))
        except ValueError:
            valor = 0.0

        return {
            "data": data, "horario_inicio": hora_inicio, 
            "horario_fim": hora_fim, "tipo_atendimento": tipo, "valor_total": valor
        }

    def pegar_dados_procedimento(self):
        print("\n--- Adicionar Procedimento ---")
        descricao = input("Descrição do procedimento: ")
        try:
            custo = float(input("Custo do procedimento (R$): "))
        except ValueError:
            custo = 0.0
        return {"descricao": descricao, "custo": custo}

    def pegar_dados_pagamento(self):
        print("\n--- Registrar Pagamento ---")
        data = input("Data do Pagamento (YYYY-MM-DD): ")
        try:
            valor = float(input("Valor pago (R$): "))
            print("\nTipos de Pagamento:")
            print("1 - Dinheiro | 2 - PIX | 3 - Cartão")
            tipo = int(input("Escolha o tipo: "))
        except ValueError:
            valor = 0.0
            tipo = 1
            
        return {"data": data, "valor": valor, "tipo_pagamento": tipo}

    def mostrar_atendimentos(self, dados_atendimentos):
        print("\n--- Atendimentos Agendados ---")
        for at in dados_atendimentos:
            print(f"ID: {at['id']} | Data: {at['data']} | Tipo: {at['tipo']}")
            print(f"Paciente: {at['paciente']} | Profissional: {at['profissional']}")
            print(f"Clínica: {at['clinica']}")
            print(f"Valor Total: R${at['valor_total']:.2f} | Restante: R${at['valor_restante']:.2f}")
            print("-" * 30)

    def mostrar_mensagem(self, msg: str):
        print(f"\n[ATENDIMENTO]: {msg}")