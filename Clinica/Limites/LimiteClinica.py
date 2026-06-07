class LimiteClinica:
    def tela_opcoes(self):
        print("\n--- MÓDULO DE CLÍNICAS ---")
        print("1 - Cadastrar Clínica")
        print("2 - Listar Clínicas")
        print("3 - Alterar Clínica")
        print("4 - Excluir Clínica")
        print("0 - Retornar") # <- Alterado de 6 para 0
        
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def pegar_dados_clinica(self):
        print("\n--- Dados da Clínica ---")
        nome = input("Nome da Clínica: ")
        cidade = input("Cidade: ")
        descricao = input("Descrição: ")
        
        return {"nome": nome, "cidade": cidade, "descricao": descricao}

    def selecionar_clinica(self):
        return input("Digite o NOME da Clínica que deseja selecionar: ")

    def mostrar_clinicas(self, dados_clinicas):
        print("\n--- Clínicas Cadastradas ---")
        for clinica in dados_clinicas:
            print(f"Nome: {clinica['nome']} | Cidade: {clinica['cidade']}")
            print(f"Descrição: {clinica['descricao']}")
            print("-" * 20)

    def mostrar_mensagem(self, msg: str):
        print(f"\n[CLÍNICA]: {msg}")