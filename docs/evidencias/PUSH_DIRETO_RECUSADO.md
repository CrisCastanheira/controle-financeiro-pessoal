# Evidência — Recusa de push direto na branch main

**Repositório:** CrisCastanheira/controle-financeiro-pessoal
**Data do teste:** 16/11/2026
**Branch de destino:** main
**Commit local de teste:** 58df6fe
**Arquivo temporário:** TESTE_BLOQUEIO_PUSH.txt (criado apenas na cópia temporária local; não foi publicado no repositório)

## Procedimento

1. Foi clonada uma cópia temporária do repositório.
2. Foi criado um arquivo de teste e um commit local na branch main.
3. Foi executado `git push origin main`, sem a opção `--force`.

## Resultado observado

```text
remote: error: GH006: Protected branch update failed for refs/heads/main.
remote:
remote: - Changes must be made through a pull request.
remote:
remote: - Required status check "tests" is expected.
To https://github.com/CrisCastanheira/controle-financeiro-pessoal.git
 ! [remote rejected] main -> main (protected branch hook declined)
error: failed to push some refs to 'https://github.com/CrisCastanheira/controle-financeiro-pessoal.git'
```

## Conclusão

O teste comprova que a regra de proteção da branch main está ativa: atualizações diretas foram recusadas, a integração deve ocorrer por Pull Request e o status check `tests` é exigido. O arquivo `TESTE_BLOQUEIO_PUSH.txt` permaneceu somente na cópia temporária local.

**Observação:** este registro textual documenta a saída reproduzida no terminal. Para a entrega da atividade, recomenda-se anexar também uma captura de tela do PowerShell mostrando o comando e a mensagem de recusa.