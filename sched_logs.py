"""
Task simples que tem o funcionamento parecido com o cron do linux.

Neste exemplo a função saytime é chamada e escreve a
    hora atual no arquivo de log
"""
import sched
import logging
from time import time, ctime
from datetime import datetime, timedelta
from itertools import count

# Configurações básicas do logging
logging.basicConfig(filename='sched.txt',
                    filemode='w',
                    level=logging.INFO)

# cria a instancia do basicConfig
log = logging.getLogger()

# cria um scheduler baseado em time
scheduler = sched.scheduler(timefunc=time)


def one_minute_taks(function):
    """
    Função que seta o próximo minuto redondo (MIN:00:00) e inicia o scheduler
        com a função do argumento para ser executada de 1 em um minuto
    vars:
        - new_target: pega a hora atual e substitui os minutos
                            e segundos para zero e soma mais 1 minuto

    obs: scheduler.enterabs: agenda a proxima execução da function;
        ou seja, toda vez que one_minute_taks é chamanda, agenda sua proxima
        execução
    """
    new_target = datetime.now().replace(
        second=0, microsecond=0)
    new_target += timedelta(minutes=1)
    scheduler.enterabs(
        new_target.timestamp(), priority=0, action=function)


def saytime():
    """
    Função que escreve a hora no log e chamanda one_minute_taks com ela mesma
        para que seja executada na sequência do scheduler
    """
    log.info(ctime())
    one_minute_taks(saytime)

one_minute_taks(saytime)

try:
    # inicia o processo do scheduler
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print('Stopped.')
