
from libs import *
import calculator as cal
from calculator import T_0, T_t, Sensor_TimeDuration, Setup_CameraSensor


#Setup
Package = [1,1,1,1,0]
Signal = [300, Package]
time_start_transmit = 0  #To calculate argument of symbol - T_t
time_start_record = 0    #To calculate argument of sensor - T_0

Symbols_package = cal.SetupPackageSignals(Signal)
Symbols = Symbols_package.Symbol_Package_communication()['Symbols']
print(Symbols)
Sensor_info = Setup_CameraSensor(sensor_size = (1080,1920), Fps=30, T_exp=1/800, T_row=0.000001*20, T_rdout=0.000001*10)
Sensor = Sensor_info.Initilization_Sensor()
Sensor_img = Sensor['Sensor_matrix']
for i in range(100,200):
    Sensor_img[i]=255
plt.imshow(Sensor_img, cmap='gray')
plt.show()
