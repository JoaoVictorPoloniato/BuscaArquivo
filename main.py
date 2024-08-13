import os
import shutil

def main(pasta_origem, pasta_destino):

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino) 

    arquivos = os.listdir(pasta_origem) 

    for arquivo in arquivos:
        caminho_arquivo_origem = os.path.join(pasta_origem, arquivo)
        caminho_arquivo_destino = os.path.join(pasta_destino, arquivo)

        # Verifica se é um arquivo e não um diretório
        if os.path.isfile(caminho_arquivo_origem):
            shutil.copy2(caminho_arquivo_origem, caminho_arquivo_destino)
            print(f'{arquivo} copiado de {pasta_origem} para {pasta_destino}')

if __name__ == "__main__":
    # Especifica as pastas (troque se necessário)
    pasta_origem = r"D:\users\João Victor Poloniato Buss\OneDrive\Documentos\GitHub\busca_cep"
    pasta_destino = r"D:\users\João Victor Poloniato Buss\OneDrive\Documentos\GitHub\BuscaArquivo\anexaarquivo"

    main(pasta_origem, pasta_destino)
