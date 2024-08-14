import os
import shutil
import time
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def compactar_pasta(pasta_destino, caminho_backup):
    caminho_rar_exe = r"C:\Program Files\WinRAR\rar.exe"
    comando = [
        caminho_rar_exe, "a", "-r", caminho_backup, os.path.join(pasta_destino, "*")
    ]

    subprocess.run(comando, check=True)
    print(f'Todos os arquivos foram compactados em {caminho_backup}')

def enviar_email(subject, body, to_email):
    from_email = 'poloniato155@gmail.com'  # Seu e-mail
    password = '2018112020310157'  # Sua senha de e-mail

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Configurar o servidor SMTP
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Falha ao enviar e-mail: {e}')

def main(pasta_origem, pasta_destino):
    while True:
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        arquivos = os.listdir(pasta_origem)

        for arquivo in arquivos:
            caminho_arquivo_origem = os.path.join(pasta_origem, arquivo)
            caminho_arquivo_destino = os.path.join(pasta_destino, arquivo)

            if os.path.exists(caminho_arquivo_destino):
                
                if os.path.isfile(caminho_arquivo_origem):
                    origem_mod_time = os.path.getmtime(caminho_arquivo_origem)
                    destino_mod_time = os.path.getmtime(caminho_arquivo_destino)

                    if origem_mod_time > destino_mod_time:
                        shutil.copy2(caminho_arquivo_origem, caminho_arquivo_destino)
                        print(f'{arquivo} atualizado em {pasta_destino}')
                    else:
                        print(f'{arquivo} já existe e não foi modificado, pulando...')
                    continue

                elif os.path.isdir(caminho_arquivo_origem):
                    origem_mod_time = os.path.getmtime(caminho_arquivo_origem)
                    destino_mod_time = os.path.getmtime(caminho_arquivo_destino)

                    if origem_mod_time > destino_mod_time:
                        shutil.rmtree(caminho_arquivo_destino)
                        shutil.copytree(caminho_arquivo_origem, caminho_arquivo_destino) 
                        print(f'Diretório {arquivo} atualizado em {pasta_destino}')
                    else:
                        print(f'Diretório {arquivo} já existe e não foi modificado, pulando...')
                    continue

            if os.path.isfile(caminho_arquivo_origem):
                shutil.copy2(caminho_arquivo_origem, caminho_arquivo_destino)
                print(f'{arquivo} copiado de {pasta_origem} para {pasta_destino}')
            elif os.path.isdir(caminho_arquivo_origem):
                shutil.copytree(caminho_arquivo_origem, caminho_arquivo_destino)
                print(f'Diretório {arquivo} copiado de {pasta_origem} para {pasta_destino}')

        caminho_backup = os.path.join(pasta_destino, "backup", "backup.rar")
        if not os.path.exists(os.path.dirname(caminho_backup)):
            os.makedirs(os.path.dirname(caminho_backup))
        compactar_pasta(pasta_destino, caminho_backup)

        # Enviar e-mail após o backup
        subject = 'Backup Completo'
        body = f'O backup foi concluído com sucesso e os arquivos foram compactados em {caminho_backup}.'
        to_email = 'kailageovana@gmail.com'  # E-mail do destinatário

        enviar_email(subject, body, to_email)

        print("Aguardando 60 segundos para a próxima verificação...")
        time.sleep(60)  # tempo para executar novamente

if __name__ == "__main__":
    # Especifica as pastas (troque se necessário)
    pasta_origem = r"D:\users\João Victor Poloniato Buss\OneDrive\Documentos\GitHub\CALCULADORA-JS"
    pasta_destino = r"D:\users\João Victor Poloniato Buss\OneDrive\Documentos\GitHub\BuscaArquivo\anexaarquivo"

    main(pasta_origem, pasta_destino)
