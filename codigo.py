# Passo a passo do projeto

# ----- Passo 1 - Entrar no sistema da empresa 
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

#pyautogui - RPA automação bot (pip install ptautogui)

import pyautogui
import time

# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar -> pyautogui.press
# apertar -> pyautogui.hotkey (cria atalho com varias teclas)
# scroll/rolar -> pyautogui.scroll

# aperta a tecla do windows
# digita o nome do programa (chrome)
# aperta enter
# digitar o link
# apertar enter

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("mozilla")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.click(x=612, y=75)
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(2.5)


# -------- Passo 2 - Fazer Login
# digitar o email
# passar para o campo de senha
# digitar a senha
# dar enter

pyautogui.click(x=623, y=452)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("minha senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2.5)


# ------- Passo 3 - Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# ------ Passo 4 - Cadastrar um produto

for linha in tabela.index:
    pyautogui.click(x=668, y=319)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    #enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)


# ------ Passo 5 - Repetir isso até acabar a base de dados
# Acrescentar um alerta indicando que a inclusão da base foi feita no sistema. 
