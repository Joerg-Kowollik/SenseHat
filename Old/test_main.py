from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation (180)
sense.clear((0,0,0))

temperatur = round(sense.get_temperature(),1)
druck = round(sense.get_pressure (), 1)
feuchte = round(sense.get_humidity (), 1)

def degree(temperatur, druck, feuchte):
    
    ausgabe = ('Temperatur: %s C ' % str(temperatur) + 'Luftdruck: %s hPa ' % str(druck)+ 'Luftfeuchtigkeit: %s %%' % str(feuchte))
    print (ausgabe)
    sleep(1)

def fahrenheit(temperatur, druck, feuchte):
    
    fahrenheit = round(int(1.8 * temperatur + 32))
    ausgabe = ('Temperatur: %s F ' % str(fahrenheit) + 'Luftdruck: %s hPa ' % str(druck)+ 'Luftfeuchtigkeit: %s %%' % str(feuchte))
    print (ausgabe)
    sleep(1)

degree (temperatur, druck, feuchte)
fahrenheit (temperatur, druck, feuchte)
