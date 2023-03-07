import sys
import json

dicionario = ['d', 'e', 'h', 'i', 'j', 'l', 'o', 'w', '<', '=',
              '+', ';', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
reservadas = ['while', 'do']
operadores = ['<', '=', '+']
terminadores = [';']
identificadores = ['i', 'j']
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

tokens = []
simbolos = []


def verificaToken(token: str, inicio):
    eh_numero = True
    for i in token:
        if not i in numeros:
            eh_numero = False
    
    
    if not token == '':
        if eh_numero:
            if not token in simbolos:
                simbolos.append(token)
            tokens.append(
                [token, ['constante', simbolos.index(token) + 1], len(token), inicio])
        elif token in reservadas:
            tokens.append([token, 'palavra reservada', len(token), inicio])
        elif token in operadores:
            tokens.append([token, 'operador', len(token), inicio])
        elif token in terminadores:
            tokens.append([token, 'terminador', len(token), inicio])
        elif token in identificadores:
            if not token in simbolos:
                simbolos.append(token)
            tokens.append(
                [token, ['identificador', simbolos.index(token) + 1], len(token), inicio])
        else:
            print(
                f'Simbolo "{token}" não reconhecido. Linha {inicio[0]}, Coluna {inicio[1]}')
            return False
    return True

def tokensParaJson():
    listJson = []
    for token in tokens:
        listJson.append({"token": token[0], "identificacao": token[1], "tamanho": token[2], "posicao": token[3]})

    return listJson


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python analisador_lexico.py <input_file>")
        sys.exit(1)

    file = sys.argv[1]

    with open(file, 'r') as f:
        code = f.read().split('\n')

    coluna = 0
    token = ''
    stop = False

    for linha in range(len(code)):
        if stop:
            break
        for coluna in range(len(code[linha])):
            if code[linha][coluna] != ' ' and not code[linha][coluna] in dicionario:
                '''
                Verifica se o caractere não é espaço vazio e se está presente no dicionário
                '''

                print(
                    f"'{code[linha][coluna]}' não está presente no dicionário. Ln {linha}, Col {coluna}")
                stop = True
                break

            elif code[linha][coluna] in terminadores:
                '''
                Verifica se o caractere é um terminador
                '''

                stop = not verificaToken(token, (linha, coluna-len(token)))
                stop = not verificaToken(code[linha][coluna], (linha, coluna))
                token = ''

            elif code[linha][coluna] != ' ':
                token += code[linha][coluna]

            else:
                stop = not verificaToken(token, (linha, coluna-len(token)))
                token = ''

    if not stop:
        tokensJson = tokensParaJson()

        jsonFinal = {"tokens": tokensJson, "simbolos": simbolos}
        with open('tabelas.json', 'w', encoding='utf-8') as f:
            json.dump(jsonFinal, f, ensure_ascii=False, indent=2)