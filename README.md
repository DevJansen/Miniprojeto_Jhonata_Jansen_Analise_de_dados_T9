## Mini projeto de análise de dados turma T9 - Senai/SC - SCTEC

- Aluno: Jhonata Jansen
- Professor: Renisson Souza
- Miniprojeto — Análise de Dados de Varejo

Projeto de análise de dados desenvolvido em Python para explorar uma base de vendas de varejo
(830.000 registros). O projeto cobre o fluxo completo de um trabalho de análise:
**importação → limpeza → resumo dos indicadores**, com saída formatada no terminal usando a
biblioteca **Rich**.

---

## Sumário

- [Sobre o projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Base de dados](#base-de-dados)
- [Pré-requisitos](#pré-requisitos)
- [Como usar](#como-usar)
- [Como a aplicação funciona](#como-a-aplicação-funciona)
- [Saída esperada](#saída-esperada)
- [Observações](#observações)

---

## Sobre o projeto

O objetivo é analisar o comportamento de compra dos clientes de uma rede de varejo, respondendo
perguntas como:

- Qual o volume de compras, clientes e registros da base?
- Qual o perfil dos clientes (gênero, estado civil, número de filhos, classe social)?
- Quais dias concentram mais compras?
- Quais categorias e produtos são os mais comprados?

A base utilizada é pública, disponível no Kaggle:
[Base Varejo](https://www.kaggle.com/datasets/namespaiva/base-varejo/data).

---

## Funcionalidades

| Funcionalidade | Onde está |
| --- | --- |
| Leitura da base CSV (`;` como separador) | `Importacao_dados.py` |
| Remoção de colunas 100% vazias | `Limpeza_dados.py` |
| Remoção de registros nulos | `Limpeza_dados.py` |
| Remoção de duplicatas | `Limpeza_dados.py` |
| Relatório de linhas removidas e mantidas | `Limpeza_dados.py` |
| Exportação da base tratada para CSV | `Limpeza_dados.py` |
| Cálculo dos indicadores (KPIs) do varejo | `Resumo.py` |
| Formatação de números no padrão brasileiro | `Formatacao.py` |
| Exibição do resumo em painel no terminal | `Resumo.py` + `rich` |

---

## Estrutura do projeto

```
Miniprojeto_Jhonata_Jansen_Analise_de_dados_T9/
├── Base_varejo.csv          # Base de dados original (Kaggle), separada por ";"
├── Importacao_dados.py      # Carrega o CSV em um DataFrame do pandas
├── Limpeza_dados.py         # Classe LimpezaDeDados (tratamento da base)
├── Resumo.py                # Calcula e imprime os indicadores do varejo
├── Formatacao.py            # Console Rich e função numero_br()
├── requirements.txt         # Dependências do projeto
├── README.md                # Este arquivo
└── venv/                    # Ambiente virtual (não versionado)
```

---

## Base de dados

Arquivo: `Base_varejo.csv` — 830.000 registros, separados por `;`, cobrindo o período de
**04/01/2019 a 08/12/2022**.

| Coluna | Descrição |
| --- | --- |
| `DATA` | Data da compra (formato `dd/mm/aaaa`) |
| `CO_ID` | Identificador da compra (carrinho) |
| `CL_ID` | Identificador do cliente |
| `CL_GENERO` | Gênero do cliente (`M` / `F`) |
| `CL_EC` | Estado civil (1 = casado, 2 = divorciado, 3 = separado, 4 = solteiro, 5 = viúvo) |
| `CL_FHL` | Número de filhos do cliente |
| `CL_SEG` | Classe/segmento do cliente (`A`, `B`, `C`) |
| `PR_ID` | Código (SKU) do produto |
| `PR_CAT` | Categoria do produto |
| `PR_NOME` | Nome do produto |

> A base original possui ainda 4 colunas extras totalmente vazias (`Unnamed: 10` a `Unnamed: 13`),
> que são eliminadas na etapa de limpeza.

---

## Pré-requisitos

- **Python 3.10+** (o projeto foi executado com Python 3.14)
- `pip` disponível no terminal

Bibliotecas principais: `pandas` e `rich`.

---

## Como usar

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd Miniprojeto_Jhonata_Jansen_Analise_de_dados_T9
```

### 2. Baixe a base de dados

Acesse [Base Varejo no Kaggle](https://www.kaggle.com/datasets/namespaiva/base-varejo/data),
baixe o arquivo CSV e salve-o na raiz do projeto com o nome **`Base_varejo.csv`**.

### 3. Crie e ative o ambiente virtual

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Prompt de Comando):**

```bat
python -m venv venv
venv\Scripts\activate.bat
```

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instale as dependências

Opção recomendada (todas as versões do projeto):

```bash
pip install -r requirements.txt
```

Opção mínima (apenas o necessário para este projeto):

```bash
pip install pandas rich
```

### 5. Execute os scripts na ordem

```bash
# 1) Verifica se a base foi carregada corretamente
python Importacao_dados.py

# 2) Limpa a base e gera o arquivo tratado
python Limpeza_dados.py

# 3) Exibe o resumo com os indicadores
python Resumo.py
```

Cada arquivo também pode ser importado como módulo em outro script Python:

```python
from Importacao_dados import importar_dados
from Limpeza_dados import LimpezaDeDados
from Resumo import mostrar_resumo

df = importar_dados()
df = LimpezaDeDados(df).executar().df
mostrar_resumo(df)
```

---

## Como a aplicação funciona

O projeto segue um pipeline simples de três etapas, onde cada script tem uma responsabilidade
única e pode ser executado de forma independente:

```
Base_varejo.csv
      │
      ▼
┌─────────────────────┐
│ Importacao_dados.py │  pd.read_csv(..., sep=";")
└─────────┬───────────┘
          │ DataFrame (830.000 linhas)
          ▼
┌─────────────────────┐
│  Limpeza_dados.py   │  remove colunas vazias → nulos → duplicatas
└─────────┬───────────┘
          │ Base tratada + relatório no terminal
          ▼
┌─────────────────────┐
│      Resumo.py      │  calcula os KPIs
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│   Formatacao.py     │  numero_br() + Console Rich
└─────────┬───────────┘
          │
          ▼
   Painel "Resumo varejo" no terminal
```

### Etapa 1 — Importação (`Importacao_dados.py`)

Define os caminhos dos arquivos a partir da pasta do próprio script (funciona independente de
onde o comando é executado) e expõe a função `importar_dados()`:

- `CAMINHO_CSV` → `Base_varejo.csv` (arquivo lido)
- `CAMINHO_CSV_ORIGINAL` → `Base_varejo_original.csv` (arquivo gerado pela limpeza)

A leitura usa `sep=";"`, pois o CSV do Kaggle é separado por ponto e vírgula. Ao rodar o arquivo
diretamente, ele imprime a quantidade de registros carregados e as 5 primeiras linhas.

### Etapa 2 — Limpeza (`Limpeza_dados.py`)

A classe `LimpezaDeDados` encapsula o tratamento em métodos encadeáveis (cada um retorna
`self`, permitindo chamadas em sequência):

| Método | O que faz |
| --- | --- |
| `remover_colunas_vazias()` | Remove colunas em que **todos** os valores são nulos (`dropna(axis=1, how="all")`) |
| `remover_nulos()` | Remove linhas com qualquer valor nulo (`dropna()`) |
| `removr_duplicados()` | Remove linhas duplicadas e reindexa o DataFrame |
| `executar()` | Executa as três etapas acima na ordem correta |
| `mostrar_relatorio()` | Exibe registros iniciais, removidos e finais |
| `salvar_novo_csv(caminho)` | Grava o resultado em CSV com `;` e sem o índice |

O construtor guarda `registros_iniciais`, usado depois para calcular quantas linhas foram
descartadas. Ao executar o arquivo diretamente, ele lê `Base_varejo.csv`, aplica a limpeza,
imprime o relatório e salva o resultado em `Base_varejo_original.csv`.

> Na base atual, as 4 colunas vazias são removidas e existem **96.553 linhas duplicadas**,
> restando **733.447 registros** após a limpeza.

### Etapa 3 — Resumo (`Resumo.py`)

A função `mostrar_resumo(df)` calcula os indicadores e monta o texto exibido no painel:

| Indicador | Como é calculado |
| --- | --- |
| Dia(s) com mais compras | `DATA.value_counts()` e seleção do(s) valor(es) máximo(s) |
| Total de registros | `len(df)` |
| Total de compras | `CO_ID.nunique()` |
| Total de clientes | `CL_ID.nunique()` |
| Mulheres / Homens | Clientes únicos filtrados por `CL_GENERO` (`F` / `M`) |
| Estado civil | Clientes únicos filtrados por `CL_EC` (1 a 5) |
| Média de filhos | Considera apenas a **compra mais recente de cada cliente** (`drop_duplicates` por `CL_ID` após ordenar por data) |
| Classes A / B / C | Clientes únicos filtrados por `CL_SEG` |
| Categoria(s) mais comprada(s) | `PR_CAT.mode()` (moda da coluna) |
| Produto(s) mais comprado(s) | Agrupamento por `PR_ID` + `PR_NOME`, contagem de linhas e seleção do máximo |

### Etapa 4 — Formatação (`Formatacao.py`)

- Cria uma instância global de `rich.console.Console`, reutilizada pelos outros módulos.
- `numero_br(valor, casas=0)` converte números para o padrão brasileiro:
  `830000` → `830.000` e `1.5` → `1,5` (troca `,` por `.` e vice-versa com um caractere
  temporário para evitar conflito).

O resultado final é impresso com `Panel(..., title="Resumo varejo:")`, deixando a saída
visualmente organizada no terminal.

---

## Saída esperada

**`python Importacao_dados.py`**

```
830000 registros carregados
        DATA  CO_ID  CL_ID CL_GENERO  CL_EC  CL_FHL CL_SEG  PR_ID    PR_CAT  ...
0 01/02/2019   1000    534         M      4       1      C     67   BEBIDAS  ...
```

**`python Limpeza_dados.py`**

```
Registros iniciais: 830000
Registros removidos: 96553
Registros finais: 733447
Base limpa salva em .../Base_varejo_original.csv
```

**`python Resumo.py`**

```
+---------------------------- Resumo varejo: -----------------------------+
|  Dia(s) com mais compras:  21/08/2020                                   |
|  Total de registros:  830.000                                           |
|  Total de compras:  18.471                                              |
|  Total de clientes:  1.000                                              |
|  Total de mulheres:  519                                                |
|  Total de homens:  481                                                  |
|  Total de casados(as):  233                                             |
|  Total de divorciados(as):  238                                         |
|  Total de separados(as):  250                                           |
|  Total de solteiros(as):  251                                           |
|  Total de viúvos(as):  28                                               |
|  Média de filhos:  1                                                    |
|  Total de clientes classe A:  84                                        |
|  Total de clientes classe B:  645                                       |
|  Total de clientes classe C:  271                                       |
|  Categoria(s) mais comprada(s):  ALIMENTOS                              |
|  Produto(s) mais comprado(s):  SKU 93 - AGUA SANITARIA (3.773 unidades) |
+-------------------------------------------------------------------------+
```

---

## Observações

- **Nomes dos arquivos:** o script de limpeza lê `Base_varejo.csv` e grava o resultado em
  `Base_varejo_original.csv`. Ou seja, o arquivo com o sufixo `_original` é, na prática, a
  **saída tratada**. Se preferir outra convenção (ex.: `Base_varejo_limpa.csv`), basta ajustar
  a constante `CAMINHO_CSV_ORIGINAL` em `Importacao_dados.py`.
- **Codificação do terminal:** no Windows, o painel pode exibir acentos quebrados (`vi�vos`)
  dependendo do code page. Executar com `chcp 65001` ou no Windows Terminal resolve.
- **Método `removr_duplicados`:** o nome contém um erro de digitação (`removr`), mantido para
  não quebrar as chamadas existentes. Ao renomear, atualize também `executar()`.
- **Ambiente virtual:** a pasta `venv/` está listada no `.gitignore` e não deve ser versionada.
- **Dados sensíveis:** a base é pública (Kaggle), portanto não há dados pessoais reais.
