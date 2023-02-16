import sys

dic = ['d','e', 'h', 'i', 'j','l','o','w', '<' , '=', '+', ';', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
reservadas = ['while', 'do']
operadores = ['<', '=', '+']
terminadores = [';']
identificadores = ['i','j']
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

tokens = []
simbolos = []

def verificaToken(token, inicio):
    eNumero = True
    for i in token:
        if not i in numeros:
            eNumero = False

    if eNumero:
        if not token in simbolos:
            simbolos.append(token)
        tokens.append([token, ['constante', simbolos.index(token)], len(token), inicio])
    elif token in reservadas:
        tokens.append([token, 'palavra reservada', len(token), inicio])
    elif token in operadores:
        tokens.append([token, 'operador', len(token), inicio])
    elif token in terminadores:
        tokens.append([token, 'terminador', len(token), inicio])
    elif token in identificadores:
        if not token in simbolos:
            simbolos.append(token)
        tokens.append([token, ['identificador', simbolos.index(token)], len(token), inicio])
    else:
        print(f'Simbolo "{token}" não reconhecido. Ln {inicio[0]}, Col {inicio[1]}')
        return False
    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python comp.py <input_file>")
        sys.exit(1)

    file = sys.argv[1]

    with open(file, 'r') as f:
        code = f.read().split('\n')

    col = 0
    token = ''
    stop = False

    for ln in range(len(code)):
        if stop:
            break
        for col in range(len(code[ln])):
            if code[ln][col] != ' ' and not code[ln][col] in dic:
                '''
                Verifica se o caractere não é espaço vazio e se está presente no dicionário
                '''

                print(f"'{code[ln][col]}' não está presente no dicionário. Ln {ln}, Col {col}")
                stop = True
                break

            elif code[ln][col] in terminadores:
                '''
                Verifica se o caractere é um terminador
                '''

                stop = not verificaToken(token, (ln, col-len(token)))
                stop = not verificaToken(code[ln][col], (ln, col))
                token = ''

            elif code[ln][col] != ' ':
                token += code[ln][col]

            else:
                stop = not verificaToken(token, (ln, col-len(token)))
                token = ''

    if not stop:
        with open('saida.md', 'w', encoding='utf-8') as saida:
            saida.write('# Tabela de Tokens\n')
            saida.write('| Token | Identificação | Tamanho | Posição |\n')
            saida.write('| :----: | :-----------: | :------: | :------: |\n')

            for token in tokens:
                saida.write(f'| {token[0]} | {token[1]} | {token[2]} | {token[3]} |\n')

            saida.write('\n<br/>\n\n')

            saida.write('# Tabela de Tokens\n')
            saida.write('\n| Índice | Símbolo |\n')
            saida.write('| :----: | :-----------: |\n')

            for simbolo in simbolos:
                saida.write(f'| {(simbolos.index(simbolo)+1)} | {simbolo} |\n')
