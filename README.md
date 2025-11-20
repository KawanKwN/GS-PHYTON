Mapeador de Profissões para o Futuro do Trabalho
Global Solution / Computational Thinking with Python / FIAP 2025

Este projeto faz parte da avaliação da disciplina e tem como foco entender como as mudanças do mercado de trabalho impactam diferentes profissões, principalmente com o avanço da automação e da inteligência artificial.

A ideia foi criar uma ferramenta simples, mas funcional, que faz a triagem de profissionais, avalia o risco de automação de cada profissão e indica caminhos de requalificação. No final, todos os dados são organizados em um DataFrame e viram um relatório.

Objetivo do Projeto
Construir um sistema em Python que:
recebe dados de profissionais
identifica o nível de risco da profissão
sugere uma área de requalificação
organiza tudo em um DataFrame
gera relatórios e insights
utiliza todas as estruturas pedidas no enunciado
Estruturas Obrigatórias e Como Foram Aplicadas

1. Entrada de Dados
Os dados dos profissionais são coletados pelo terminal:

nome = input("Nome do profissional: ")
profissao = input("Profissão atual: ")
idade = entrada_inteiro("Idade: ")


2. Saída de Dados
Os resultados e relatórios são exibidos com print(), sempre de forma organizada para facilitar leitura.
3. Estruturas de Repetição
O menu principal roda com while True, permitindo cadastrar vários profissionais antes de fechar o programa. Também usei for para percorrer o DataFrame e montar relatórios.
4. Estruturas de Condição
As condições controlam tanto o menu quanto a classificação da profissão.
Exemplo:

if risco == "Alto":
    ...
Também usei condição para gerar o insight final com base nos dados coletados.
5. Funções
O código é separado em funções para ficar organizado:

entrada_inteiro()
classificar_risco_e_recomendacao()
coletar_um_profissional()
gerar_relatorios()
main()

Cada parte do processo fica isolada e mais fácil de manter.

6. Função dentro de Função
No relatório, usei uma função interna para calcular percentuais de forma local:

def gerar_relatorios(df):
    def formatar_percentual(qtd, total):
        return f"{(qtd / total) * 100:.1f}%"

Serve apenas para o relatório, então faz sentido deixá-la “escondida”.

7. DataFrame
Todos os profissionais coletados são organizados em um DataFrame:

df = pd.DataFrame(profissionais)

Isso permite contar categorias, percorrer dados e gerar relatório final.

Explicação das Principais Funções

entrada_inteiro()
Evita erros de digitação e garante que a idade e opções do menu sejam valores numéricos válidos.

classificar_risco_e_recomendacao()
Analisa a profissão com base em padrões de texto e retorna tanto o risco quanto a sugestão de requalificação.

coletar_um_profissional()
Organiza a triagem completa de um profissional e retorna um dicionário pronto para o DataFrame.

gerar_relatorios()
Exibe a lista de profissionais, a distribuição dos riscos e um resumo final com insights sobre o grupo analisado.

main()
Controla o fluxo do programa e o menu principal. Toda execução passa por ela.

Conexão com o Tema “O Futuro do Trabalho”
O projeto dialoga diretamente com o tema da Global Solution:
mostra como a automação afeta profissões diferentes
reforça a importância da requalificação
organiza dados para facilitar análise
apoia decisões pensando no cenário real do mercado

### Como Executar
Instale o pandas:
pip install pandas

Rode o programa:
python futuro_do_trabalho.py

Menu inicial:
1 - Fazer triagem
2 - Finalizar e gerar relatório

Exemplo de Saída (resumo) 
Nome: João
Profissão: Atendente
Idade: 23
Risco de Automação: Alto
Foco de Requalificação: Tecnologia e IA aplicada
--------------------------------------------------------
Distribuição por risco:
...
