class LimiteSistema:
    def tela_opcoes(self):
        print("\n")
        print("------ SISTEMA DE CLÍNICAS ------")
        print("1 - Clínicas")
        print("2 - Pacientes")
        print("3 - Profissionais")
        print("4 - Atendimentos")
        print("5 - Relatórios")
        print("0 - Encerrar Sistema") # <- Alterado de 6 para 0
        print("-" * 33)
        
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao in [0, 1, 2, 3, 4, 5]:
                    return opcao
                print("Opção inválida! Tente novamente.")
            except ValueError:
                print("Por favor, digite um número válido listado acima.")
                
    def mostrar_mensagem(self, msg: str):
        print(f"\n[SISTEMA]: {msg}")