import pyautogui
import pandas as pd
import time

# Mover para coordenadas X e Y
pyautogui.moveTo(100, 200, duration=1)

# Clicar em uma posição (padrão: botão esquerdo)
pyautogui.click(100, 200)

# Clicar com botão direito ou clique duplo
pyautogui.click(button='right')
pyautogui.doubleClick()

# Arrastar o mouse até a posição
pyautogui.dragTo(300, 400, duration=0.5)

# Rolar a tela (positivo para cima, negativo para baixo)
pyautogui.scroll(500)

# Pegar a posição atual do mouse
x, y = pyautogui.position()
