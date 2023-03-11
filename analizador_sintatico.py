import json

def verifica_while(tokens, simbolos):
    valida_while = ['palavra reservada', 'identificador','operador','constante', 'palavra reservada', 'identificador','operador','identificador','operador','identificador',';']
    
    x = 10
    for i in range(x):
        if type(tokens[i]['identificacao']) == list:
            if tokens[i]['identificacao'][0] != valida_while[i]:
                raise SyntaxError("Arquivo 'entrada.py', posição {} tipo esperado: {}, tipo encontrado: {} SyntaxError: invalid syntax".format(tokens[i]["posicao"], valida_while[i], tokens[i]['identificacao'][0]))
        else:
            if tokens[i]['identificacao'] != valida_while[i]:
                raise SyntaxError("Arquivo 'entrada.py', posição {} tipo esperado: {}, tipo encontrado: {} SyntaxError: invalid syntax".format(tokens[i]["posicao"], valida_while[i], tokens[i]['identificacao']))
                

with open('tabelas.json', 'r') as tabelas:
    tabelas = json.load(tabelas)    
    tokens = tabelas["tokens"]
    simbolos = tabelas["simbolos"]

    verifica_while(tokens, simbolos)
    print('Verificação finalizada com sucesso :)')