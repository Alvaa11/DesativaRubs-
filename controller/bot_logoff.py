import controller.bot_func as bf
from time import sleep

class BotLogOff():
    def __init__(self):
        pass

    def log_off():
          # Faz a desvinculação dos rubs
        bf.moverMouse(x=411, y=42)
        bf.clicar()
        sleep(0.5)
        bf.moverMouse(x=851, y=347)
        bf.clicar()
        sleep(1)

        # Sai do login do usuário e fecha o Browser
        bf.moverMouse(x=1509, y=9)
        bf.clicar()
        sleep(0.5)
        bf.moverMouse(x=1510, y=124)
        bf.clicar()
        sleep(0.5)
        bf.pressionarTecla('f11')
        bf.pressionarTeclas('alt', 'f4')

