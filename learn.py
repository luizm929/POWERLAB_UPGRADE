
import serial

# Debuggin purposes
#import tkinter
#--------------------



import serial.tools.list_ports

# devices=list(serial.tools.list_ports.comports())
# for p in devices:
#     if "Arduino" or "Uno" in p:
#         Arduino=p
# arduinoData=serial.Serial(Arduino.device,9600,timeout=.1)



#while (1==1):
#  if (arduinoData.inWaiting()>0):
#      myData = arduinoData.readline()
#      print (myData)

# Debuggin purposes
#relay_control_window = tkinter.Tk()
#---------------------------------

def OFF_all_Relays():
    arduinoData.write(b'x')

def ON_all_Relays():
    arduinoData.write(b'z')

def ON_Relay0():
    arduinoData.write(b'1')
def ON_Relay1():
    arduinoData.write(b'2')
def ON_Relay2():
    arduinoData.write(b'3')
def ON_Relay3():
    arduinoData.write(b'4')
def ON_Relay4():
    arduinoData.write(b'5')
def ON_Relay5():
    arduinoData.write(b'6')
def ON_Relay6():
    arduinoData.write(b'7')
def ON_Relay7():
    arduinoData.write(b'8')
def ON_Relay8():
    arduinoData.write(b'9')
def OFF_Relay0():
    arduinoData.write(b'a')
def OFF_Relay1():
    arduinoData.write(b'b')
def OFF_Relay2():
    arduinoData.write(b'c')
def OFF_Relay3():
    arduinoData.write(b'd')
def OFF_Relay4():
    arduinoData.write(b'e')
def OFF_Relay5():
    arduinoData.write(b'f')
def OFF_Relay6():
    arduinoData.write(b'g')
def OFF_Relay7():
    arduinoData.write(b'h')
def OFF_Relay8():
    arduinoData.write(b'i')

#------------------------------------------------------------------------------------------
''' Debuggin purposes: Creates a simple GUI with buttons to test functionality.
  the actual GUI is written in PyQt5.'''
# btnoff = tkinter.Button (relay_control_window,text="Turn all relays off",command=OFF_all_Relays )
# btnoff.pack()
# btnon = tkinter.Button (relay_control_window,text="Turn all relays on",command= ON_all_Relays)
# btnon.pack()
#
#
# btnon1 = tkinter.Button (relay_control_window,text="Turn On RELAY0",command= ON_Relay0)
# btnon1.pack()
# btnon2 = tkinter.Button (relay_control_window,text="Turn On RELAY1",command= ON_Relay1)
# btnon2.pack()
# btnon3 = tkinter.Button (relay_control_window,text="Turn On RELAY2",command= ON_Relay2)
# btnon3.pack()
# btnon4 = tkinter.Button (relay_control_window,text="Turn On RELAY3",command= ON_Relay3)
# btnon4.pack()
# btnon5 = tkinter.Button (relay_control_window,text="Turn On RELAY4",command= ON_Relay4)
# btnon5.pack()
# btnon6 = tkinter.Button (relay_control_window,text="Turn On RELAY5",command= ON_Relay5)
# btnon6.pack()
# btnon7 = tkinter.Button (relay_control_window,text="Turn On RELAY6",command= ON_Relay6)
# btnon7.pack()
# btnon8 = tkinter.Button (relay_control_window,text="Turn On RELAY7",command= ON_Relay7)
# btnon8.pack()
# btnon9 = tkinter.Button (relay_control_window,text="Turn On RELAY8",command= ON_Relay8)
# btnon9.pack()
#
# btnon1 = tkinter.Button (relay_control_window,text="Turn OFF RELAY0",command= OFF_Relay0)
# btnon1.pack()
# btnon2 = tkinter.Button (relay_control_window,text="Turn OFF RELAY1",command= OFF_Relay1)
# btnon2.pack()
# btnon3 = tkinter.Button (relay_control_window,text="Turn OFF RELAY2",command= OFF_Relay2)
# btnon3.pack()
# btnon4 = tkinter.Button (relay_control_window,text="Turn OFF RELAY3",command= OFF_Relay3)
# btnon4.pack()
# btnon5 = tkinter.Button (relay_control_window,text="Turn OFF RELAY4",command= OFF_Relay4)
# btnon5.pack()
# btnon6 = tkinter.Button (relay_control_window,text="Turn OFF RELAY5",command= OFF_Relay5)
# btnon6.pack()
# btnon7 = tkinter.Button (relay_control_window,text="Turn OFF RELAY6",command= OFF_Relay6)
# btnon7.pack()
# btnon8 = tkinter.Button (relay_control_window,text="Turn OFF RELAY7",command= OFF_Relay7)
# btnon8.pack()
# btnon9 = tkinter.Button (relay_control_window,text="Turn OFF RELAY8",command= OFF_Relay8)
# btnon9.pack()
#
# relay_control_window.mainloop()
#-----------------------------------------------------------------------------------------