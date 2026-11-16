# Plano de Gerenciamento de Configuração de Software (PGC)

**Projeto:** CFP — Controle Financeiro Pessoal  
**Responsável pelo projeto e pela GCS:** Cristiano Castanheira  
**Repositório:** https://github.com/CrisCastanheira/controle-financeiro-pessoal  
**Versão:** 1.1 — revisão para execução da N2-P2  
**Data:** 16/11/2026  
**Abordagem:** GCS com práticas DevOps proporcionais ao projeto individual

## Histórico de revisões

| Data | Versão | Descrição | Autor |
|---|---:|---|---|
| 21/09/2026 | 1.0 | Elaboração inicial do PGC do Controle Financeiro Pessoal. | Cristiano Castanheira |
| 16/11/2026 | 1.1 | Revisão conforme as aulas, o template e o Plano GCS do OngConecta; inclusão do fluxo prático de GitHub e CI. | Cristiano Castanheira |

## 1. Introdução

### 1.1 Finalidade
Este Plano de Gerenciamento de Configuração (PGC) estabelece como os artefatos do Controle Financeiro Pessoal serão identificados, versionados, alterados, integrados, validados, liberados e auditados. Busca preservar a integridade dos itens de configuração, manter a rastreabilidade das mudanças e permitir recuperar versões conhecidas do projeto.

O plano aplica os quatro pilares trabalhados na disciplina: identificação da configuração, controle de versão, controle de mudanças e auditoria/status da configuração. As práticas DevOps e CI/CD são dimensionadas para a realidade do projeto, sem declarar infraestrutura ou implantação que não existe.

### 1.2 Escopo
O projeto é uma aplicação de terminal em Python 3, com persistência local em SQLite, testes automatizados com pytest e gráficos com matplotlib. O escopo abrange código-fonte, testes, dependências, documentação, arquivos de configuração do GitHub e artefatos de versão. O banco local e os arquivos gerados pelo uso da aplicação não são versionados.

O desenvolvimento é individual, sob responsabilidade de Cristiano Castanheira. O par de revisão será cadastrado quando houver um colega definido; até essa definição, a revisão por pares permanece pendente e não será declarada como realizada.

### 1.3 Definições, acrônimos e abreviações

| Termo | Significado |
|---|---|
| GCS / PGC | Gestão de Configuração de Software / Plano de Gerenciamento de Configuração. |
| IC | Item de Configuração: artefato identificado e controlado formalmente. |
| Baseline | Configuração revisada e aceita, usada como referência estável para mudanças posteriores. |
| Check-out / Check-in | Obtenção da versão do repositório para trabalho local / registro de alteração com versão, autor e comentário. |
| Branch / Merge | Linha alternativa de desenvolvimento / integração das alterações. |
| Build / Release | Versão integrada e validável / versão identificada e disponibilizada. |
| CI / CD | Integração Contínua / Entrega ou Implantação Contínua. |
| SemVer | Versionamento Semântico: MAJOR.MINOR.PATCH. |
| CCM | Comitê de Controle de Mudanças. Neste projeto individual, a decisão fica com o responsável. |

### 1.4 Referências
- Aulas 01, 02, 03, 04, 05, 06, 09 e 10 da disciplina, conforme os arquivos disponibilizados.
- Template “Plano de Gerenciamento de Configuração — Enfoque DevOps”.
- “Plano de Gerenciamento de Configuração — ONGConecta”, usado como referência para o processo e o fluxo CI/CD.
- Repositório, README.md, requirements.txt, .gitignore e testes do próprio projeto.

### 1.5 Visão geral
A aplicação organiza o código em módulos dentro de app/, mantém testes em tests/, declara dependências em requirements.txt e utiliza GitHub como repositório central. A branch main é a linha principal. Mudanças devem ser desenvolvidas em branches curtas, submetidas por Pull Request e verificadas pelo pipeline de CI antes da integração, conforme as regras de proteção a serem ativadas no GitHub.

## 2. Cultura DevOps e papéis na Gerência de Configuração

Como a execução é individual, Cristiano Castanheira acumula os papéis. O acúmulo de funções não elimina a necessidade de registrar decisões e evidências.

| Papel | Responsável e atribuições |
|---|---|
| Gerente de Projeto / Product Owner | Cristiano: define escopo, prioriza melhorias e decide mudanças de maior impacto. |
| Responsável de GCS / Release Engineer | Cristiano: administra GitHub, branches, versões, tags, documentação e releases. |
| Desenvolvedor | Cristiano: implementa funcionalidades, correções e documentação. |
| QA / Automação | Cristiano: mantém e executa pytest; GitHub Actions automatiza as verificações. |
| Segurança / DevSecOps | Cristiano: mantém segredos fora do repositório, revisa dependências e o .gitignore. |
| Operações / SRE | Não há serviço hospedado; verificações são locais e por commit/tag. |
| Par de revisão | A definir. O colega deverá receber permissão Write; requisito pendente. |
| CCM | Não há comitê formal; Cristiano avalia mudanças de alto impacto e registra decisões. |

## 3. Ferramentas, ambientes e infraestrutura

### 3.1 Ferramentas do projeto e do pipeline

| Categoria | Ferramenta | Finalidade / situação |
|---|---|---|
| Controle de versão | Git e GitHub | Código, documentação, branches, PRs e releases. |
| CI | GitHub Actions | Workflow CI para sintaxe/testes e workflow manual para demonstrar os gates staging/production. |
| Linguagem | Python 3 | Execução da aplicação; CI definido com Python 3.12. |
| Persistência | SQLite | Banco local; não versionado. |
| Testes | pytest | Testes automatizados; 13 aprovados na validação de 16/11/2026. |
| Gráficos | matplotlib | Geração local de gráficos. |
| Dependências | requirements.txt e Dependabot | Declaração e acompanhamento das dependências Python e GitHub Actions. |
| Empacotamento / containers | Não utilizado | Projeto local; Docker e registro de imagens não se aplicam atualmente. |
| IaC / observabilidade | Não aplicável | Sem servidores ou serviços hospedados. |

### 3.2 Ambientes e infraestrutura
Os ambientes staging e production desta atividade são GitHub Environments para controle de etapas e aprovação, não ambientes de hospedagem da aplicação. O projeto continua sendo executado localmente; a existência desses ambientes no GitHub não significa que exista deploy de uma aplicação web.

| Ambiente | Finalidade | Gatilho / controle |
|---|---|---|
| Desenvolvimento | Execução local com Python, ambiente virtual e SQLite. | Alterações feitas em cópia local após check-out. |
| Staging | Etapa de homologação/validação registrada no GitHub. | Job de validação após CI aprovado; não há servidor de staging. |
| Production | Gate de aprovação para liberação. | Deve exigir Cristiano Castanheira (CrisCastanheira) como revisor obrigatório no GitHub Environment. Não há servidor de produção ou deploy real. |

O workflow manual environment-gates.yml executa uma verificação demonstrativa em staging e, depois, solicita a aprovação de production; ele não realiza deploy nem altera dados da aplicação.

Não são utilizados DNS, IP público, load balancer, containers ou credenciais de infraestrutura. Segredos futuros deverão ficar em GitHub Secrets/Environment Secrets, nunca no código ou em arquivos versionados.

### 3.3 Estratégia de branching e versionamento
- main: branch principal, protegida contra alterações diretas; mudanças chegam por Pull Request.
- feature/<descricao-curta>: novas funcionalidades, por exemplo feature/relatorio-mensal.
- fix/<descricao-curta>: correções comuns, por exemplo fix/validacao-data.
- hotfix/<descricao-curta>: correção urgente, também registrada e integrada por PR.
- release/vX.Y.Z: opcional, para preparação de versão formal.

Os commits seguem Conventional Commits: feat, fix, test, docs, refactor e chore, preferencialmente com escopo quando útil. Releases usam SemVer, por exemplo v1.0.0. A proteção clássica da branch main deverá exigir Pull Request, status checks aprovados e, após a definição do par, pelo menos uma aprovação. O bypass deverá permanecer desabilitado.

## 4. Identificação da configuração

### 4.1 Itens de configuração

| Item | Localização / política |
|---|---|
| Código-fonte | app/ e run.py; versionados no Git. |
| Testes | tests/; versionados e executados no CI. |
| Dependências | requirements.txt; versionado e revisado quando atualizado. |
| Configuração GitHub | .gitignore, .github/workflows/, templates de Issues/PR e dependabot.yml; versionados. |
| Documentação | README.md e docs/, incluindo este PGC; versionados. |
| Dados locais | data/*.db; ignorados pelo Git. |
| Exportações | exports/*.csv e exports/*.png; ignoradas pelo Git. |
| Ambientes e caches | .venv/, venv/, __pycache__/, .pytest_cache/, cobertura e arquivos de IDE; ignorados. |

### 4.2 Convenção de nomenclatura

| Artefato | Convenção | Exemplo |
|---|---|---|
| Branch | feature/<descricao>, fix/<descricao> ou hotfix/<descricao> | feature/relatorio-mensal |
| Commit | Conventional Commits | feat(report): adiciona resumo mensal |
| Tag | SemVer com prefixo v | v1.0.0 |
| Issue | Título objetivo | Solicitação: adicionar filtro mensal |
| Pull Request | Objetivo da mudança | Adiciona filtro por mês |

### 4.3 Estrutura do repositório

```text
controle-financeiro-pessoal/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── change_request.md
│   ├── pull_request_template.md
│   ├── dependabot.yml
│   └── workflows/
│       ├── ci.yml
│       └── environment-gates.yml
├── app/
│   ├── cli/
│   ├── database/
│   ├── models/
│   ├── services/
│   └── utils/
├── data/                  # dados locais; banco ignorado
├── docs/
│   ├── ONBOARDING.md
│   └── PLANO_GCS.md
├── exports/               # arquivos gerados; ignorados
├── tests/
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

## 5. Integração Contínua (CI)

O workflow CI é mantido em .github/workflows/ci.yml e executa verificações em Pull Requests direcionados à main e em atualizações da branch principal. O pipeline também é um item de configuração versionado.

### 5.1 Etapas do pipeline de CI
1. Fazer checkout do repositório.
2. Configurar Python 3.12 no runner.
3. Atualizar pip e instalar requirements.txt.
4. Verificar sintaxe com python -m compileall -q app run.py.
5. Executar pytest -q.
6. Publicar o resultado do job como status check para a regra de proteção da main.

### 5.2 Política de Pull Request e revisão
Toda mudança destinada à main deve partir de uma branch e ser submetida por Pull Request. O PR deve explicar objetivo, impacto, ICs alterados e testes. O CI precisa concluir com sucesso antes do merge. A política final deve exigir pelo menos uma aprovação de colaborador com permissão de escrita; essa aprovação fica pendente até a inclusão de um par real.

### 5.3 Critérios de qualidade
- Workflow sem falhas.
- compileall sem erros.
- Todos os testes pytest aprovados.
- Banco local, exports, ambientes virtuais, caches e segredos fora do Git.
- Alterações funcionais relevantes acompanhadas de testes quando aplicável.

## 6. Entrega e implantação contínua (CD)

A aplicação não está hospedada como serviço. CD é tratado como preparação e publicação de versão identificável no GitHub, não como deploy online.

### 6.1 Etapas de entrega
1. Confirmar CI aprovado para o commit candidato.
2. Executar validação funcional local (python run.py) e conferir testes.
3. Criar tag SemVer no commit validado.
4. Publicar GitHub Release com resumo das mudanças.
5. Executar manualmente environment-gates.yml para demonstrar a validação em staging e a aprovação obrigatória em production; esse workflow não realiza deploy.
6. Usar staging como etapa de validação e production como gate de aprovação.
7. Se houver hospedagem futura, atualizar este PGC antes de definir deploy, smoke tests e rollback.

### 6.2 Estratégias de implantação
Rolling update, Blue-Green e Canary não se aplicam à versão local. Feature flags também não são necessárias no estágio atual. A estratégia vigente é publicar releases versionadas no GitHub.

### 6.3 Rollback e recuperação
A recuperação consiste em identificar a última tag ou commit estável e retornar o código a essa referência. Banco SQLite e exports são dados locais ignorados pelo Git; restauração desses dados requer backup local. Uma futura hospedagem exigirá procedimento próprio.

## 7. Infraestrutura como Código (IaC)

IaC não é aplicável porque o sistema executa localmente e não provisiona servidores, redes, containers ou serviços externos. Arquivos de configuração do repositório e workflows permanecem versionados. Se houver hospedagem, infraestrutura e configurações serão incorporadas ao PGC e versionadas.

### 7.1 Versionamento de infraestrutura
Não há código IaC nem arquivo de estado no projeto. Mudanças futuras em infraestrutura seguirão branches, Pull Requests, revisão e validações.

### 7.2 Ambientes efêmeros
Review Apps e ambientes efêmeros não se aplicam à aplicação de terminal. Os GitHub Environments staging e production funcionam como controles de etapa/aprovação, sem provisionar servidores.

## 8. Controle de configuração e mudança

### 8.1 Processo de solicitação de mudança
Fluxo padrão: Issue (quando pertinente) → check-out da main atualizada → branch → alteração e testes → commits/check-in → Pull Request → CI e revisão → merge → tag/release quando aplicável. Issue e PR mantêm a rastreabilidade. Correções urgentes também devem ser registradas.

### 8.2 Comitê de Controle de Mudanças
Não há CCM formal. Cristiano avalia mudanças de alto impacto, em especial alterações de persistência SQLite, formato de dados, dependências ou release. Quando um par de revisão for designado, participará dos PRs. Decisão e justificativa ficam na Issue ou PR.

## 9. Baselines e Releases

### 9.1 Geração de baseline
Uma baseline corresponde a commit estável na main, após CI aprovado e revisão prevista na política. A release formal usa tag SemVer vinculada ao commit exato. A primeira baseline formal será marcada quando houver versão avaliada e liberada.

### 9.2 Notas de versão
Cada GitHub Release apresentará versão, data, resumo de funcionalidades, correções, alterações e limitações conhecidas. Commits e PRs são a fonte das notas.

## 10. Estimativa do status de configuração

### 10.1 Monitoramento e auditoria
O status é acompanhado por commits, branches, Issues, Pull Requests, resultados de Actions, tags e Releases. Não existe serviço hospedado para monitorar disponibilidade ou logs. A auditoria verifica artefatos versionados, arquivos locais ignorados e regras de repositório ativas.

### 10.2 Métricas DORA

| Métrica | Aplicação |
|---|---|
| Deployment Frequency | Frequência de releases GitHub; não é deploy de serviço online. |
| Lead Time for Changes | Tempo entre abertura/primeiro commit e merge ou release. |
| Change Failure Rate | Percentual de releases que exigem correção posterior, com histórico suficiente. |
| MTTR | Tempo para retornar a commit/tag estável; sem serviço online para medir indisponibilidade. |

### 10.3 Relatórios e auditorias
Histórico GitHub e GitHub Actions são as evidências principais. Em cada entrega, verificar estrutura, PGC, proteção da main, CI, environments, revisor obrigatório e permissões do colaborador/par.

## 11. Marcos de GCS

1. Repositório individual e estrutura inicial organizados — concluído.
2. PGC inicial elaborado em 21/09/2026 — concluído.
3. Revisão conforme aulas e OngConecta — versão 1.1.
4. Workflows CI e environment-gates versionados — incluídos nesta revisão; CI já executado com sucesso em commit da branch.
5. Proteção clássica da main com PR, status check tests e sem bypass — configurada e validada pelo teste de push direto em 16/11/2026. Exigência de aprovação de par permanece pendente até a inclusão de um colega real.
6. GitHub Environments staging e production — criados e configurados em 16/11/2026; production exige CrisCastanheira como revisor obrigatório e restringe deployments à branch main. Workflow manual de validação concluído com sucesso.
7. Par real com permissão Write e aprovação mínima no PR — pendente; colega ainda não definido.
8. Evidência de push direto recusado — concluída em 16/11/2026. A tentativa recebeu GH006, com a mensagem “Changes must be made through a pull request” e indicação de que o status check tests é esperado. O registro está em docs/evidencias/PUSH_DIRETO_RECUSADO.md.
9. Primeira release formal SemVer — futura.

## 12. Treinamento e recursos

Recursos necessários: Git, GitHub, GitHub Actions, Python 3, SQLite, pytest e matplotlib. O responsável deve conhecer check-out/check-in, branches, merge, tags, Issues, Pull Requests, leitura do CI e recuperação por commit/tag. O guia docs/ONBOARDING.md documenta configuração e execução.

Canal de comunicação e janela de resposta a PRs não foram definidos porque o projeto é individual. Se um colaborador for adicionado, README/guia deverá registrar o canal e o prazo acordados, sem presumir acordo inexistente.

## 13. Controle de software de subcontratados, fornecedores e dependências

Não há software de subcontratados ou fornecedores incorporado. As dependências externas atuais são matplotlib e pytest, declaradas em requirements.txt. Atualizações devem ser controladas em branch, registradas e validadas no CI. Dependabot acompanhará dependências Python e GitHub Actions. Segredos não devem ser armazenados no repositório.

## 14. Quadro-resumo do pipeline CI/CD

| Etapa | Descrição | Gatilho |
|---|---|---|
| Check-out / branch | Atualizar main e criar branch feature/fix. | Início de mudança. |
| CI | Configurar Python, instalar dependências, verificar sintaxe e executar pytest. | Push e Pull Request. |
| Revisão | Conferir diff, objetivo, impacto, ICs e testes. | PR aberto/atualizado. |
| Merge | Integrar após CI verde e aprovação exigida. | PR aprovado e checks concluídos. |
| Staging | Etapa de homologação/validação controlada no GitHub; verificação pelo environment-gates.yml, sem servidor. | Após CI e merge, conforme fluxo de release. |
| Gate production | Aprovação obrigatória de Cristiano no Environment production. | Preparação de liberação. |
| Release / baseline | Criar tag SemVer e publicar notas. | Validação e gate concluídos. |

**Nota de estado (16/11/2026):** a proteção da main foi configurada e testada; staging e production foram criados e o workflow de gate foi executado com sucesso. O requisito de par de revisão permanece pendente. O projeto atual é local e não possui aplicação hospedada; os GitHub Environments são gates de aprovação, não servidores de aplicação.
