import re

def contar_palavras(texto):
    palavras = re.findall(r'\b\w+\b', texto.lower())
    
    contagem_palavras = {}
    
    for palavra in palavras:
        if palavra in contagem_palavras:
            contagem_palavras[palavra] += 1
        else:
            contagem_palavras[palavra] = 1
    
    return contagem_palavras

if __name__ == "__main__":
    texto = input("Digite o texto: ")
    resultado = contar_palavras(texto)
    for palavra, contagem in sorted(resultado.items()):
        print(f'{palavra}: {contagem}')
