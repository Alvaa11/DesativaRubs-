import controller.bot_func as bf
from time import sleep
from rubs import rubs_list



class BotRubs():
    def __init__(self, rubs_selected : list[str]):
        self.rubs_selected = rubs_selected

    def desativar(self):
        
        # Abre tela cheia e abaixa a aba dos rubs
        bf.pressionarTecla('f11')
        sleep(1.5)
        bf.moverMouse(x=39, y=93)
        bf.clicar()
        sleep(0.5)
        bf.moverMouse(x=1567, y=441)
        bf.clicar()
        sleep(0.5)
        bf.segurarTecla('ctrl')

        # Seleciona os Rubs passados pelo o usuario
        for rub in self.rubs_selected:
            bf.moverMouse(rubs_list[f'{rub}']['x'], rubs_list[f'{rub}']['y'])
            sleep(0.5)  
            bf.clicar()

        bf.soltarTecla('ctrl')

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

