from sense_hat import SenseHat
from time import sleep
import pickle


filename = 'einstellung'
n = 1
sense = SenseHat()
sense.set_rotation (180)
sense.clear((0,0,0))

file = open(filename,'rb')
n = pickle.load(file)
file.close()

def degree():
    temperatur = round(sense.get_temperature(),1)
    druck = round(sense.get_pressure (), 1)
    feuchte = round(sense.get_humidity (), 1)
    
    ausgabe = ('Temperatur: %s C ' % str(temperatur) + 'Luftdruck: %s hPa ' % str(druck)+ 'Luftfeuchtigkeit: %s %%' % str(feuchte))
    #ausgabe = ('Temperatur in Grad Celsius ' + str(temperatur))
    #sense.show_message (ausgabe, scroll_speed = 0.1)
    print (ausgabe)
    sleep(1)

def fahrenheit():
    temperatur = round(sense.get_temperature(),1)
    druck = round(sense.get_pressure (), 1)
    feuchte = round(sense.get_humidity (), 1)
    
    fahrenheit = round(int(1.8 * temperatur + 32))
    
    ausgabe = ('Temperatur: %s F ' % str(fahrenheit) + 'Luftdruck: %s hPa ' % str(druck)+ 'Luftfeuchtigkeit: %s %%' % str(feuchte))
    #ausgabe = ('Temperatur in Fahrenheit ' + str(fahrenheit))
    #sense.show_message (ausgabe, scroll_speed = 0.1)
    print (ausgabe)
    sleep(1)

while True:
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            if event.direction == 'up':
                degree()
                n = 1
            if event.direction == 'down':
                fahrenheit()
                n = 2
    else:
        if n == 1:
            degree()
        if n == 2:
            fahrenheit ()
            
    file = open (filename, 'wb')
    pickle.dump (n, file)
    file.close()

while True:
    pass