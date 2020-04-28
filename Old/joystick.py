from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.set_rotation (180)

sense.clear((0,0,0))

# while True:
#     for event in sense.stick.get_events():
#         if event.action is 'pressed':
#             if event.direction is 'up':
#                 sense.show_letter('U')
#             sleep(0.5)
#             sense.clear()
#         print(event.direction, event.action)
        
#sense.stick.direction_up

def changetemp (temperatur):
    fahrenheit = round(int(1.8 * temperatur + 32))
    return fahrenheit
    

while True:              
    temperatur = round(sense.get_temperature_from_humidity (),1)
    #print (temperatur)
    #temperatur2 = round(sense.get_temperature_from_pressure (), 1)
    #print (temperatur2)

    for event in sense.stick.get_events():
        if event.action is 'pressed':
            if event.direction is 'up':
                temperatur = changetemp (temperatur)
                ausgabe = ('Werte: ' + str(temperatur))
                sense.show_message (ausgabe, scroll_speed = 0.1)
            if event.direction is 'down':
                temperatur = changetemp (temperatur)
                ausgabe = ('Werte: ' + str(temperatur))
                sense.show_message (ausgabe, scroll_speed = 0.1)
                      
#     ausgabe = ('Werte: ' + str(temperatur))
#     print (ausgabe)
#     ausgabe = ('Werte: ' + str(temperatur)+ 'C ' + str(temperatur2) + 'C')
#     sense.show_message (ausgabe, scroll_speed = 0.1)
