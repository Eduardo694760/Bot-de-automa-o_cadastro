# Bot de automação para digitar as peças e etc... da metalurgica.


#Importa as biblbiotecas

import pyautogui
import pandas as pd
import time

# Importar a planilha Exce
df = pd.read_excel('planilha_pecas_metalurgica.xlsx')

# Abrir o menu iniciar do Windows
pyautogui.press('win')
time.sleep(1)

# Pesquisar chrome e dar enter
pyautogui.write('chrome', interval=0.1)
pyautogui.press('enter')
time.sleep(3) # Aguarda o Chrome abrir

# Clicar na barra de pesquisa usando as coordenadas informadas
pyautogui.click(x=931, y=410)
time.sleep(0.5) # Pausa curta para garantir o foco do clique

# Clicar na barra de pesquisa (garante o foco) e digitar o link
# NOTA: Substitua 'LINK_DO_SEU_SITE_AQUI' pela URL real do sistema
pyautogui.write('https://m90jpy9j64.youware.app', interval=0.05)
pyautogui.press('enter')
time.sleep(5) # Aguarda o site carregar completamente

# --- NOVO CLIQUE SOLICITADO ---
# Clica na posição informada após a pesquisa do link
pyautogui.click(x=140, y=225)
time.sleep(6)

# --- PASSO A PASSO: LOOP DE CADASTRO --

# O loop lê linha por linha e para sozinho automaticamente no final da planilha
for index, linha in df.iterrows():
    
    # Extrai os dados exatos da sua planilha
    codigo       = str(linha['Código da Peça'])
    nome         = str(linha['Nome da Peça'])
    categoria    = str(linha['Categoria'])
    material     = str(linha['Material'])
    quantidade   = str(linha['Quantidade'])
    preco        = str(linha['Preço Unitário (R$)'])
    fornecedor   = str(linha['Fornecedor'])
    
    # 1. Clica no primeiro campo da página para focar
    # AJUSTE AQUI: Mude o X e Y para a posição real da barra de pesquisa do site
    pyautogui.click(x=500, y=400) 
    time.sleep(0.5)
    
    # 2. Sequência de digitação e navegação por TAB
    pyautogui.write(codigo, interval=0.05)
    pyautogui.press('tab')
    
    pyautogui.write(nome, interval=0.05)
    pyautogui.press('tab')
    
    pyautogui.write(categoria, interval=0.05)
    pyautogui.press('tab')
    
    pyautogui.write(material, interval=0.05)
    pyautogui.press('tab')
    
    pyautogui.write(quantidade, interval=0.05)
    pyautogui.press('tab')
    
    pyautogui.write(preco, interval=0.05)
    pyautogui.press('tab')
    
    # Último campo: digita o fornecedor e dá ENTER para salvar a peça
    pyautogui.write(fornecedor, interval=0.05)
    pyautogui.press('enter')
    
    # Tempo de espera para o site salvar a peça antes de ir para a próxima linha
    time.sleep(2.5)

print("Todas as peças foram cadastradas. O bot parou automaticamente!")



