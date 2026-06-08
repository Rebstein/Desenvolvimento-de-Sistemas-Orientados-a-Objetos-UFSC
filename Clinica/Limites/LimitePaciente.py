class LimitePaciente:
    def tela_opcoes(self):
        print("\n------ PACIENTES ------")
        print("1 - Cadastrar Paciente")
        print("2 - Listar Pacientes")
        print("3 - Alterar Paciente")
        print("4 - Excluir Paciente")
        print("0 - Retornar")
        print("-" * 23)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def pegar_dados_paciente(self):
        print("\n------ Dados do Paciente ------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        celular = input("Celular: ")
        data_nascimento = input("Data de Nascimento (YYYY-MM-DD): ")
        
        return {"nome": nome, "cpf": cpf, "celular": celular, "data_nascimento": data_nascimento}

    def selecionar_paciente(self):
        return input("Digite o CPF do Paciente que deseja selecionar: ")

    def mostrar_pacientes(self, dados_pacientes):
        print("\n-------- Pacientes Cadastrados --------")
        for paciente in dados_pacientes:
            print(f"Nome: {paciente['nome']} | CPF: {paciente['cpf']}")
            print(f"Celular: {paciente['celular']} | Nasc: {paciente['data_nascimento']}")
            print("-" * 39)

    def mostrar_mensagem(self, msg: str):
        print(f"\n[PACIENTE]: {msg}")