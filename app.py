import pyautogui as py
from time import sleep
from rubs import rubs
# print(py.position())

# Abre um novo Browser
py.moveTo(x=938, y=874)
py.click(button='right')
py.moveTo(x=893, y=749)
py.click()
sleep(1)

# Abre o site do Rub
py.typewrite('https://srvuca662.br-atacadao.corp/vue/#/core/web/dispositivo')
py.press('enter')
sleep(1)

# Faz login no site, não tem problema caso já esteja feito
py.press('tab')
py.typewrite('010454164')
py.press('tab')
py.typewrite('Iamnotafraid1!')
py.press('enter')
py.press('f11')
sleep(1.5)
py.moveTo(x=1567, y=441)
py.click()
py.keyDown('ctrl')

# Seleciona os Rubs passados pelo o usuario
py.moveTo(rubs['35']['x'], rubs['35']['y'])
sleep(0.5)
py.click()
py.moveTo(rubs['03']['x'], rubs['03']['y'])
sleep(0.5)
py.click()

py.keyUp('ctrl')

# Faz a desvinculação dos rubs
py.moveTo(x=411, y=42)
py.click()
py.moveTo(x=851, y=347)
py.click()
sleep(1)

# Sai do login do usuário e fecha o Browser
py.moveTo(x=1509, y=9)
py.click()
sleep(0.5)
py.moveTo(x=1510, y=124)
py.click()
sleep(0.5)
py.press('f11')
py.moveTo(x=1579, y=17)
py.click()





