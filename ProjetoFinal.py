#janela para selecionar a pasta do nosso computador
import os
from tkinter.filedialog import askdirectory 
import shutil
import datetime

nome_pasta_selecionada = askdirectory()

lista_de_arquivos = os.listdir(nome_pasta_selecionada)

#fazer o backup dos arquivos que estão nessa pasta
nome_pasta_backup = "backup"
nome_completo_pasta_backup = f"{nome_pasta_selecionada}/{nome_pasta_backup}"

if not os.path.exists(nome_completo_pasta_backup): #se nao existir a pasta backup, ele cria uma
    os.mkdir(nome_completo_pasta_backup)

data_atual = datetime.datetime.today().strftime("%Y-%m-%d %H%M%S")

for arquivo in lista_de_arquivos:
    nome_completo_arquivo = f"{nome_pasta_selecionada}/{arquivo}"
    nome_final_arquivo = f"{nome_completo_pasta_backup}/{data_atual}/{arquivo}"
    
    if not os.path.exists(f"{nome_pasta_selecionada}/{arquivo}"): #se nao existir a pasta backup, ele cria uma
        os.mkdir(f"{nome_pasta_selecionada}/{arquivo}")

    if "." in arquivo:
        shutil.copy2(nome_completo_arquivo, nome_final_arquivo) #shutil.copy2 copia so arquivos
    elif not "backup" in arquivo:
        shutil.copytree(nome_completo_arquivo, nome_final_arquivo) #copia tudo que tem dentro da pasta

