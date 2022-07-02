from random import sample
from libs import *
T_t = 0
T_0 = 0 #Start record to receive signals
class Setup_CameraSensor():
    global T_0
    def __init__(self, sensor_size, Fps, T_exp, T_row, T_rdout):
        self.sensor_size = sensor_size
        self.Fps = Fps
        self.T_exp = T_exp
        self.T_row = T_row
        self.T_rdout = T_rdout
    def Initilization_Sensor(self):
        Sensor_size = self.sensor_size
        matrix = np.zeros(Sensor_size)
        sensor = {
            'Sensor_matrix': matrix,
            'Fps': self.Fps,
            'T_row': self.T_row,
            'T_exp': self.T_exp,
            'T_rdout': self.T_rdout
            
        }
        return sensor
class Sensor_TimeDuration():
    def __init__(self, t_startRecord, t_startTransmit, Sensor, Symbols):
        self.Signals = Symbols
        self.t_startRecord = t_startRecord
        self.t_startTransmit = t_startTransmit
        self.Fps = Sensor['Fps']
        self.T_row = Sensor['T_row']
        self.T_exp = Sensor['T_exp']
        self.T_rdout = Sensor['T_rdout']
    def Info_Row(self, ordinal_postion_of_frame, ordinal_position_of_row):
        T_0 = self.t_startRecord
        T_row = self.T_row
        Fps = self.Fps
        T_exp = self.T_exp
        T_rdout = self.T_rdout
        x = ordinal_postion_of_frame
        i = ordinal_position_of_row
        #frame
        Time_start_frame_x = T_0 + (x)/Fps
        Time_end_frame_x = Time_start_frame_x + (1079)*T_row + T_exp + T_rdout
        #row
        Time_start_row_i_in_frame_x = Time_start_frame_x +(i)*T_row
        Time_end_row_i_in_frame_x = Time_start_frame_x +(i)*T_row + T_exp + T_rdout
        
        sample = {
            'Info_Row': [Time_start_row_i_in_frame_x, Time_end_row_i_in_frame_x],
            'Info_Frame': [Time_start_frame_x, Time_end_frame_x]
        }
        return(sample)        
    def Info_Frame(self, ordinal_postion_of_frame):
        T_0 = self.t_startRecord
        T_row = self.T_row
        Fps = self.Fps
        T_exp = self.T_exp
        T_rdout = self.T_rdout
        x = ordinal_postion_of_frame 
        #frame
        Time_start_frame_x = T_0 + (x)/Fps
        Time_end_frame_x = Time_start_frame_x + (1079)*T_row + T_exp + T_rdout
        sample = {
            'Info_Frame': [Time_start_frame_x, Time_end_frame_x],
            'period' : (1080-1)*T_row + T_exp + T_rdout
        }
        return sample

    def Time_coordinate(self, ordinal_position_of_symbol):
        k = ordinal_position_of_symbol
        x, y = SetupPackageSignals(self.Signals).Timer_symbol(k)

class SetupPackageSignals():
    
    def __init__(self, Signals):
        Manchester_coding = []
        self.Info_symbol = Signals
        Frequency_signal = Signals[0]
        Signal_matrix = Signals[1]
        self.Frequency_signal = Frequency_signal
        self.Signal_matrix = Signal_matrix
        for i in Signal_matrix:
            if i == 1:
                Manchester_coding.append(1)
                Manchester_coding.append(0)
            else: 
                Manchester_coding.append(0)
                Manchester_coding.append(1)
        T_sym = 1/(2*Frequency_signal)
        
        self.T_sym = T_sym
        self.Manchester_coding = Manchester_coding
    def Symbol_Package_communication(self):
        Symbols = self.Manchester_coding
        T_sym =  self.T_sym
        sample = {
            'Symbols': Symbols,
            'T_sym': T_sym
        }
        return(sample)
    def Symbol_element(self, idx):
        Symbols = self.Manchester_coding
        T_sym =  self.T_sym
        k = idx
        Element = Symbols[k]
        TimeStart_Symbol = T_t + (k)*T_sym
        TimeEnd_Symbol = T_t + (k+1)*T_sym
        sample = {
            'Element' : Element,
            'Info_Symbol' : [TimeStart_Symbol, TimeEnd_Symbol],
            'TimeStart_Symbol' : TimeStart_Symbol,
            'TimeEnd_Symbol' : TimeEnd_Symbol
        }
        return(sample)


def Split_frame(Symbols_status):
    Sensor_status = []
    flags = [0]
    for i,x in enumerate(Symbols_status):
        if i+1 != len(Symbols_status):
            if Symbols_status[i][2] != Symbols_status[i+1][2]:
                flags.append(i+1)
    flags.append(len(Symbols_status)+1)
    print('#########################################',flags)
    for i in range(len(flags)):
        if  i+1!= len(flags):
            brr= Symbols_status[flags[i]:flags[i+1]]   
            Sensor_status.append(brr)
    print(len(Sensor_status))
    return Sensor_status

    
# Sensor = Setup_CameraSensor(sensor_size = (1080,1920), Fps=30, T_exp=1/800, T_row=0.000001*20, T_rdout=0.000001*10)

# Setup_CameraSensor.Initilization_Sensor(Sensor)
