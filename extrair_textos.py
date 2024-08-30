import os
     
def extrair_descricao_cursos(diretorio: str) -> dict:
    dic = {}
    secoes = ['Titulo', 'Descricao', 'Detalhes']

    for nome_arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        with open(caminho_arquivo, 'r') as conteudo:
            titulo = ""
            for linha in conteudo:
                for secao in secoes:
                    if linha.startswith(secao):
                        valor = linha.removeprefix(f'{secao}: ').strip()
                        if secao == 'Titulo':
                            titulo = valor
                            dic[titulo] = {}
                        else:
                            dic[titulo][secao.lower()] = valor
    return dic