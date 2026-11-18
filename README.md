# Teste de Situação do Aluno

## Descrição
Projeto desenvolvido para a disciplina de Testes, com o objetivo de implementar uma suíte de testes automatizados para verificar a situação final de um aluno, considerando sua média e frequência.

## Tecnologias utilizadas
- Python
- Biblioteca unittest

## Arquivos do projeto
- `situacao.py`: função responsável por determinar a situação final do aluno.
- `test_situacao.py`: testes automatizados para verificar os resultados da função e o tratamento de entradas inválidas.

## Regras de negócio
- Média abaixo de 4,0: REPROVADO.
- Média entre 4,0 e 6,9: RECUPERACAO.
- Média igual ou superior a 7,0: APROVADO.
- Frequência inferior a 75%: REPROVADO_POR_FALTA.
- Valores fora dos limites permitidos geram erro ValueError.

## Como executar os testes

Com os dois arquivos na mesma pasta, execute no terminal:

```bash
python -m unittest test_situacao.py -v
```

## Resultado esperado
Todos os testes devem ser executados com sucesso, validando os casos de aprovação, recuperação, reprovação, reprovação por falta e entradas inválidas.

## Disciplina
Testes de Software
