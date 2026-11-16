# Guia de onboarding — Controle Financeiro Pessoal

Este guia apresenta os passos para preparar, executar e contribuir com o projeto.

## 1. Requisitos
- Python 3 instalado.
- Git instalado.
- Acesso ao repositório: https://github.com/CrisCastanheira/controle-financeiro-pessoal.

## 2. Preparar o ambiente local
Clone o repositório e entre na pasta:

```bash
git clone https://github.com/CrisCastanheira/controle-financeiro-pessoal.git
cd controle-financeiro-pessoal
```

No Windows, crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## 3. Executar e testar
Execute a aplicação com `python run.py` e a suíte de testes com:

```bash
python -m pytest -q
```

## 4. Fluxo de mudança
1. Atualize a branch main (`git switch main` e `git pull`).
2. Crie uma branch curta, por exemplo `feature/relatorio-mensal` ou `fix/validacao-data`.
3. Faça a alteração e execute os testes.
4. Registre a mudança com Conventional Commits, por exemplo `feat(report): adiciona resumo mensal`.
5. Envie a branch e abra um Pull Request direcionado à main.
6. Confira o workflow CI, responda às observações de revisão e aguarde os checks exigidos.
7. Integre a mudança somente quando os critérios de proteção do repositório forem atendidos.

## 5. Itens que não devem ser versionados
O banco local data/*.db, as exportações exports/*.csv e exports/*.png, ambientes virtuais, caches, arquivos de cobertura e segredos são ignorados pelo .gitignore. Não remova essas proteções sem justificativa registrada.

## 6. Comunicação e revisão
O projeto está sendo mantido individualmente. Até que um par de revisão seja formalmente definido, não existe canal coletivo nem prazo acordado para resposta a Pull Requests. Quando houver um colaborador, o canal e a janela de resposta deverão ser combinados e registrados neste guia.

## 7. Documentação principal
Consulte [PLANO_GCS.md](PLANO_GCS.md) para as políticas de configuração, identificação dos itens, branching, mudanças, baselines, CI/CD e auditoria.
