from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat ()
sense.set_rotation (180)

# r = 255
# g = 0
# b = 255
while True:
    temperatur = round(sense.get_temperature_from_humidity (), 1)
    druck = round(sense.get_pressure (), 1)
    feuchte = round(sense.get_humidity (), 1)

    print (temperatur)
    print (druck)
    print (feuchte)

    ausgabe = ('Temperatur: %s C ' % str(temperatur) + 'Luftdruck: %s hPa ' % str(druck)+ 'Luftfeuchtigkeit: %s %%' % str(feuchte))
    #ausgabe = ('Werte: ' + str(temperatur)+ 'C' + str(druck) + 'hPa' + str(feuchte) + '%%')
    sense.show_message (ausgabe, scroll_speed = 0.1)

# sense.show_letter ('1', text_colour = (255, 0,255), back_colour = (0, 255,0))
# sleep (1)
# sense.show_letter ('A')
#sense.show_message ('Hallo ihr Ficker', text_colour = (255,0,0), scroll_speed = 0.2)

#sense.clear (r,g,b)

# while True:
#     sense.show_message ('Hello world')
   
#print (dir(sense))
    
#pythonhosted.org/sense-hat/
