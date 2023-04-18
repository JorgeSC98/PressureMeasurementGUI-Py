import serial, serial.tools.list_ports
import matplotlib.pyplot as plt
from threading import Thread, Event
from tkinter import StringVar, BooleanVar, IntVar,messagebox
import time
import json 
class Comunication():
    
    def __init__(self,*args):
        super().__init__(*args)
        self.datos_recibidos = StringVar()
        self.datos_test = StringVar()
        self.test_init= BooleanVar()  # Declara variable de tipo booleana
        self.progress=IntVar()
        self.terminal_text=StringVar()
        self.terminal2_text=StringVar()
        self.arduino=serial.Serial()
        self.arduino.timeout=0.5
        self.baudrates=['9600','19200','38400','115200']
        self.puertos=[]
        self.senal_read= Event()
        self.hilo_read= None
        self.senal_protocol= Event()
        self.hilo_protocol= None
        self.Data=dict()
        self.Data_final=dict()
        
    def puertos_disponibles(self):
        self.puertos=[port.device for port in serial.tools.list_ports.comports()]
        
    def conexion_serial(self):
        try:
            self.arduino.open()
            time.sleep(.3)
        
            if (self.arduino.is_open):
                self.iniciar_hilo_read()
                self.terminal_text.set('Communication has been Established')
                self.terminal2_text.set('Connected...')
                
        except: 
            messagebox.showerror(message="Could not establish communication", title="Error")
            self.terminal_text.set('Could not establish communication, \n make sure device is connected')
            self.terminal2_text.set('Error...')
                
    def enviar_datos(self,data):
        if(self.arduino.is_open):
            self.datos_enviados= str(data)
            try:
                self.arduino.write(self.datos_enviados.encode())
            except:
                messagebox.showerror(message="An error has ocurred while sending data", title="Error")
        else:
            messagebox.showerror(message="Could not establish communication", title="Error")
            
    def leer_datos(self):
        data = self.arduino.readline().decode()
        return data
    
    def protocol_init(self,x):
        self.test_init.set(False)
        #self.iniciar_hilo_read()
        self.iniciar_hilo_protocol()
        
    def save_datos(self,name):
        if len(name)==10 or len(name)==11:   
            self.terminal2_text.set('Saving Data...')
            try:
                self.saveDictionary(self.Data,name)
                self.terminal2_text.set('Saving Data... '+name+"  Saved") 
            except: messagebox.showerror(message="The Data could not be saved", title="Data Error")
        else: 
            messagebox.showerror(message="The Data could not be saved, verify participant info", title="Data Error")
         
    def leer_datos_hilo(self):
        try:
            while(self.senal_read.isSet() and self.arduino.is_open):
                data = self.arduino.readline().decode('utf-8').strip()
                if (len(data)>1):
                    self.datos_recibidos.set(data)
        except:
            messagebox.showerror(message="An error has occured while reading data", title="Error")
            
        
    def runprotocol(self):  #Podemos enviar datos para guardar el diccionario
        while (self.test_init.get()) :
            sendiglabel= "s"
            self.progress=0;
        keys = ["sensor_0","sensor_1","sensor_2","sensor_3","sensor_4","sensor_5","sensor_6","sensor_7"]
        printfreq = 10
        sendiglabel= "s"
        duration=15
        self.Data.clear() 
                # Initate empty dictionary
        for key in keys:      # Iterate over keys
            self.Data[key]    = [] # Append an empty list to every key
        self.Data["time"] = [] # Add a data value for time 
        PythonTime  = 0                        # Set Python time to 0
        InitialTime = time.time()              # Retrive time 
        FinalTime   = InitialTime + duration   # Duration of protocol
        i = 0                                  # Variable to set printing frecuency 
        #message="Adquiring Data"
        #self.terminal_text.set("[CPU]   "  + message)            # Print inital message
        
        while PythonTime  < FinalTime : 
            PythonTime = time.time() 
            self.progress.set(int(PythonTime))
            i +=1
            if(not(self.arduino.is_open)):
                messagebox.showerror(message="An error has occured while running the protocol, verify your connection", title="Error")
                break
            try:
                #messages=self.datos_arduino.leer_datos()
                self.datos=(self.datos_recibidos.get())
                time.sleep(.02)
                if i == printfreq:
                    i = 0               # Reset i
                    #self.terminal_text.set(".",end=" ")  # Print point     
                cad   = self.datos.strip()                                        # Remove \n and \r
                position = cad.index(":")                                  # Get the index of lable/status separation
                label  = cad[:position]                                    # Get label              
                SensorValueList = cad[position+1:].split(",")              # Retrive sensor values
                if label  ==sendiglabel:
                    for key,retirvedValue in zip(keys,SensorValueList):
                        self.Data[key].append(retirvedValue)                    # Append Sensor Value 
                     
                    self.Data["time"].append(PythonTime-InitialTime)            # Append time
                                                                            #Global Variable 
            
            except :
                  messagebox.showerror(message="An error has occured while running the protocol, try again", title="Error")
                  

            pass
        self.Data_final=self.Data
        self.progress.set(0)
        self.test_init.set(True)
        #self.ani.event_source.stop()
        
   
                        #Guardar diccionario 
                #Cerrar el hilo
    
    def iniciar_hilo_read(self):
        self.hilo_read= Thread(target= self.leer_datos_hilo)
        self.hilo_read.setDaemon(1)
        self.senal_read.set()
        self.hilo_read.start()
        
    def iniciar_hilo_protocol(self):
        self.hilo_protocol= Thread(target= self.runprotocol)
       # self.hilo_protocol.setDaemon(1)
        self.senal_protocol.set()
        self.hilo_protocol.start()
    
    def stop_hilo_protocol(self):
        if (self.hilo_protocol is not None):
            self.senal_protocol.clear()
            self.hilo_protocol.join()
            self.hilo_protocol= None
        
    def stop_hilo_read(self):
        if (self.hilo_read is not None):
            self.senal_read.clear()
            self.hilo_read.join()
            self.hilo_read= None
            
    def desconectar(self):
        self.arduino.close()
        self.stop_hilo_protocol()
        self.stop_hilo_read()
        
    def saveDictionary(self,data: dict,filename:str = "dfnone") -> None:
    
    ### Handle Filename ###
        if filename == "dfnone":
            filename = "report_" + (datetime.now()).strftime("%H_%M_%S") + ".json"
        elif filename != "dfnone":
            if ".json" in filename:
                pass
            else:
                filename = filename + ".json"
            
        with open(filename, "w") as handler:
            json.dump(data,handler)
    
        #print(f"Data has been saved as {filename}")
    