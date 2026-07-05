import sys
from Controladores.ControladorClinica import ControladorClinica
from Controladores.ControladorPaciente import ControladorPaciente
from Controladores.ControladorProfissional import ControladorProfissional
from Controladores.ControladorAtendimento import ControladorAtendimento
from Controladores.ControladorRelatorio import ControladorRelatorio
from Limites.LimiteSistema import LimiteSistema

class ControladorSistema:
    def __init__(self):
        self.__limite_sistema = LimiteSistema()
        
        self.__controlador_clinicas = ControladorClinica(self)
        self.__controlador_pacientes = ControladorPaciente(self)
        self.__controlador_profissionais = ControladorProfissional(self)
        self.__controlador_atendimentos = ControladorAtendimento(self)
        self.__controlador_relatorios = ControladorRelatorio(self)

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

    def inicializar_sistema(self):
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
            
            # Se o usuário fechar a janela no 'X', o PySimpleGUI retorna None ou -1.
            # Tratar isso para fechar o sistema de forma segura.
            if opcao == 0 or opcao is None or opcao == -1:
                self.encerrar_sistema()
                break
                
            funcao_escolhida = opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__limite_sistema.mostrar_mensagem("Opção inválida! Digite um número do menu.")

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