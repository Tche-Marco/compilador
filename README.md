<h1>Analisador léxico</h1>

> Status: Em desenvolvimento

### Esse projeto foi criado como resposta à uma atividade da matéria de Compiladores, com o intuito de fazer um analisador léxico que gere a tabela de tokens e a de símbolos para a entrada analisada, com base nas especificações da linguagem abaixo.

## Características dessa linguagem de programação:

+ palavras reservadas: while, do
+ operadores: <, =, +
+ terminador:  ;
+ identificadores: i, j
+ constantes: sequência de números
+ números: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
  
## Como rodar o analisador:

Abra o console na pasta onde encontram-se os arquivos 'main.py' e 'entrada.txt' e digite:
```console
  python main.py entrada.txt
```

Ao digitar esse comando, acontecerá a análise do código presente no arquivo 'entrada.txt' e caso algum erro seja encontrado, será apresentado no console qual token não foi identificado e sua posição (linha/coluna), caso nenhum erro sintático seja encontrado (com base na linguagem modelo da atividade) será criado um arquivo em Markdown chamado 'saida.md' apresentando a tabela de tokens e de símbolos referente à entrada.  
