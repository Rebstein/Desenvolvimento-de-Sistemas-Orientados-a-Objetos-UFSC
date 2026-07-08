from DAOs.AtendimentoDao import AtendimentoDAO
from datetime import datetime, time
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
        self.__atendimento_dao = AtendimentoDAO()
        self.__limite_atendimento = LimiteAtendimento()
    
    @property
    def atendimentos(self):
        return self.__atendimento_dao.get_all()

    def buscar_atendimento_por_id(self, id_atendimento: int):
        # CORREÇÃO: Passa a buscar o atendimento diretamente pela chave numérica no DAO
        return self.__atendimento_dao.get(id_atendimento)

    def incluir_atendimento(self):
        try:
            controlador_cli = self.__controlador_sistema.controlador_clinicas
            
            controlador_cli.listar_clinicas()
            nome_clinica = self.__limite_atendimento.pedir_string("Digite o nome da Clínica para o atendimento:")
            if nome_clinica is None: return

            clinica = controlador_cli.buscar_clinica_por_nome(nome_clinica)
            if clinica is None:
                self.__limite_atendimento.mostrar_mensagem("Erro: Clínica não encontrada!")
                return

            # Seleção do Paciente via pedir_string
            controlador_pac = self.__controlador_sistema.controlador_pacientes
            controlador_pac.listar_pacientes()
            cpf_paciente = self.__limite_atendimento.pedir_string("Digite o CPF do Paciente:")
            if cpf_paciente is None: return
            paciente = controlador_pac.buscar_paciente_por_cpf(cpf_paciente)
            if paciente is None:
                self.__limite_atendimento.mostrar_mensagem("Erro: Paciente não cadastrado!")
                return

            # Seleção do Profissional via pedir_string
            controlador_prof = self.__controlador_sistema.controlador_profissionais
            controlador_prof.listar_profissionais()
            cpf_profissional = self.__limite_atendimento.pedir_string("Digite o CPF do Profissional:")
            if cpf_profissional is None: return
            profissional = controlador_prof.buscar_profissional_por_cpf(cpf_profissional)
            if profissional is None:
                self.__limite_atendimento.mostrar_mensagem("Erro: Profissional não cadastrado!")
                return

            # Coleta de dados do Atendimento
            dados_atend = self.__limite_atendimento.pegar_dados_atendimento()
            if dados_atend is None: return

            # Conversão de Strings de data/hora para objetos nativos
            data_limpa = dados_atend["data"].replace("/", "-")
            data_obj = datetime.strptime(data_limpa, "%d-%m-%Y").date()
            horario_inicio_obj = datetime.strptime(dados_atend["horario_inicio"], "%H:%M").time()
            horario_fim_obj = datetime.strptime(dados_atend["horario_fim"], "%H:%M").time()

            # Horário de Funcionamento da Clínica
            try:
                cli_inicio = datetime.strptime(clinica.horario_funcionamento_inicio, "%H:%M").time()
                cli_fim = datetime.strptime(clinica.horario_funcionamento_fim, "%H:%M").time()
            except Exception:
                raise ValueError("Os horários de funcionamento da clínica estão em formato inválido (use HH:MM).")

            if horario_inicio_obj < cli_inicio or horario_fim_obj > cli_fim:
                self.__limite_atendimento.mostrar_mensagem(
                    f"Erro: O atendimento está fora do horário de funcionamento da clínica!\n"
                    f"Funcionamento da Clínica: {clinica.horario_funcionamento_inicio} até {clinica.horario_funcionamento_fim}"
                )
                return
            
            if horario_inicio_obj >= horario_fim_obj:
                self.__limite_atendimento.mostrar_mensagem("Erro: Horário de início deve ser menor que o horário de fim.")
                return

            # Mapeamento do texto do tipo de atendimento para o Enum correspondente
            tipo_str = dados_atend["tipo_atendimento"].upper()
            if tipo_str == "CONSULTA": tipo_enum = TipoAtendimento.CONSULTA
            elif tipo_str == "EXAME": tipo_enum = TipoAtendimento.EXAME
            elif tipo_str == "RETORNO": tipo_enum = TipoAtendimento.RETORNO
            elif tipo_str == "PROCEDIMENTO": tipo_enum = TipoAtendimento.PROCEDIMENTO
            elif tipo_str in ["EMERGÊNCIA", "EMERGENCIA"]: tipo_enum = TipoAtendimento.EMERGÊNCIA
            else: raise ValueError("Tipo de atendimento inválido.")

            novo_atendimento = Atendimento(
                clinica, paciente, profissional=profissional, 
                data=data_obj, horario_inicio=horario_inicio_obj, horario_fim=horario_fim_obj,
                tipo_atendimento=tipo_enum, valor_total=dados_atend["valor_total"]
            )

            if tipo_enum == TipoAtendimento.RETORNO:
                novo_atendimento.valor_total = 0.0

            # CORREÇÃO: Atribui a posição da lista/dicionário como ID numérico antes de enviar ao DAO
            novo_id = len(self.__atendimento_dao.get_all())
            novo_atendimento.id = novo_id

            self.__atendimento_dao.add(novo_atendimento)
            self.__limite_atendimento.mostrar_mensagem("Atendimento agendado com sucesso!")

        except ValueError as e:
            self.__limite_atendimento.mostrar_mensagem(f"Erro de validação nos dados: {e}")
        except Exception as e:
            self.__limite_atendimento.mostrar_mensagem(f"Erro inesperado: {e}")

    def listar_atendimentos(self):
        todos = self.__atendimento_dao.get_all()
        dados_lista = []
        
        if not todos or len(todos) == 0:
            self.__limite_atendimento.mostrar_mensagem("Nenhum atendimento cadastrado no sistema.")
            return

        # CORREÇÃO: Agora mapeia usando o id armazenado no próprio objeto atendimento
        for at in todos:
            if hasattr(at.data, "strftime"):
                data_formatada = at.data.strftime("%d-%m-%Y")
            else:
                data_formatada = str(at.data).replace("/", "-")

            tipo_formatado = at.tipo_atendimento.name if hasattr(at.tipo_atendimento, 'name') else str(at.tipo_atendimento)

            dados_lista.append({
                "id": at.id,  
                "data": data_formatada,
                "tipo": tipo_formatado,
                "paciente": at.paciente.nome,
                "profissional": at.profissional.nome,
                "clinica": at.clinica.nome,
                "valor_total": at.valor_total,
                "valor_restante": at.calcular_valor_restante()
            })
            
        self.__limite_atendimento.mostrar_atendimentos(dados_lista)

    def alterar_atendimento(self):
        todos = self.__atendimento_dao.get_all()
        if len(todos) == 0:
            self.__limite_atendimento.mostrar_mensagem("Nenhum atendimento agendado.")
            return

        self.listar_atendimentos()
        id_string = self.__limite_atendimento.pedir_string("Digite o ID do atendimento que deseja alterar:")
        if id_string is None: return

        try:
            id_atend = int(id_string)
            atendimento = self.buscar_atendimento_por_id(id_atend)
            if atendimento is None:
                self.__limite_atendimento.mostrar_mensagem("Erro: Atendimento não encontrado!")
                return

            dados_atend = self.__limite_atendimento.pegar_dados_atendimento()
            if dados_atend is None: return

            data_limpa = dados_atend["data"].replace("/", "-")
            data_obj = datetime.strptime(data_limpa, "%d-%m-%Y").date()
            horario_inicio_obj = datetime.strptime(dados_atend["horario_inicio"], "%H:%M").time()
            horario_fim_obj = datetime.strptime(dados_atend["horario_fim"], "%H:%M").time()

            cli_inicio = datetime.strptime(atendimento.clinica.horario_funcionamento_inicio, "%H:%M").time()
            cli_fim = datetime.strptime(atendimento.clinica.horario_funcionamento_fim, "%H:%M").time()

            if horario_inicio_obj < cli_inicio or horario_fim_obj > cli_fim:
                self.__limite_atendimento.mostrar_mensagem(
                    f"Erro: Horário fora do expediente da clínica ({atendimento.clinica.horario_funcionamento_inicio} - {atendimento.clinica.horario_funcionamento_fim})."
                )
                return

            tipo_str = dados_atend["tipo_atendimento"].upper()
            if tipo_str == "CONSULTA": tipo_enum = TipoAtendimento.CONSULTA
            elif tipo_str == "EXAME": tipo_enum = TipoAtendimento.EXAME
            elif tipo_str == "RETORNO": tipo_enum = TipoAtendimento.RETORNO
            elif tipo_str == "PROCEDIMENTO": tipo_enum = TipoAtendimento.PROCEDIMENTO
            elif tipo_str in ["EMERGÊNCIA", "EMERGENCIA"]: tipo_enum = TipoAtendimento.EMERGÊNCIA
            else: raise ValueError("Tipo inválido.")

            atendimento.data = data_obj
            atendimento.horario_inicio = horario_inicio_obj
            atendimento.horario_fim = horario_fim_obj
            atendimento.tipo_atendimento = tipo_enum
            atendimento.valor_total = dados_atend["valor_total"]

            if tipo_enum == TipoAtendimento.RETORNO:
                atendimento.valor_total = 0.0

            # CORREÇÃO: Garante que chama o update do DAO utilizando a própria chave numérica do id
            if hasattr(self.__atendimento_dao, 'update'):
                self.__atendimento_dao.update(atendimento)
            else:
                self.__atendimento_dao.add(atendimento)

            self.__limite_atendimento.mostrar_mensagem("Atendimento alterado com sucesso!")
        except Exception as e:
            self.__limite_atendimento.mostrar_mensagem(f"Erro ao alterar: {e}")

    def excluir_atendimento(self):
        todos = self.__atendimento_dao.get_all()
        if len(todos) == 0:
            self.__limite_atendimento.mostrar_mensagem("Nenhum atendimento cadastrado.")
            return

        self.listar_atendimentos()
        id_string = self.__limite_atendimento.pedir_string("Digite o ID do atendimento que deseja excluir:")
        if id_string is None: return

        try:
            id_atend = int(id_string)
            atendimento = self.buscar_atendimento_por_id(id_atend)
            if atendimento is None:
                self.__limite_atendimento.mostrar_mensagem("Erro: Atendimento não encontrado!")
            else:
                # CORREÇÃO: Passa explicitamente o id (chave numérica int) exigido no método do seu DAO
                self.__atendimento_dao.remove(atendimento.id)
                self.__limite_atendimento.mostrar_mensagem("Atendimento excluído com sucesso!")
        except ValueError:
            self.__limite_atendimento.mostrar_mensagem("Erro: ID inválido.")

    def adicionar_procedimento(self):
        self.listar_atendimentos()
        id_string = self.__limite_atendimento.pedir_string("Digite o ID do atendimento:")
        if id_string is None: return

        try:
            id_atend = int(id_string)
            atendimento = self.buscar_atendimento_por_id(id_atend)
            if atendimento is None:
                self.__limite_atendimento.mostrar_mensagem("Erro: Atendimento não encontrado!")
                return

            dados_proc = self.__limite_atendimento.pegar_dados_procedimento()
            if dados_proc is None: return

            novo_procedimento = Procedimento(
                dados_proc["descricao"],
                dados_proc["custo"],
                atendimento.profissional
            )
            atendimento.adicionar_procedimento(novo_procedimento)
            atendimento.valor_total += dados_proc["custo"]
            
            if hasattr(self.__atendimento_dao, 'update'):
                self.__atendimento_dao.update(atendimento)
            else:
                self.__atendimento_dao.add(atendimento)
                
            self.__limite_atendimento.mostrar_mensagem("Procedimento adicionado com sucesso!")
        except ValueError:
            self.__limite_atendimento.mostrar_mensagem("Erro: ID inválido.")

    def registrar_pagamento(self):
        self.listar_atendimentos()
        id_string = self.__limite_atendimento.pedir_string("Digite o ID do atendimento para pagar:")
        if id_string is None: return

        try:
            id_atend = int(id_string)
            atendimento = self.buscar_atendimento_por_id(id_atend)
            if atendimento is None:
                self.__limite_atendimento.mostrar_mensagem("Erro: Atendimento não encontrado!")
                return

            restante = atendimento.calcular_valor_restante()
            if restante <= 0:
                self.__limite_atendimento.mostrar_mensagem("Este atendimento já está totalmente pago!")
                return

            self.__limite_atendimento.mostrar_mensagem(f"Valor pendente: R$ {restante:.2f}")
            dados_pag = self.__limite_atendimento.pegar_dados_pagamento()
            if dados_pag is None: return

            valor_pago = dados_pag["valor"]
            if valor_pago <= 0 or valor_pago > restante:
                self.__limite_atendimento.mostrar_mensagem(f"Erro: Valor inválido.")
                return

            tipo = dados_pag["tipo_pagamento"]
            if tipo == 1:
                novo_pagamento = PagamentoDinheiro(dados_pag["data"], atendimento, atendimento.paciente, valor_pago)
            elif tipo == 2:
                # CORREÇÃO MVC: Chama a View para pedir o texto
                cpf_pagador = self.__limite_atendimento.pedir_cpf_pix()
                if cpf_pagador is None: return
                novo_pagamento = PagamentoPix(dados_pag["data"], atendimento, atendimento.paciente, valor_pago, cpf_pagador)
            elif tipo == 3:
                # CORREÇÃO MVC: Chama a View para pedir os dados do cartão
                dados_cartao = self.__limite_atendimento.pedir_dados_cartao()
                if dados_cartao is None: return
                num_cartao, bandeira = dados_cartao
                novo_pagamento = PagamentoCartao(dados_pag["data"], atendimento, atendimento.paciente, valor_pago, int(num_cartao), bandeira)

            atendimento.adicionar_pagamento(novo_pagamento)
            
            if hasattr(self.__atendimento_dao, 'update'):
                self.__atendimento_dao.update(atendimento)
            else:
                self.__atendimento_dao.add(atendimento)
                
            restante_agora = atendimento.calcular_valor_restante()
            self.__limite_atendimento.mostrar_mensagem(f"Pagamento registrado! Restante: R$ {restante_agora:.2f}")
        except Exception as e:
            self.__limite_atendimento.mostrar_mensagem(f"Erro no pagamento: {e}")

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
                self.__limite_atendimento.mostrar_mensagem("Opção Inválida!")

    def retornar(self):
        pass