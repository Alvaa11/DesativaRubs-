import pyautogui as py

def moverMouse(x: int, y:int):
    py.moveTo(x, y)

    return

def clicar(button : str = 'left'):
    py.click(button=button)

    return

def doisCliques():
    py.doubleClick()
    
    return

def pressionarTecla(tecla : str):
    py.press(tecla)

    return

def pressionarTeclas(*args : str):
    py.hotkey(*args)

def escrever(frase : str, interval : float = 0):
    py.typewrite(message=frase, interval=interval)

    return

def segurarTecla(tecla : str):
    py.keyDown(tecla)

    return

def soltarTecla(tecla : str):
    py.keyUp(tecla)

def alerta(title : str, mess : str, button : str):
    py.alert(title=title, text=mess, button=button)