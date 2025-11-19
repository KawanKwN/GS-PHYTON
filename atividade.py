"""
Projeto: Mapeador de Profissões para o Futuro do Trabalho
Tema: O Futuro do Trabalho (Global Solution FIAP 2025)

Kawan Oliveira Amorim 562197
Alana Vieira Batista Rm563796
"""

import pandas as pd


# FUNÇÕES DE ENTRADA

def entrada_inteiro(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("⚠️ Digite um número inteiro válido.")

# LÓGICA DE CLASSIFICAÇÃO

def classificar_risco_e_recomendacao(profissao: str) -> tuple[str, str]:
    texto = profissao.lower()

    if any(p in texto for p in [
        "caixa", "atendimento", "telemarketing", "call center",
        "operador", "digitador", "repetitivo"
    ]):
        risco = "Alto"
        foco = "Requalificação em tecnologia, atendimento digital e IA aplicada ao cliente"

    elif any(p in texto for p in [
        "analista de dados", "cientista de dados", "engenheiro de dados",
        "programador", "desenvolvedor", "dev", "software"
    ]):
        risco = "Baixo"
        foco = "Aprofundar IA, automação, liderança técnica e arquitetura de sistemas"

    elif any(p in texto for p in [
        "professor", "educador", "psicólogo", "psicologa", "enfermeiro",
        "enfermeira", "médico", "medico", "dentista", "fonoaudiólogo",
        "assistente social"
    ]):
        risco = "Médio"
        foco = "Uso de IA como apoio, teleatendimento e habilidades socioemocionais"

    else:
        risco = "Médio"
        foco = "Desenvolver competências digitais, pensamento crítico e colaboração"

    return risco, foco


# COLETA DE PROFISSIONAL (1 pessoa)


def coletar_um_profissional() -> dict:
    """
    Coleta um único profissional.
    Só é chamada após o usuário escolher no menu.
    """

    print("\n=== TRIAGEM DO PROFISSIONAL ===")

    nome = input("Nome do profissional: ").strip()
    profissao = input("Profissão atual: ").strip()
    idade = entrada_inteiro("Idade: ")

    risco, foco = classificar_risco_e_recomendacao(profissao)

    print(f"\n➡️ {nome} classificado com RISCO {risco.upper()}.")
    print(f"   Foco de requalificação indicado: {foco}\n")

    return {
        "Nome": nome,
        "Profissao": profissao,
        "Idade": idade,
        "Risco_Automacao": risco,
        "Foco_Requalificacao": foco,
    }


# RELATÓRIOS


def gerar_relatorios(df: pd.DataFrame) -> None:

    def formatar_percentual(qtd: int, total: int) -> str:
        if total == 0:
            return "0%"
        return f"{(qtd / total) * 100:.1f}%"

    total = len(df)

    print("\n================== LISTA DE PROFISSIONAIS ==================\n")

    for _, row in df.iterrows():
        print(f"Nome: {row['Nome']}")
        print(f"Profissão: {row['Profissao']}")
        print(f"Idade: {row['Idade']}")
        print(f"Risco de Automação: {row['Risco_Automacao']}")
        print(f"Foco de Requalificação: {row['Foco_Requalificacao']}")
        print("-" * 55)

    print("\n================ DISTRIBUIÇÃO POR RISCO ===================")
    cont_risco = df["Risco_Automacao"].value_counts()
    for risco, qtd in cont_risco.items():
        print(f"- {risco}: {qtd} ({formatar_percentual(qtd, total)})")

    print("\n========= ÁREAS SUGERIDAS DE REQUALIFICAÇÃO ================")
    cont_foco = df["Foco_Requalificacao"].value_counts()
    for foco, qtd in cont_foco.items():
        print(f"- {foco}: {qtd} ({formatar_percentual(qtd, total)})")

    print("\n==================== INSIGHT AUTOMÁTICO ====================")
    if "Alto" in cont_risco and cont_risco["Alto"] / total > 0.5:
        print("⚠️ Mais de 50% estão em profissões de ALTO risco.")
        print("   Necessário implementar reskilling imediatamente.")
    else:
        print("✅ A maioria não está em risco elevado.")
        print("   Continue promovendo competências digitais e IA aplicada.")

    print("\n============================================================\n")


# FUNÇÃO PRINCIPAL COM MENU INTELIGENTE


def main():

    profissionais = []

    while True:

        # MENU DEPENDENDO SE JÁ EXISTE CADASTRO
        print("\n=== MENU ===")

        if len(profissionais) == 0:
            print("1 - Fazer triagem")
        else:
            print("1 - Adicionar profissional para triagem")

        print("2 - Finalizar e gerar relatório")

        opcao = entrada_inteiro("Escolha uma opção: ")

        if opcao == 1:
            pessoa = coletar_um_profissional()
            profissionais.append(pessoa)

        elif opcao == 2:
            break

        else:
            print("⚠️ Opção inválida. Tente novamente.")

    if not profissionais:
        print("Nenhum profissional cadastrado. Encerrando.")
        return

    df = pd.DataFrame(profissionais)

    gerar_relatorios(df)



# PONTO DE ENTRADA


if __name__ == "__main__":
    main()
