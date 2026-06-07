class LimiteProfissional:
    def tela_opcoes(self):
        print("\n--- MÓDULO DE PROFISSIONAIS ---")
        print("1 - Cadastrar Profissional")
        print("2 - Listar Profissionais")
        print("3 - Alterar Profissional")
        print("4 - Excluir Profissional")
        print("0 - Retornar")
        
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def pegar_dados_profissional(self):
        print("\n--- Dados do Profissional ---")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        celular = input("Celular: ")
        especialidade = input("Especialidade: ")
        registro = input("Registro Profissional: ")
        
        return {
            "nome": nome, "cpf": cpf, "celular": celular, 
            "especialidade": especialidade, "registro_profissional": registro
        }

    def selecionar_profissional(self):
        return input("Digite o CPF do Profissional que deseja selecionar: ")

    def mostrar_profissionais(self, dados_profissionais):
        print("\n--- Profissionais Cadastrados ---")
        for prof in dados_profissionais:
            print(f"Nome: {prof['nome']} | CPF: {prof['cpf']} | Reg: {prof['registro_profissional']}")
            print(f"Celular: {prof['celular']} | Especialidade: {prof['especialidade']}")
            print("-" * 20)

    def mostrar_mensagem(self, msg: str):
        print(f"\n[PROFISSIONAL]: {msg}")