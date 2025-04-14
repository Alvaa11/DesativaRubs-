import controller.bot_func as bf
from time import sleep
import controller.bot_desactivate as bd

class BotLogin():
    def __init__(self, user : str, senha : str, rubs_selected : list):
        self.user = user
        self.senha = senha
        self.rubs_selected = rubs_selected

    def login(self):
        
        bf.alerta(
            title='AVISO!!',
            mess='''
                O robô irá controlar seu mouse e teclado 
                        então por favor, NÃO MEXA
            para que possa ocorrer tudo bem com o  script mantenha a página
            do rub em 75% de zoom. obrigado!
    ''',
            button='OK'
        )
        
        # Abre um novo Browser
        bf.moverMouse(x=938, y=874)
        bf.clicar(button='right')
        bf.moverMouse(x=893, y=749)
        bf.clicar()
        sleep(1.5)

        # Abre o site do Rub
        bf.escrever(frase='https://srvuca662.br-atacadao.corp/vue/#/core/web/dispositivo')
        bf.pressionarTecla('enter')
        sleep(1)
        # Faz login no site, não tem problema caso já esteja feito
        bf.pressionarTecla('tab')
        bf.escrever(f'{self.user}')
        bf.pressionarTecla('tab')
        bf.escrever(f'{self.senha}')
        bf.pressionarTecla('enter')
        sleep(0.5)

        # Chama o proximo bot responsavel pela desativação
        bot = bd.BotRubs(self.rubs_selected)
        bot.desativar()

    def error():
        bf.alerta(
            title='ERROR MESSENGE!',
            mess='''
                    ESTÁ FALTANDO PREENCHER ALGUM DOS CAMPOS
                    POR FAVOR, PREENCHA-OS E CONTINUE
    ''',
            button='OK'
        )

    
