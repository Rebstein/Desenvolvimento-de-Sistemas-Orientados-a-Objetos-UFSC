import sys
from Controladores.ControladorClinica import ControladorClinica
from Controladores.ControladorPaciente import ControladorPaciente
from Controladores.ControladorProfissional import ControladorProfissional
from Controladores.ControladorAtendimento import ControladorAtendimento
from Controladores.ControladorRelatorio import ControladorRelatorio
from Limites.LimiteSistema import LimiteSistema

class ControladorSistema:
    def __init__(self):
        # 1. Instanciamos o Limite (Tela Principal)
        self.__limite_sistema = LimiteSistema()
        
        # 2. Inicializamos as variáveis dos sub-controladores
        self.__controlador_clinicas = None
        self.__controlador_pacientes = None
        self.__controlador_profissionais = None
        self.__controlador_atendimentos = None
        self.__controlador_relatorios = None
        
        # 3. Instanciamos passando o 'self' para que eles conheçam este Maestro
        self.__controlador_clinicas = ControladorClinica(self)
        self.__controlador_pacientes = ControladorPaciente(self)
        self.__controlador_profissionais = ControladorProfissional(self)
        self.__controlador_atendimentos = ControladorAtendimento(self)
        self.__controlador_relatorios = ControladorRelatorio(self)

    # --- GETTERS (Essenciais para a comunicação entre controladores) ---
    @property
    def controlador_clinicas(self):
        return self.__controlador_clinicas

    @property
    def controlador_pacientes(self):
        return self.__controlador_pacientes

    @property
    def controlador_profissionais(self):
        return self.__controlador_profissionais

    @property
    def controlador_atendimentos(self):
        return self.__controlador_atendimentos

    @property
    def controlador_relatorios(self):
        return self.__controlador_relatorios

    # --- FLUXO DE EXECUÇÃO ---
    def inicializar_sistema(self):
        # Este é o método que será chamado pelo arquivo main.py
        self.abrir_menu()

    def abrir_menu(self):
        opcoes = {
            1: self.cadastrar_clinicas,
            2: self.cadastrar_pacientes,
            3: self.cadastrar_profissionais,
            4: self.gerenciar_atendimentos,
            5: self.gerar_relatorios,
            0: self.encerrar_sistema
        }

        while True:
            opcao = self.__limite_sistema.tela_opcoes()
            funcao_escolhida = opcoes.get(opcao)
            
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__limite_sistema.mostrar_mensagem("Opção inválida! Digite um número do menu.")

    # --- REDIRECIONAMENTOS ---
    # Estes métodos apenas "passam a bola" para o controlador específico abrir o seu próprio menu
    def cadastrar_clinicas(self):
        self.__controlador_clinicas.abrir_menu()

    def cadastrar_pacientes(self):
        self.__controlador_pacientes.abrir_menu()

    def cadastrar_profissionais(self):
        self.__controlador_profissionais.abrir_menu()

    def gerenciar_atendimentos(self):
        self.__controlador_atendimentos.abrir_menu()

    def gerar_relatorios(self):
        self.__controlador_relatorios.abrir_menu()

    def encerrar_sistema(self):
        self.__limite_sistema.mostrar_mensagem("Encerrando o Sistema de Clínicas... Até logo!")
        sys.exit(0)

    