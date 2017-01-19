"""
Exemplo de um temporazidor que evenia e-mail em um tempo pré definido

Nesse caso ele enviara um e-mail a cada 10 segundos para todos da lista
Com a hora/data atual.
"""
import smtplib
from time import sleep
from time import gmtime, strftime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_dict = {'subject': 'ASSUNTO',
             'from': 'teste@gmail.com',
             'msg': 'Teste'}


def run_task(mails: list, mail_dict: dict) -> None:
    while True:
        for mail in mails:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = mail_dict['subject']
            msg['From'] = mail_dict['from']
            msg['To'] = mail

            me = mail_dict['from']
            you = mail
            text = 'Hora atual\n\n{}'.format(strftime("%Y-%m-%d %H:%M:%S",
                                                      gmtime()))
            msg = MIMEText(text, 'plain')

            mail = smtplib.SMTP('smtp.gmail.com', 587)

            mail.ehlo()

            mail.starttls()

            mail.login(mail_dict['from'], "eduzinh0oo")
            mail.sendmail(me, you, msg.as_string())
            mail.quit()
        sleep(10)

run_task(['teste@gmail.com', 'teste@gmail.com'], mail_dict)
