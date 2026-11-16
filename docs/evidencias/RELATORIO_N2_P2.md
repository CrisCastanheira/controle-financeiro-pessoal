# Índice de evidências — Avaliação N2-P2

**Projeto:** Controle Financeiro Pessoal  
**Data:** 16/11/2026  
**Repositório:** https://github.com/CrisCastanheira/controle-financeiro-pessoal

## 1. Proteção da branch main
A regra clássica para `main` exige Pull Request e status check `tests`, bloqueia bypass e mantém force push e exclusão desativados. A exigência de aprovação de colega não foi ativada porque a atividade foi realizada individualmente, sem par de revisão.

## 2. Teste de push direto recusado
Foi criado um commit temporário em uma cópia local e executado `git push origin main`. O GitHub respondeu com GH006 e recusou a atualização, indicando:
- `Changes must be made through a pull request.`
- `Required status check "tests" is expected.`

A transcrição completa está em [PUSH_DIRETO_RECUSADO.md](PUSH_DIRETO_RECUSADO.md). A captura de terminal está no arquivo PDF de evidências entregue junto com o plano.

## 3. Ambientes
- `staging`: job de validação executado com sucesso.
- `production`: CrisCastanheira configurado como revisor obrigatório; após sua aprovação, o workflow concluiu com Success.
- Os environments funcionam como gates; o aplicativo local não foi implantado em servidor.

## 4. Pull Requests e execuções
- [PR #1 — documentação GCS e automações](https://github.com/CrisCastanheira/controle-financeiro-pessoal/pull/1)
- [PR #4 — atualização do PGC e registro GH006](https://github.com/CrisCastanheira/controle-financeiro-pessoal/pull/4)
- [CI na main após PR #4 — sucesso](https://github.com/CrisCastanheira/controle-financeiro-pessoal/actions/runs/43950121700)
- [Environment Gates — sucesso após aprovação](https://github.com/CrisCastanheira/controle-financeiro-pessoal/actions/runs/43947102802)

## 5. Capturas incluídas no Dossiê PDF
1. Configuração da regra de proteção da `main`.
2. Status check `tests` e bloqueio de bypass.
3. Confirmação de criação da regra.
4. Configuração do ambiente `staging`.
5. Ambiente `production` salvo com CrisCastanheira e branch `main`.
6. Execução aguardando aprovação em production, após staging.
7. Execução concluída com Success após a aprovação.
8. Terminal com `git push origin main` e resposta GH006.

## 6. Condição individual
A atividade foi realizada individualmente, sem par de revisão. Não houve colega adicionado com permissão Write nem revisão independente. O processo individual foi documentado sem simular uma revisão por pares.
