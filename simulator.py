from libs import *
import calculator as cal
from calculator import T_0, T_t, Sensor_TimeDuration, Setup_CameraSensor, Split_frame


#Setup
Package = [1,0,1,1,0,1,0,1,1,1,0,1,1,0,1,0,1,1]
Signal = [400, Package]
time_start_transmit = 0  #To calculate argument of symbol - T_t
time_start_record = 0    #To calculate argument of sensor - T_0

Symbols_package = cal.SetupPackageSignals(Signal)
Symbols = Symbols_package.Symbol_Package_communication()['Symbols']
print(Symbols)
Sensor_info = Setup_CameraSensor(sensor_size = (1080,1920), Fps=30, T_exp=1/800, T_row=0.000001*20, T_rdout=0.000001*10)
Sensor = Sensor_info.Initilization_Sensor()
Sensor_matrix = Sensor['Sensor_matrix']
Fps = Sensor['Fps']
T_row = Sensor['T_row']
T_exp = Sensor['T_exp']
T_rdout = Sensor['T_rdout']


TimeDuration = Sensor_TimeDuration(t_startRecord= time_start_record, t_startTransmit= time_start_transmit, 
                                   Sensor= Sensor, Symbols=Symbols)

### Grammar code
# sample = TimeDuration.Info_Row(2, 0)
# print(sample)
# Symbol_element, info = Symbols.Symbol_element(0)
# print(Symbol_element, info)
###

def Conditional_checking(x, k):
    a, b = TimeDuration.Info_Frame(x)['Info_Frame']
    Info_symbol = Symbols_package.Symbol_element(k)['Info_Symbol']
    c, d = Info_symbol    
    if b>c and a<d:
        return True        
    else:
        return False        
def Effected_frame_by_symbol(k):
    t_k = Symbols_package.Symbol_element(k)['TimeStart_Symbol']
    x = int(t_k*Fps)
    return x
def Effected_row_by_symbol(x, k):
    t_k1 = Symbols_package.Symbol_element(k)['TimeStart_Symbol']
    t_k2 = Symbols_package.Symbol_element(k)['TimeEnd_Symbol']
    a = ((t_k1 - T_0 - (x)/Fps - T_exp - T_rdout)/T_row) 
    b = ((t_k1 - T_0 - (x)/Fps)/T_row)
    
    c = ((t_k2 - T_0 - (x)/Fps - T_exp - T_rdout)/T_row) 
    d = ((t_k2 - T_0 - (x)/Fps)/T_row) 
    if a < 0:
        a = 0
    if b > 1079:
        b = 1079
    if c < 0:
        c = 0
    if d > 1079:
        d = 1079
    
    arr_i = np.arange(int(a), int(d)+1, 1)
    return arr_i

def Exposure_intensity(k, symbol, x, i):
    a, b = Symbols_package.Symbol_element(k)['Info_Symbol']
    c, d = TimeDuration.Info_Row(x,i)['Info_Row']
    if symbol == 1:
        if c<=a<d<=b:
            Gray_level = ((d-a)/T_exp)*255
            Intensity = int(Gray_level)
            return Intensity
        elif a<=c<d<=b:
            Gray_level = 255
            Intensity = int(Gray_level)
            return Intensity
        elif a<=c<b<=d:
            Gray_level = ((b-c)/T_exp)*255
            Intensity = int(Gray_level)
            return Intensity
        else:
            Intensity  = 0
            return Intensity    

    else:
        if c<=a<d<=b:
            Gray_level = ((d-a)/T_exp)*255
            Intensity = 255-int(Gray_level)
            return Intensity
        elif a<=c<d<=b:
            Gray_level = 255
            Intensity = 255-int(Gray_level)
            return Intensity
        elif a<=c<b<=d:
            Gray_level = ((b-c)/T_exp)*255
            Intensity = 255-int(Gray_level)
            return Intensity
        else:
            Intensity  = 0
            return Intensity    
        





Symbols_status = []
# Symbols_status[i][0] - k_symbol
# Symbols_status[i][1] - symbol
# Symbols_status[i][2] - x_frame
# Symbols_status[i][3] - rows are effected by symbol


for k, symbol in enumerate(Symbols):
    period_of_frame = (1080-1)*T_row + T_exp + T_rdout
    x_frame = Effected_frame_by_symbol(k)
    list_row = Effected_row_by_symbol(x_frame, k)
    # print('Symbol', k, ', Frame: ', x_frame)
    # print(list_row, symbol)
    Symbols_status_element = [k, symbol, x_frame, list_row]
    Symbols_status.append(Symbols_status_element)
    
# Remove the same effected rows by symbol_(k+1) as that with symbol_(k) & symbol_(k+2)
# for k in range(0, len(Symbols_status), 2):
#     print('#########################################')

#     if k+1 != len(Symbols_status):
#         Symbols_status[k+1][3] = list(Symbols_status[k+1][3])
#         for x in Symbols_status[k][3]:
#             if x in Symbols_status[k+1][3]:
#                 Symbols_status[k+1][3].remove(x)
#     if k+2 != len(Symbols_status):        
#         for x in Symbols_status[k+2][3]:
#             if x in Symbols_status[k+1][3]:
#                 Symbols_status[k+1][3].remove(x)
#     Symbols_status[k+1][3] = np.array(Symbols_status[k+1][3])
    # print('symbol',k,'is' ,Symbols_status[k][1], Symbols_status[k][3])
    # print('symbol',k+1,'is' ,Symbols_status[k+1][1], Symbols_status[k+1][3])
    
# print(Symbols_status)
Sensor_status = Split_frame(Symbols_status)
for symbol_status_element in Sensor_status[0]:
    Instensity_of_row_in_symbol_status_element = []
    k = symbol_status_element[0]
    symbol = symbol_status_element[1]
    frame = symbol_status_element[2]
    rows_list = symbol_status_element[3]
    for row in rows_list:
        I = Exposure_intensity(k, symbol, frame, row)
        Instensity_of_row_in_symbol_status_element.append(I)
    print(Instensity_of_row_in_symbol_status_element)
    symbol_status_element.append(Instensity_of_row_in_symbol_status_element)
    
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',Sensor_status[0]) #Frame 0 with [k, symbol, x_frame, row_list, intensive_list]


for k in Sensor_status[0]:
    for row in k[3]:
        for i,k_compare in enumerate(Sensor_status[0]):
            if k[0] != k_compare[0]:
                if row in  k_compare[3]:
                    print(row, k_compare[4][i])
                
