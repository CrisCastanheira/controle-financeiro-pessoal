# Adendo ao Plano de GCS — Execução individual

**Projeto:** Controle Financeiro Pessoal (CFP)  
**Responsável:** Cristiano Castanheira  
**Data:** 16/11/2026  
**Repositório:** https://github.com/CrisCastanheira/controle-financeiro-pessoal

## 1. Preservação do plano original

Este adendo complementa o Plano de Gerenciamento de Configuração original (Versão 1.0), sem substituir seu conteúdo. O plano original foi mantido e este registro acrescenta a execução prática realizada no GitHub em 16/11/2026.

## 2. Condição de execução

O projeto e a atividade foram realizados individualmente, sem par de revisão. Não houve revisão independente por outro integrante e a autoavaliação não é apresentada como revisão por pares.

Para manter rastreabilidade e controle de qualidade, foram utilizados Pull Requests, validação automatizada por GitHub Actions, checklist individual antes da integração e aprovação obrigatória do ambiente `production` pelo responsável do projeto. Esses controles documentam o processo individual, mas não equivalem à aprovação independente de um colega.

## 3. Implementações verificadas

| Elemento | Estado |
|---|---|
| Branch principal | `main` |
| Proteção da `main` | Regra clássica criada; exige Pull Request e status check `tests`; bloqueia bypass; force push e exclusão desativados. |
| Aprovação de PR por colega | Não configurada, pois o trabalho foi realizado individualmente e não houve par de revisão. |
| Environment `staging` | Criado; job de validação concluído com sucesso. |
| Environment `production` | Criado com `CrisCastanheira` como revisor obrigatório; self-review permitido; bypass de administradores desativado; deployments restritos à `main`. |
| CI | GitHub Actions executa instalação de dependências, verificação de sintaxe e pytest; job `tests` aprovado. |
| Workflow de ambientes | Executa o gate de staging, solicita aprovação em production e termina após aprovação. Não realiza deploy da aplicação. |

## 4. Evidência do bloqueio de push direto

O teste foi feito em uma cópia temporária clonada do repositório. Nela foi criado `TESTE_BLOQUEIO_PUSH.txt` e o commit local `58df6fe`, somente para a tentativa de push direto na branch `main`.

Comando executado:

```powershell
git push origin main
```

Resposta do GitHub:

```text
remote: error: GH006: Protected branch update failed for refs/heads/main.
remote:
remote: - Changes must be made through a pull request.
remote:
remote: - Required status check "tests" is expected.
! [remote rejected] main -> main (protected branch hook declined)
error: failed to push some refs to 'https://github.com/CrisCastanheira/controle-financeiro-pessoal.git'
```

O arquivo de teste ficou apenas na cópia temporária local e não foi publicado no repositório remoto. A evidência textual completa está em [PUSH_DIRETO_RECUSADO.md](evidencias/PUSH_DIRETO_RECUSADO.md).

## 5. Validação de staging e production

O workflow manual [Environment Gates](../.github/workflows/environment-gates.yml) foi executado na branch `main`. O job `Validate staging environment` concluiu com sucesso; o job `Await production approval` aguardou a aprovação de `CrisCastanheira`; após a aprovação, o workflow terminou com resultado `Success`.

Os GitHub Environments são gates de controle e aprovação. O CFP é uma aplicação de terminal local em Python/SQLite; não há servidor nem implantação real em staging ou production.

## 6. Fluxo individual aplicado

1. Identificar a alteração e os itens de configuração afetados.
2. Criar uma branch curta a partir da `main`.
3. Implementar a mudança e executar os testes.
4. Fazer autoavaliação do diff, dos arquivos afetados e dos riscos.
5. Abrir Pull Request e conferir o status check `tests`.
6. Integrar somente após os checks obrigatórios concluírem com sucesso.
7. Registrar versões, decisões e evidências no GitHub.

## 7. Rastreabilidade

- [Repositório](https://github.com/CrisCastanheira/controle-financeiro-pessoal)
- [Plano GCS publicado](https://github.com/CrisCastanheira/controle-financeiro-pessoal/blob/main/docs/PLANO_GCS.md)
- [Guia de onboarding](https://github.com/CrisCastanheira/controle-financeiro-pessoal/blob/main/docs/ONBOARDING.md)
- [Evidência do push recusado](https://github.com/CrisCastanheira/controle-financeiro-pessoal/blob/main/docs/evidencias/PUSH_DIRETO_RECUSADO.md)
- [Pull Request #1](https://github.com/CrisCastanheira/controle-financeiro-pessoal/pull/1)
- [Pull Request #4](https://github.com/CrisCastanheira/controle-financeiro-pessoal/pull/4)
- [CI aprovado na main](https://github.com/CrisCastanheira/controle-financeiro-pessoal/actions/runs/43950121700)
- [Environment Gates aprovado](https://github.com/CrisCastanheira/controle-financeiro-pessoal/actions/runs/43947102802)

## 8. Situação dos requisitos

| Requisito | Situação em 16/11/2026 |
|---|---|
| Repositório organizado e acessível | Concluído |
| Plano GCS publicado | Concluído |
| Recusa de push direto na `main` | Comprovada por GH006 |
| Environment `staging` | Configurado e testado |
| Environment `production` com Cristiano como revisor obrigatório | Configurado e testado |
| Par de revisão com acesso Write | Não realizado — atividade desenvolvida individualmente, sem par de revisão |

**Nota:** a ausência de par de revisão permanece registrada de forma explícita e não é apresentada como requisito cumprido.
