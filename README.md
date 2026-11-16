# Controle Financeiro Pessoal

Aplicação de terminal desenvolvida em Python para registrar receitas e despesas, consultar o resumo financeiro, filtrar movimentações, exportar dados para CSV e gerar gráficos.

O projeto foi pensado como um projeto de aprendizado e portfólio, utilizando Python, SQLite, testes, tratamento de erros e Git/GitHub sem adicionar complexidade desnecessária.

## Funcionalidades

- Adicionar receitas
- Adicionar despesas
- Listar movimentações
- Consultar total de receitas, despesas e saldo
- Filtrar por tipo, categoria e período
- Excluir movimentações com confirmação
- Exportar movimentações para CSV
- Gerar gráfico de receitas x despesas
- Gerar gráfico de despesas por categoria
- Validar valores, datas, tipos e campos obrigatórios
- Persistir dados em SQLite
- Testar regras principais com pytest

## Tecnologias

- Python 3
- SQLite
- sqlite3
- csv
- datetime
- decimal
- pathlib
- pytest
- matplotlib
- Git/GitHub

## Estrutura do projeto

```text
controle-financeiro/
├── app/
│   ├── database/
│   │   └── connection.py
│   ├── models/
│   │   └── transaction.py
│   ├── services/
│   │   ├── transaction_service.py
│   │   └── report_service.py
│   ├── utils/
│   │   ├── validators.py
│   │   └── formatters.py
│   ├── cli/
│   │   └── menu.py
│   └── main.py
├── data/
├── exports/
├── tests/
│   ├── test_transactions.py
│   └── test_validators.py
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

## Banco de dados

O SQLite cria automaticamente `data/finance.db`.

Valores monetários são armazenados como inteiros em centavos. Por exemplo, R$ 10,50 é armazenado como `1050`. Essa estratégia evita os problemas de precisão comuns do `float` em cálculos financeiros.

O programa usa parâmetros nas consultas SQL, evitando concatenar diretamente entradas do usuário nas queries.

## Como executar

### 1. Criar ambiente virtual

No Windows:

```powershell
python -m venv .venv
```

### 2. Ativar

```powershell
.venv\Scripts\activate
```

### 3. Instalar dependências

```powershell
pip install -r requirements.txt
```

### 4. Executar

```powershell
python run.py
```

## Testes

```powershell
pytest -q
```

## Exportação CSV

No menu, escolha:

```text
6. Exportar dados para CSV
```

O arquivo será criado em:

```text
exports/transactions.csv
```

## Gráficos

No menu, escolha:

```text
7. Gerar gráfico
```

Serão gerados:

- `exports/receitas_vs_despesas.png`
- `exports/despesas_por_categoria.png`

## Exemplo de uso

```text
Descrição: Salário
Valor: 4000
Categoria: Trabalho
Data (DD/MM/AAAA): 19/08/2026
```

Resumo:

```text
========================================
          RESUMO FINANCEIRO
========================================
Total de receitas: R$ 4.000,00
Total de despesas: R$ 350,00
Saldo:             R$ 3.650,00
========================================
```

## O que aprendi

Este projeto pratica:

- variáveis e tipos de dados
- funções
- módulos e pacotes
- classes e dataclasses
- tratamento de exceções
- `Decimal`
- manipulação de datas
- SQLite e SQL
- CRUD
- consultas parametrizadas
- filtros
- exportação CSV
- geração de gráficos
- testes automatizados
- ambiente virtual
- organização de projeto
- Git/GitHub

## Próximas melhorias

- edição de movimentações
- categorias cadastradas em tabela própria
- filtros mais avançados
- relatório mensal
- testes de integração do banco
- interface gráfica em uma versão futura
- possível API em um projeto separado

## Git

Commits sugeridos:

```text
feat: initialize python project
feat: add sqlite database connection
feat: create transaction model
feat: implement transaction creation
feat: implement transaction listing
feat: add financial summary
feat: add transaction filters
feat: add csv export
feat: add financial charts
test: add transaction validation tests
test: add financial calculation tests
docs: add project README
```

O banco local e os arquivos gerados não devem ser enviados ao GitHub.


## Gestão de Configuração

O projeto utiliza um fluxo de branches, Pull Requests e validação automatizada para manter as alterações rastreáveis.

- [Plano de Gerenciamento de Configuração (PGC)](docs/PLANO_GCS.md)
- [Guia de onboarding e contribuição](docs/ONBOARDING.md)
- [Workflow de Integração Contínua (CI)](.github/workflows/ci.yml)
- [Verificação manual dos gates staging/production](.github/workflows/environment-gates.yml)

O workflow de CI instala as dependências, verifica a sintaxe Python e executa os testes automatizados com pytest. A configuração dos ambientes e das regras de proteção da main deve ser mantida nas Settings do repositório, conforme o PGC.

## Adendo e evidências da N2-P2

- [Adendo GCS - execução individual](docs/ADENDO_GCS_TRABALHO_INDIVIDUAL.md)
- [Índice de evidências N2-P2](docs/evidencias/RELATORIO_N2_P2.md)
- [Registro do push direto recusado (GH006)](docs/evidencias/PUSH_DIRETO_RECUSADO.md)

O adendo preserva o contexto do plano original e registra a execução individual, os controles efetivamente configurados e o requisito de par de revisão não realizado.
