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
A estrutura organizada terá .github/ (workflows, templates e Dependabot), app/ (cli, database, models, services, utils), data/ (dados locais ignorados), docs/ (PGC e onboarding), exports/ (arquivos gerados ignorados), tests/, .gitignore, README.md, requirements.txt e run.py.

## 5. Integração Contínua (CI)

O workflow CI será mantido em .github/workflows/ci.yml e executará verificações em Pull Requests direcionados à main e em atualizações da branch principal. O pipeline também é um item de configuração versionado.

### 5.1 Etapas do pipeline de CI
1. Fazer checkout do repositório.
2. Configurar Python 3.12 no runner.
3. Atualizar pip e instalar as dependências declaradas em requirements.txt.
4. Verificar sintaxe com python -m compileall -q app run.py.
5. Executar a suíte com python -m pytest -q.
6. Publicar o resultado do job como status check para uso na regra de proteção da main.

### 5.2 Política de Pull Request e revisão
Toda mudança destinada à main deve partir de uma branch e ser submetida por Pull Request. O PR deve explicar objetivo, impacto, itens de configuração alterados e testes executados. O CI precisa concluir com sucesso antes do merge. A política final deve exigir pelo menos uma aprovação de colaborador com permissão de escrita; essa aprovação fica pendente até a inclusão de um par real.

### 5.3 Critérios de qualidade (Quality Gate)
- O workflow deve concluir sem falhas.
- compileall deve concluir sem erro.
- Todos os testes pytest devem passar.
- Banco local, exportações, ambientes virtuais, caches e segredos não devem ser adicionados ao Git.
- Alterações funcionais relevantes devem incluir ou atualizar testes quando aplicável.

## 6. Entrega e implantação contínua (CD)

A aplicação atual não está hospedada como serviço. Portanto, CD é tratado como preparação e publicação de uma versão identificável no GitHub, não como deploy de uma aplicação online.

### 6.1 Etapas de entrega
1. Confirmar CI aprovado para o commit candidato.
2. Executar validação funcional local (python run.py) e conferir os testes.
3. Criar tag SemVer no commit validado.
4. Publicar GitHub Release com resumo das mudanças.
5. Executar manualmente environment-gates.yml para demonstrar a validação em staging e a aprovação obrigatória em production; esse workflow não realiza deploy.
6. Usar staging como etapa de validação e production como gate de aprovação da liberação.
7. Caso o projeto passe a ser hospedado, atualizar este PGC antes de definir deploy, smoke tests e rollback de infraestrutura.

### 6.2 Estratégias de implantação
Rolling update, Blue-Green e Canary Release não se aplicam à versão local atual. Feature flags também não são necessárias no estágio atual. A estratégia vigente é publicação de releases versionadas no GitHub.

### 6.3 Rollback e recuperação
A recuperação consiste em identificar a última tag ou commit estável e retornar o código para essa referência. Como o banco SQLite e os exports são dados locais ignorados pelo Git, a restauração desses dados requer backup local. Uma futura hospedagem exigirá procedimento próprio de backup e rollback.

## 7. Infraestrutura como Código (IaC)

IaC não é aplicável atualmente porque o sistema executa localmente e não provisiona servidores, redes, containers ou serviços externos. Os arquivos de configuração do repositório e workflows permanecem versionados. Caso seja adotada hospedagem, a infraestrutura e suas configurações deverão ser incorporadas ao PGC e versionadas.

### 7.1 Versionamento de infraestrutura
Não há código IaC nem arquivo de estado no projeto. Mudanças futuras em infraestrutura seguirão branches, Pull Requests, revisão e validações.

### 7.2 Ambientes efêmeros
Review Apps e ambientes efêmeros não se aplicam à aplicação de terminal atual. Os GitHub Environments staging e production funcionam como controles de etapa/aprovação, sem provisionamento de servidores.

## 8. Controle de configuração e mudança

### 8.1 Processo de solicitação de mudança
Fluxo padrão: registrar Issue (quando pertinente) → fazer check-out da main atualizada → criar branch → alterar e testar → fazer commits/check-in → abrir Pull Request → executar CI e revisão → integrar por merge → criar tag/release quando aplicável. Issue e PR mantêm rastreabilidade. Correções urgentes também devem ser registradas.

### 8.2 Comitê de Controle de Mudanças (CCM)
Como o projeto é individual, não existe CCM formal. Cristiano avalia mudanças de alto impacto, especialmente alterações na persistência SQLite, no formato dos dados, nas dependências ou no processo de release. Quando um par de revisão for designado, ele participará da revisão dos PRs. Decisões e justificativas devem permanecer registradas na Issue ou no PR.

## 9. Baselines e Releases

### 9.1 Geração de baseline
Uma baseline corresponde a um commit estável na main, após CI aprovado e revisão prevista pela política. A release formal deve ser identificada por tag SemVer vinculada ao commit exato. A primeira baseline formal será marcada quando houver uma versão avaliada e liberada.

### 9.2 Notas de versão
Cada GitHub Release deverá apresentar versão, data, resumo das funcionalidades, correções, alterações relevantes e limitações conhecidas. O histórico de commits Conventional Commits e os PRs servem como fonte para as notas.

## 10. Estimativa do status de configuração

### 10.1 Monitoramento e auditoria
O status da configuração será acompanhado pelo histórico de commits, branches, Issues, Pull Requests, resultados de Actions, tags e Releases. Não há serviço de produção hospedado para monitorar disponibilidade ou logs em execução. A auditoria verifica se os artefatos estão versionados, se os arquivos locais estão ignorados e se as regras de repositório estão ativas.

### 10.2 Métricas DORA

| Métrica | Aplicação no projeto |
|---|---|
| Deployment Frequency | Frequência de releases GitHub; não representa deploy de serviço online. |
| Lead Time for Changes | Tempo entre abertura/primeiro commit e merge ou release, obtido pelo histórico. |
| Change Failure Rate | Percentual de releases que exigem correção posterior; será mensurável com histórico suficiente. |
| Mean Time to Restore (MTTR) | Tempo para retornar a uma versão estável via commit/tag; não há serviço online para medir indisponibilidade. |

As métricas serão acompanhadas de forma qualitativa enquanto o projeto não possuir volume de releases suficiente para indicadores estatísticos úteis.

### 10.3 Relatórios e auditorias
O histórico do GitHub e os registros do GitHub Actions são a evidência principal. A cada entrega avaliativa, verificar estrutura do repositório, presença do PGC, proteção da main, resultado do CI, ambientes, revisor obrigatório e permissões do colaborador/par.

## 11. Marcos de GCS

1. Repositório individual criado e estrutura inicial organizada — concluído.
2. PGC inicial elaborado — concluído em 21/09/2026.
3. Revisão do PGC conforme aulas e material OngConecta — em execução nesta versão 1.1.
4. Workflows CI e environment-gates versionados — a concluir na publicação desta revisão.
5. Proteção clássica da main com PR obrigatório, status check e sem bypass — pendente de configuração nas Settings do GitHub.
6. Criação dos GitHub Environments staging e production — pendente de configuração nas Settings do GitHub.
7. Definição do par, permissão Write e aprovação mínima no PR — pendente, por ausência de colega definido.
8. Evidência de recusa de push direto na main — pendente de teste após ativação da proteção.
9. Primeira release formal com tag SemVer — marco futuro.

## 12. Treinamento e recursos

Os recursos necessários são Git, GitHub, GitHub Actions, Python 3, SQLite, pytest e matplotlib. O responsável deve conhecer operações de check-out/check-in, branches, merge, tags, Issues, Pull Requests, leitura do resultado de CI e recuperação por commit/tag. O guia docs/ONBOARDING.md documenta os passos para configurar e executar o projeto.

O canal de comunicação e a janela de resposta a PRs ainda não foram definidos porque o projeto está sendo desenvolvido individualmente. Caso um colaborador seja adicionado, README/guia deverá registrar o canal acordado e o prazo de resposta combinado, sem presumir um acordo inexistente.

## 13. Controle de software de subcontratados, fornecedores e dependências de terceiros

Não há software desenvolvido por subcontratados ou fornecedores incorporado ao projeto. As dependências externas atuais são matplotlib e pytest, declaradas em requirements.txt. A biblioteca padrão do Python não requer instalação externa. Atualizações devem ser controladas, registradas em branch e validadas no CI. O Dependabot acompanhará atualizações de dependências Python e GitHub Actions. Nenhuma credencial ou segredo deve ser armazenado no repositório.

## 14. Quadro-resumo do pipeline CI/CD

| Etapa | Descrição | Gatilho |
|---|---|---|
| Check-out / branch | Atualizar main e criar branch feature/fix. | Início de uma mudança. |
| CI | Configurar Python, instalar dependências, verificar sintaxe e executar pytest. | Push e Pull Request. |
| Revisão | Conferir diff, objetivo, impactos, ICs e evidências de teste. | Pull Request aberto/atualizado. |
| Merge | Integrar na main após CI verde e aprovação exigida pela regra. | PR aprovado e checks concluídos. |
| Staging | Etapa de homologação/validação controlada no GitHub; verificação manual pelo environment-gates.yml, sem servidor. | Após CI e merge, conforme fluxo de release. |
| Gate de production | Aprovação obrigatória de Cristiano Castanheira no GitHub Environment production. | Preparação de release/liberação. |
| Release / baseline | Criar tag SemVer e publicar notas no GitHub. | Validação concluída e gate aprovado. |

---

**Nota de estado:** este PGC distingue recursos existentes de configurações pendentes no GitHub. As regras de proteção da branch, os GitHub Environments e o par de revisão só devem ser marcados como concluídos depois da configuração e da verificação efetiva nas Settings do repositório. O projeto atual é local e não possui aplicação hospedada.
