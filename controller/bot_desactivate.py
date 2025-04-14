import controller.bot_func as bf
from time import sleep
from rubs import rubs_list
import controller.bot_logoff as bl



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

        # Chama o proximo bot responsável pelo logoff do usuario
        bot = bl.BotLogOff()
        bot.log_off()
