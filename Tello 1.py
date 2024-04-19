import djitellopy
from djitellopy import Tello

dron = Tello()
dron.connect()

##detectar objeto


##Revisar bateria
x = dron.get_battery()
print('Battery: ', x)

##Despegar
dron.takeoff()

dron.move_up(50)
dron.rotate_clockwise(360)
dron.move_forward(50)

##Aterrizar
dron.land()