from rubs import rubs_list
import bot_func as bf
from time import sleep
# print(py.position())

def desativar(user : str, senha : str, rubs_selected : list):
    
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
    sleep(1)

    # Abre o site do Rub
    bf.escrever(frase='https://srvuca662.br-atacadao.corp/vue/#/core/web/dispositivo')
    bf.pressionarTecla('enter')
    sleep(1)

    # Faz login no site, não tem problema caso já esteja feito
    bf.pressionarTecla('tab')
    bf.escrever(f'{user}')
    bf.pressionarTecla('tab')
    bf.escrever(f'{senha}')
    bf.pressionarTecla('enter')
    sleep(0.5)
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
    for rub in rubs_selected:
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

def error():
    bf.alerta(
        title='ERROR MESSENGE!',
        mess='''
                ESTÁ FALTANDO PREENCHER ALGUM DOS CAMPOS
                POR FAVOR, PREENCHA-OS E CONTINUE
''',
        button='OK'
    )