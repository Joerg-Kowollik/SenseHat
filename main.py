from sense_hat import SenseHat
from time import sleep
import smtplib
from email.mime.text import MIMEText
import pickle

def degree(temperatur, druck, feuchte):

    ausgabe = ('Temperatur: %s C ' % str(temperatur) + 'Luftdruck: %s hPa ' % str(druck)+ 'Luftfeuchtigkeit: %s %%' % str(feuchte))
    sense.show_message (ausgabe, scroll_speed = 0.1)
    print (ausgabe)
    sleep(1)

def fahrenheit(temperatur, druck, feuchte):
    
    fahrenheit = round(int(1.8 * temperatur + 32))
    ausgabe = ('Temperatur: %s F ' % str(fahrenheit) + 'Luftdruck: %s hPa ' % str(druck)+ 'Luftfeuchtigkeit: %s %%' % str(feuchte))
    sense.show_message (ausgabe, scroll_speed = 0.1)
    print (ausgabe)
    sleep(1)
    
def mail(ausgabe):
    title = ausgabe
    msg_content = '<h2>{title} <font color="red">Sturmwarnung</font></h2>\n'.format(title=title)
    message = MIMEText(msg_content, 'html')

    message['From'] = 'Raspberry Pi Wetterstation <embsys@outlook.de>'
    message['To'] = 'Receiver Name <kowollik@hm.edu>'
    message['Cc'] = 'Receiver2 Name <kowollik@hm.edu>'
    message['Subject'] = 'Sturmwarnung'

    msg_full = message.as_string()

    server = smtplib.SMTP('smtp-mail.outlook.com:587')
    server.starttls()
    server.login('embsys@outlook.de', 'hm-embedded')
    server.sendmail('embsys@outlook.de',
                ['kowollik@hm.edu', 'kowollik@hm.edu'],
                msg_full)
    server.quit()

filename = 'einstellung'
n = 1
m = 0
sense = SenseHat()
sense.set_rotation (180)
sense.clear((0,0,0))

file = open(filename,'rb')
n = pickle.load(file)
file.close()

while True:
    
    temperatur = round(sense.get_temperature(),1)
    druck = round(sense.get_pressure (), 1)
    feuchte = round(sense.get_humidity (), 1)
        
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            if event.direction == 'up':
                degree(temperatur, druck, feuchte)
                n = 1
            if event.direction == 'down':
                fahrenheit(temperatur, druck, feuchte)
                n = 2
    else:
        if n == 1:
            degree(temperatur, druck, feuchte)
        if n == 2:
            fahrenheit (temperatur, druck, feuchte)
            
    file = open (filename, 'wb')
    pickle.dump (n, file)
    file.close()
    
    if druck < 950:
        red = (255,0,0)
        sense.show_message ('STURM', text_colour = red)
    
    if druck < 950 and m < 1:
        mail(ausgabe)
        m = m + 1
