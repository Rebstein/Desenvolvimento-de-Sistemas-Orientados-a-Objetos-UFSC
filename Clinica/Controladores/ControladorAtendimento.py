from datetime import datetime
from Entidades.Atendimento import Atendimento
from Entidades.Procedimento import Procedimento
from Entidades.TipoAtendimento import TipoAtendimento
from Entidades.Pagamento.PagamentoDinheiro import PagamentoDinheiro
from Entidades.Pagamento.PagamentoPix import PagamentoPix
from Entidades.Pagamento.PagamentoCartao import PagamentoCartao
from Limites.LimiteAtendimento import LimiteAtendimento

class ControladorAtendimento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__atendimentos = []
        self.__limite_atendimento = LimiteAtendimento()
    
    @property
    def atendimentos(self):
        return self.__atendimentos

    def buscar_atendimento_por_id(self, id_atendimento: int):
        if 0 <= id_atendimento < len(self.__atendimentos):
            return self.__atendimentos[id_atendimento]
        return None

    def incluir_atendimento(self):
        try:
            # VALIDAÇÃO DE CLÍNICAS (Bloqueia antes de pedir o nome)
            controlador_cli = self.__controlador_sistema.controlador_clinicas
            if len(controlador_cli._ControladorClinica__clinicas) == 0:
                controlador_cli.listar_clinicas() # Exibe o popup de "Nenhuma clínica cadastrada"
                return # Aborta o agendamento imediatamente

            controlador_cli.listar_clinicas()
            nome_clinica = self.__limite_atendimento.pedir_string("Digite o nome da Clínica para o atendimento: ")
            if nome_clinica is None: # Se o usuário cancelou na tela de pedir string
                return
                
            clinica = controlador_cli.buscar_clinica_por_nome(nome_clinica)
            if not clinica:
                raise ValueError("Clínica não encontrada.")

            # VALIDAÇÃO DE PACIENTES (Bloqueia antes de pedir o CPF)
            controlador_pac = self.__controlador_sistema.controlador_pacientes
            if len(controlador_pac._ControladorPaciente__pacientes) == 0:
                controlador_pac.listar_pacientes()
                return

            controlador_pac.listar_pacientes()
            cpf_paciente = self.__limite_atendimento.pedir_string("Digite o CPF do Paciente: ")
            if cpf_paciente is None:
                return
                
            paciente = controlador_pac.buscar_paciente_por_cpf(cpf_paciente)
            if not paciente:
                raise ValueError("Paciente não encontrado.")
            
            # Validação de > 18 anos
            data_nasc = datetime.strptime(paciente.data_nascimento, "%d-%m-%Y").date()
            hoje = datetime.now().date()
            idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
            if idade < 18:
                raise ValueError("Regra de Negócio: Paciente menor de 18 anos não pode realizar atendimento independente.")

            # VALIDAÇÃO DE PROFISSIONAIS (Bloqueia antes de pedir o CPF)
            controlador_prof = self.__controlador_sistema.controlador_profissionais
            if len(controlador_prof._ControladorProfissional__profissionais) == 0:
                controlador_prof.listar_profissionais()
                return

            controlador_prof.listar_profissionais()
            cpf_profissional = self.__limite_atendimento.pedir_string("Digite o CPF do Profissional: ")
            if cpf_profissional is None:
                return
                
            profissional = controlador_prof.buscar_profissional_por_cpf(cpf_profissional)
            if not profissional:
                raise ValueError("Profissional não encontrado.")

            # 4. Dados do Atendimento
            dados = self.__limite_atendimento.pegar_dados_atendimento()
            if dados is None: # Tratamento de cancelamento do formulário
                return
            
            # Validação de Horário
            hora_inicio = datetime.strptime(dados["horario_inicio"], "%H:%M").time()
            hora_fim = datetime.strptime(dados["horario_fim"], "%H:%M").time()
            if hora_inicio >= hora_fim:
                raise ValueError("Horário inválido: O fim do atendimento deve ser após o início.")

            # Mapeamento do Enum de Tipo Atendimento
            tipo_str = dados["tipo_atendimento"].upper()
            if tipo_str == "CONSULTA": tipo_enum = TipoAtendimento.CONSULTA
            elif tipo_str == "EXAME": tipo_enum = TipoAtendimento.EXAME
            elif tipo_str == "RETORNO": tipo_enum = TipoAtendimento.RETORNO
            elif tipo_str == "PROCEDIMENTO": tipo_enum = TipoAtendimento.PROCEDIMENTO
            elif tipo_str in ["EMERGÊNCIA", "EMERGENCIA"]: tipo_enum = TipoAtendimento.EMERGÊNCIA
            else: raise ValueError("Tipo de atendimento inválido.")

            # Criação do Atendimento
            novo_atendimento = Atendimento(
                clinica, 
                paciente, 
                profissional,
                dados["data"], 
                dados["horario_inicio"], 
                dados["horario_fim"], 
                tipo_enum, 
                dados["valor_total"]
            )

            if tipo_enum == TipoAtendimento.RETORNO:
                novo_atendimento.valor_total = 0.0

            self.__atendimentos.append(novo_atendimento)
            self.__limite_atendimento.mostrar_mensagem("Atendimento agendado com sucesso!")

        except ValueError as e:
            self.__limite_atendimento.mostrar_mensagem(f"Erro de Validação: {e}")
        except Exception as e:
            self.__limite_atendimento.mostrar_mensagem(f"Erro inesperado: {e}")

    def listar_atendimentos(self):
        if not self.__atendimentos:
            self.__limite_atendimento.mostrar_mensagem("Nenhum atendimento registrado.")
            return

        dados_atend = []
        for index, at in enumerate(self.__atendimentos):
            dados_atend.append({
                "id": index,
                "data": at.data,
                "paciente": at.paciente.nome,
                "clinica": at.clinica.nome,
                "profissional": at.profissional.nome,
                "tipo": at.tipo_atendimento.name if isinstance(at.tipo_atendimento, TipoAtendimento) else at.tipo_atendimento,
                "valor_total": at.valor_total,
                "valor_restante": at.calcular_valor_restante()
            })
        self.__limite_atendimento.mostrar_atendimentos(dados_atend)

    def excluir_atendimento(self):
        self.listar_atendimentos()
        if not self.__atendimentos:
            return
        
        try:
            id_atend = int(self.__limite_atendimento.pedir_string("Digite o ID do atendimento para excluir: "))
            atendimento = self.buscar_atendimento_por_id(id_atend)
            if atendimento:
                self.__atendimentos.remove(atendimento)
                self.__limite_atendimento.mostrar_mensagem("Atendimento excluído com sucesso!")
            else:
                self.__limite_atendimento.mostrar_mensagem("ID não encontrado.")
        except ValueError:
            self.__limite_atendimento.mostrar_mensagem("ID inválido. Digite um número.")

    def alterar_atendimento(self):
        self.listar_atendimentos()
        if not self.__atendimentos:
            return
            
        try:
            id_atend = int(self.__limite_atendimento.pedir_string("Digite o ID do atendimento para alterar: "))
            atendimento = self.buscar_atendimento_por_id(id_atend)
            if not atendimento:
                raise ValueError("Atendimento não encontrado.")
            
            novos_dados = self.__limite_atendimento.pegar_dados_atendimento()
            atendimento.data = novos_dados["data"]
            atendimento.horario_inicio = novos_dados["horario_inicio"]
            atendimento.horario_fim = novos_dados["horario_fim"]
            atendimento.valor_total = novos_dados["valor_total"]
            
            self.__limite_atendimento.mostrar_mensagem("Atendimento alterado com sucesso.")
        except ValueError as e:
            self.__limite_atendimento.mostrar_mensagem(f"Erro: {e}")

    def adicionar_procedimento(self):
        self.listar_atendimentos()
        if not self.__atendimentos:
            return
            
        try:
            id_atend = int(self.__limite_atendimento.pedir_string("Digite o ID do atendimento para adicionar procedimento: "))
            atendimento = self.buscar_atendimento_por_id(id_atend)
            if not atendimento:
                raise ValueError("Atendimento não encontrado.")

            dados_proc = self.__limite_atendimento.pegar_dados_procedimento()
            
            # Precisamos do profissional que realizou este procedimento
            cpf_prof = self.__limite_atendimento.pedir_string("Digite o CPF do profissional responsável pelo procedimento: ")
            prof_resp = self.__controlador_sistema.controlador_profissionais.buscar_profissional_por_cpf(cpf_prof)
            if not prof_resp:
                raise ValueError("Profissional não encontrado no sistema.")

            # Composição: O procedimento é instanciado com o profissional e pertence a este atendimento
            novo_procedimento = Procedimento(dados_proc["descricao"], dados_proc["custo"], prof_resp)
            atendimento.adicionar_procedimento(novo_procedimento) 
            
            # Atualiza o valor total do atendimento somando o custo do procedimento
            atendimento.valor_total += dados_proc["custo"]
            
            self.__limite_atendimento.mostrar_mensagem("Procedimento adicionado com sucesso!")
        except ValueError as e:
             self.__limite_atendimento.mostrar_mensagem(f"Erro: {e}")

    def registrar_pagamento(self):
        self.listar_atendimentos()
        if not self.__atendimentos:
            return
            
        try:
            id_atend = int(self.__limite_atendimento.pedir_string("Digite o ID do atendimento para pagar: "))
            atendimento = self.buscar_atendimento_por_id(id_atend)
            if not atendimento:
                raise ValueError("Atendimento não encontrado.")

            valor_devido = atendimento.calcular_valor_restante()
            if valor_devido <= 0:
                self.__limite_atendimento.mostrar_mensagem("Este atendimento já está totalmente pago!")
                return
                
            self.__limite_atendimento.mostrar_mensagem(f"Valor pendente: R$ {valor_devido:.2f}")
            dados_pag = self.__limite_atendimento.pegar_dados_pagamento()

            # Validação de Data (Regra 3)
            data_pagamento = datetime.strptime(dados_pag["data"], "%d-%m-%Y").date()
            data_atendimento = datetime.strptime(atendimento.data, "%d-%m-%Y").date()
            if data_pagamento > data_atendimento:
                raise ValueError("Pagamentos não podem ser realizados após a data do atendimento.")

            valor_pago = dados_pag["valor"]
            if valor_pago > valor_devido:
                self.__limite_atendimento.mostrar_mensagem(f"Valor excede a dívida. Registrando apenas o restante: R$ {valor_devido:.2f}")
                valor_pago = valor_devido

            tipo_pagamento = dados_pag["tipo_pagamento"] 
            novo_pagamento = None

            # Ordem correta dos parâmetros: data, atendimento, paciente, valor_pago
            if tipo_pagamento == 1:
                novo_pagamento = PagamentoDinheiro(dados_pag["data"], atendimento, atendimento.paciente, valor_pago)
            elif tipo_pagamento == 2:
                cpf_pix = self.__limite_atendimento.pedir_string("Digite o CPF do PIX: ")
                novo_pagamento = PagamentoPix(dados_pag["data"], atendimento, atendimento.paciente, valor_pago, cpf_pix)
            elif tipo_pagamento == 3:
                num_cartao = int(self.__limite_atendimento.pedir_string("Digite o número do cartão: "))
                bandeira = self.__limite_atendimento.pedir_string("Digite a bandeira: ")
                novo_pagamento = PagamentoCartao(dados_pag["data"], atendimento, atendimento.paciente, valor_pago, num_cartao, bandeira)
            else:
                raise ValueError("Tipo de pagamento inválido.")

            atendimento.adicionar_pagamento(novo_pagamento) 
            
            restante_agora = atendimento.calcular_valor_restante()
            self.__limite_atendimento.mostrar_mensagem(f"Pagamento registrado! Restante a pagar: R$ {restante_agora:.2f}")

        except ValueError as e:
            self.__limite_atendimento.mostrar_mensagem(f"Erro na validação: {e}")

    def abrir_menu(self):
        opcoes = {
            1: self.incluir_atendimento,
            2: self.listar_atendimentos,
            3: self.alterar_atendimento,
            4: self.excluir_atendimento,
            5: self.adicionar_procedimento,
            6: self.registrar_pagamento,
            0: self.retornar
        }

        while True:
            opcao = self.__limite_atendimento.tela_opcoes()
       
            if opcao == -1:
                self.__controlador_sistema.encerrar_sistema()
                break

            funcao_escolhida = opcoes.get(opcao)
            
            if funcao_escolhida:
                funcao_escolhida()
                if opcao == 0: 
                    break
            else:
                self.__limite_atendimento.mostrar_mensagem("Opção inválida!")

    def retornar(self):
        pass