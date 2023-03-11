<h1>Compilador</h1>

> Status: Em desenvolvimento

### Esse projeto está sendo desenvolvido na matéria de Compiladores, com o intuito de fazer um analisador léxico que gere a tabela de tokens e a de símbolos para a entrada analisada e um analisador sintático que utiliza dessas tabelas criadas pelo analisador léxico, com base nas especificações da linguagem abaixo.

## Características dessa linguagem de programação:

+ palavras reservadas: while, do
+ operadores: <, =, +
+ terminador:  ;
+ identificadores: i, j
+ constantes: sequência de números
+ números: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9


## Como rodar o analisador léxico:

Abra o console na pasta onde encontram-se os arquivos 'analisador_lexico.py' e 'entrada.txt' e digite:
```console
  python analisador_lexico.py entrada.txt
```

Ao digitar esse comando, acontecerá a análise do código presente no arquivo 'entrada.txt' e caso algum erro seja encontrado, será apresentado no console qual token não foi identificado e sua posição (linha/coluna), caso nenhum erro léxico seja encontrado (com base na linguagem modelo da atividade) será criado um arquivo em Json chamado 'tabelas.json' contendo a tabela de tokens e de símbolos referente à entrada. 

## Como rodar o analisador sintático:

Abra o console na pasta onde encontram-se os arquivos 'analizador_sintatico.py' e 'tabelas.json' e digite:
```console
  python analizador_sintatico.py 
```

Ao digitar esse comando, acontecerá a análise sintática das tabelas presentes no arquivo 'tabelas.json' e caso algum erro seja encontrado, será apresentado no console qual a posição do erro, qual o tipo esperado e qual o tipo encontrato, caso nenhum erro seja encontrado, aparecerá uma mensagem informando que a verificação foi finalizada com sucesso.