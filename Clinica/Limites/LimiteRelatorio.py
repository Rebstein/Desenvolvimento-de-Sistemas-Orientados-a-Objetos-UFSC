class LimiteRelatorio:
    def tela_opcoes(self):
        print("\n--- MÓDULO DE RELATÓRIOS ---")
        print("1 - Clínicas com maior número de atendimentos")
        print("2 - Atendimentos mais caros e mais baratos")
        print("3 - Procedimentos mais populares")
        print("4 - Procedimentos mais caros e mais baratos")
        print("0 - Retornar")
        
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def mostrar_mensagem(self, msg: str):
        print(f"\n[RELATÓRIO]: {msg}")

    def mostrar_relatorio_clinicas(self, ranking: list):
        print("\n=== CLÍNICAS COM MAIS ATENDIMENTOS ===")
        for posicao, (clinica, quantidade) in enumerate(ranking, start=1):
            print(f"{posicao}º - {clinica}: {quantidade} atendimento(s)")
        print("=======================================\n")

    def mostrar_relatorio_atendimentos_extremos(self, dados: dict):
        print("\n=== ATENDIMENTOS EXTREMOS ===")
        print("-> MAIS CARO:")
        print(f"   ID: {dados['caro_id']} | Data: {dados['caro_data']} | Valor: R${dados['caro_valor']:.2f}")
        print("-> MAIS BARATO:")
        print(f"   ID: {dados['barato_id']} | Data: {dados['barato_data']} | Valor: R${dados['barato_valor']:.2f}")
        print("=============================\n")

    def mostrar_relatorio_procedimentos_populares(self, ranking: list):
        print("\n=== PROCEDIMENTOS MAIS POPULARES ===")
        for posicao, (proc, quantidade) in enumerate(ranking, start=1):
            print(f"{posicao}º - {proc}: realizado {quantidade} vez(es)")
        print("====================================\n")

    def mostrar_relatorio_procedimentos_extremos(self, dados: dict):
        print("\n=== PROCEDIMENTOS EXTREMOS ===")
        print("-> MAIS CARO:")
        print(f"   {dados['caro_desc']} - Custo: R${dados['caro_custo']:.2f}")
        print("-> MAIS BARATO:")
        print(f"   {dados['barato_desc']} - Custo: R${dados['barato_custo']:.2f}")
        print("==============================\n")