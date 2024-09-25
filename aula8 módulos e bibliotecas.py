import os #biblioteca os permite trabalhar com arquivos e pastas do seu pc
import datetime #permite trabalhar com horas e datas
import  pyautogui

pyautogui.press("win") #aperta uma tecla
pyautogui.write("chrome") #escreve

print(os.listdir("arquivos")) #listar os arquivos de um diretorio (pasta) 

print(datetime.date.today()) #vai mostrar a data de hoje

data = datetime.date.today()

print(f"Hoje {data}, voce tem uma consulta agendada")


#exercicio 1
lista_arquivos = os.listdir("arquivos")

for arquivo in lista_arquivos:
    if ".txt" in arquivo:
        if "22" in arquivo:
            os.rename(f"arquivos/{arquivo}" , f"arquivos/22/{arquivo}") #mudando os arquivos que tem 22 para a pasta 22
            
        else:
            os.rename(f"arquivos/{arquivo}", f"arquivos/23/{arquivo}") #mudando os arquivos que tem 23 para a pasta 23
            