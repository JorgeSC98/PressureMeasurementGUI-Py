from tkinter import Frame,Checkbutton,Entry,StringVar,PhotoImage,LabelFrame,Label,messagebox,Entry,Scale
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter.ttk import Combobox, Progressbar,Button
import serial, serial.tools.list_ports
from threading import Thread, Event
from comunication import Comunication
import time
import collections
from PIL import Image,ImageTk
from Data_Analysis import Data_Processing
import itertools
class MainFrame(Frame):
    def __init__(self,master,*args):
        super().__init__(master, *args)
        self.datos_arduino= Comunication()
        self.data_analysis=Data_Processing()
        self.datos_arduino.puertos_disponibles()
        #self.coms_list=['COM3','COM4','COM5','COM6','COM7','COM8','COM8']
        self.baud_list=['9600','11200','38400']
        self.participant_list=['1','2','3','4','5','6','7','8','9','10']
        self.socket_list=['Conventional','Digital']
        self.repetition_list=['1M1','1M2','1M3','2M1','2M2','2M3']
        self.sensor=0
        self.datos_arduino.terminal_text.set("Welcome!")
        self.datos_arduino.terminal2_text.set("Ready for the test?")
        self.participant_text=StringVar()
        self.socket_text=StringVar()
        self.repetition_text=StringVar()
        self.muestra=200
        self.datos=0.0
        self.serie=1
        
        self.fig, ax=plt.subplots(facecolor='#000000',dpi=100,figsize=(4,2))
        plt.title("Data",color='white',size=12,family='Arial')
        ax.tick_params(direction='out',length=5,width=2,colors='white',grid_color='r',grid_alpha=0.5)
        
        self.line0, =ax.plot([],[],color='m',marker='o',linewidth=2,markersize=1,markeredgecolor='r')
        self.line1, =ax.plot([],[],color='m',marker='o',linewidth=2,markersize=1,markeredgecolor='Gray')
        self.line2, =ax.plot([],[],color='m',marker='o',linewidth=2,markersize=1,markeredgecolor='White')
        self.line3, =ax.plot([],[],color='m',marker='o',linewidth=2,markersize=1,markeredgecolor='y')
        self.line4, =ax.plot([],[],color='m',marker='o',linewidth=2,markersize=1,markeredgecolor='Blue')
        self.line5, =ax.plot([],[],color='m',marker='o',linewidth=2,markersize=1,markeredgecolor='Green')
        self.line6, =ax.plot([],[],color='m',marker='o',linewidth=2,markersize=1,markeredgecolor='Orange')
        self.line7, =ax.plot([],[],color='m',marker='o',linewidth=2,markersize=1,markeredgecolor='#630A92')
        plt.xlim([0,self.muestra])
        plt.ylim([0,900])
        
        ax.set_facecolor('#6E6D7000')
        ax.spines['bottom'].set_color('blue')
        ax.spines['left'].set_color('blue')
        ax.spines['top'].set_color('blue')
        ax.spines['right'].set_color('blue')
        
        self.datos_senal_cero=collections.deque([0]*self.muestra, maxlen=self.muestra)
        self.datos_senal_one=collections.deque([0]*self.muestra, maxlen=self.muestra)
        self.datos_senal_two=collections.deque([0]*self.muestra, maxlen=self.muestra)
        self.datos_senal_three=collections.deque([0]*self.muestra, maxlen=self.muestra)
        self.datos_senal_four=collections.deque([0]*self.muestra, maxlen=self.muestra)
        self.datos_senal_five=collections.deque([0]*self.muestra, maxlen=self.muestra)
        self.datos_senal_six=collections.deque([0]*self.muestra, maxlen=self.muestra)
        self.datos_senal_seven=collections.deque([0]*self.muestra, maxlen=self.muestra)
        
        
        self.create_widgets()
        
    def animate(self,i):
        self.datos=(self.datos_arduino.datos_recibidos.get())
        #self.terminal_text.set(self.datos)
        try:
            cad   = self.datos.strip()                                        # Remove \n and \r
            position = cad.index(":")                                  # Get the index of lable/status separation
            label  = cad[:position]                                    # Get label              
            dato = cad[position+1:].split(",")              # Retrive sensor values
            dato1=float(dato[1])
            dato2=float(dato[2])
            dato3=float(dato[3])
            dato4=float(dato[4])
            dato5=float(dato[5])
            dato6=float(dato[6])
            dato7=float(dato[7])
            dato0=float(dato[0])
        except AttributeError:
            pass
        self.datos_senal_cero.append(dato0)
        self.datos_senal_one.append(dato1)
        self.datos_senal_two.append(dato2)
        self.datos_senal_three.append(dato3)
        self.datos_senal_four.append(dato4)
        self.datos_senal_five.append(dato5)
        self.datos_senal_six.append(dato6)
        self.datos_senal_seven.append(dato7)
        
        self.line0.set_data(range(self.muestra), self.datos_senal_cero)
        self.line1.set_data(range(self.muestra), self.datos_senal_one)
        self.line2.set_data(range(self.muestra), self.datos_senal_two)
        self.line3.set_data(range(self.muestra), self.datos_senal_three)
        self.line4.set_data(range(self.muestra), self.datos_senal_four)
        self.line5.set_data(range(self.muestra), self.datos_senal_five)
        self.line6.set_data(range(self.muestra), self.datos_senal_six)
        self.line7.set_data(range(self.muestra), self.datos_senal_seven)
        
    def graficar_b(self):
    
        self.ani=animation.FuncAnimation(self.fig, self.animate, frames=100, interval=100,blit=False)
        #Desactivar botones
        self.canvas.draw()
        
    def stop_graph_b(self):
        self.ani.event_source.stop()
        
    def plot_b(self):
        self.data_analysis.Plot_sensors("M15S1R1")
    def delta_b(self):
        self.data_analysis.Plot_Delta()
        
    def filter_b(self):
        self.data_analysis.roll_M()       
        
    def run_protocol_b(self):
        
        if self.serie>3:
            self.serie=1
        if self.serie % 2==0:
            messagebox.showinfo(message="Instrucion: Balance the weight on both legs Duration: 30s /n Ready?", title="Running Protocol")
            self.datos_arduino.terminal2_text.set("Balance the weight on both legs")  
        else:
            messagebox.showinfo(message="Instrucion: Stand on the prosthesis Duration: 30s /n Ready?", title="Running Protocol")
            self.datos_arduino.terminal2_text.set("Stand on the prosthesis") 
        test=self.datos_arduino.protocol_init(self.serie)
        self.datos_arduino.terminal_text.set("Running protocol")
        
        
    def save_b(self):
        participant=(self.participant_text.get())
        socket=(self.socket_text.get())
        repetition=(self.repetition_text.get())
        
        serie=str(self.serie)
        if socket=='Conventional':
            socket='1'
        else: socket='2'
        name="M"+participant+"S"+ socket+"R"+repetition+"D"+serie
        self.datos_arduino.save_datos(name)
        self.serie+=1
        
    def calibracion_b(self):
        self.datos_arduino.terminal_text.set("Initializing with Calibration...")   
        time.sleep(.1)
        #Se activan o desactivan los botones 
        self.bt_calibration.config(state='disabled')
        #Enviar C para iniciar calibracion
        self.datos_arduino.enviar_datos('c')
        time.sleep(.1)
        self.datos_arduino.terminal2_text.set('Ready to start calibration?')   
        
        
    def select_b(self):
        if (self.sensor<8):
            self.datos_arduino.stop_hilo_read()
            #self.datos_arduino.terminal_text.set('Ready to calibrate sensor '+ str(self.sensor) +"?")  
            self.datos_arduino.enviar_datos('n')
            value_pot=self.pot_value.get()
            self.datos_arduino.enviar_datos(value_pot)
            time.sleep(.5)
            self.datos_arduino.terminal_text.set('Pot of sensor '+ str(self.sensor) + ' is set to: ' +str(value_pot))
            #time.sleep(.5)
            #messages=self.datos_arduino.leer_datos()
            #messages=messages.strip()
            message=self.datos_arduino.leer_datos()
            self.datos_arduino.terminal2_text.set("Sensor " +str(self.sensor) + ' calibrate' +message)
            self.sensor+=1
        else:
            self.datos_arduino.terminal_text.set('Calibration finished')
            self.datos_arduino.iniciar_hilo_read()
            self.datos_arduino.terminal2_text.set('IPS ready to run protocol')
        
    def auto_b(self):
        if (self.sensor<8):    
            self.datos_arduino.stop_hilo_read()
            self.datos_arduino.terminal_text.set('Ready to calibrate sensor '+ str(self.sensor) +"?")  
            self.datos_arduino.enviar_datos('y')
            time.sleep(.1)
            message=self.datos_arduino.leer_datos()
            self.datos_arduino.terminal_text.set('Pot of sensor '+ str(self.sensor) + 'is set to: ' +message)
            time.sleep(.5)
            messages=self.datos_arduino.leer_datos()
            messages=messages.strip()
            self.datos_arduino.terminal2_text.set("Sensor " +str(self.sensor) + ' calibrate' +messages)
            self.sensor+=1
        else:
            self.datos_arduino.terminal_text.set('Calibration finished')
            self.datos_arduino.iniciar_hilo_read()
            self.datos_arduino.terminal2_text.set('IPS ready to run protocol')  
        
        pass
    
    def automatic_b(self):
        self.datos_arduino.stop_hilo_read()
        self.datos_arduino.enviar_datos('y')
        self.datos_arduino.terminal_text.set('Wait for Calibration')
        time.sleep(6)
        message=self.datos_arduino.leer_datos()
        self.datos_arduino.terminal2_text.set('Calibrate' +message)
        
        self.datos_arduino.terminal_text.set('Calibration finished')
        self.datos_arduino.iniciar_hilo_read()
        self.datos_arduino.terminal2_text.set('IPS ready to run protocol')
        
    def desconectar_b(self):
        #Se activan o desactivan los botones 
        self.bt_conectar.config(state='normal')
        #Se cierra comunicacion
        try:
            self.any.event_source.stop()
        except AttributeError:
            pass
        self.datos_arduino.terminal_text.set('Establishing Serial communication with microcontroller...')
        self.datos_arduino.desconectar
        self.datos_arduino.terminal2_text.set("Disconected")
        pass   
    def conectar_b(self):
        self.datos_arduino.terminal_text.set('Establishing Serial communication with microcontroller...')
        self.bt_calibration.config(state='Enabled')
        #Se activan o desactivan los botones 
        #self.bt_conectar.config(state='disabled')
        #Se inicia comunicacion
        
        self.datos_arduino.arduino.port=self.coms.get()
        if len(self.datos_arduino.arduino.port)==4 or len(self.datos_arduino.arduino.port)==5:
            self.datos_arduino.arduino.baudrate=self.baud.get()

            self.datos_arduino.conexion_serial()
        else:
            messagebox.showerror(message="COM port not selected", title="Error")
    
   
    
    
        
        
    def create_widgets(self):
        frame= Frame(self.master,bg='#193E5D',bd=2)
        frame.grid(column=0,columnspan=2,row=0,sticky='nsew')        
        frame1= Frame(self.master,bg='#193E5D')
        frame1.grid(column=2,row=0,sticky='nsew')
        frame4= Frame(self.master,bg='#193E5D')
        frame4.grid(column=0,row=1,sticky='nsew')
        frame2= Frame(self.master,bg='#193E5D')
        frame2.grid(column=1,row=1,sticky='nsew')
        frame3= Frame(self.master,bg='#193E5D')
        frame3.grid(column=2,row=1,sticky='nsew')
        terminal_frame = LabelFrame(self.master, padx=100, pady=10,bg='Black',font='White')
        terminal_frame.grid(row=1, column=0,padx=5,pady=1)
        terminal_frame.place(x=20,y=500)

        
        self.master.columnconfigure(0,weight=1)
        self.master.columnconfigure(1,weight=1)
        self.master.columnconfigure(2,weight=1)
        self.master.rowconfigure(0,weight=5)
        self.master.rowconfigure(1,weight=1)
        
        self.canvas=FigureCanvasTkAgg(self.fig,master=frame)
        self.canvas.get_tk_widget().pack(padx=1,pady=0,expand=True,fill='both')
        
        ports=self.datos_arduino.puertos
          
        #Label(frame4,text='Terminal:').pack(padx=4,expand=1)
        self.terminal_label=Label(terminal_frame,textvariable=self.datos_arduino.terminal_text,bg='Black',fg="White")
        self.terminal_label.pack(pady=5,expand=1)
        self.terminal2_label=Label(terminal_frame,textvariable=self.datos_arduino.terminal2_text,bg='Black',fg="White")
        self.terminal2_label.pack(pady=5,expand=1)
        Label(frame1,text='COM:').place(x=170,y=75)
        self.coms=Combobox(frame1,values=ports,state='readonly')
        #self.coms.current(4)
        self.coms.place(x=140,y=100)
        Label(frame1,text='BaudRate:').place(x=340,y=75)
        self.baud=Combobox(frame1,values=self.baud_list,state='readonly')
        self.baud.current(0)
        self.baud.place(x=310,y=100)
        self.bt_conectar=Button(frame1, text='Conect', command=self.conectar_b)
        self.bt_conectar.place(x=30,y=85)
        self.bt_desconectar=Button(frame1, text='Disconect', command=self.desconectar_b)
        self.bt_desconectar.place(x=240,y=125)
        self.bt_calibration=Button(frame1, text='Calibration', command=self.calibracion_b)
        self.bt_calibration.place(x=30,y=240)
        
        #self.bt_next=Button(frame1, text='Next Calibration', command=self.next_b)
        #self.bt_next.pack(padx=4,expand=1)

        self.bt_runprotocol=Button(frame1, text='Run Protocol', command=self.run_protocol_b)
        self.bt_runprotocol.place(x=30,y=370)
        self.bt_graficar=Button(frame1, text='Graph', command=self.graficar_b)
        self.bt_graficar.place(x=160,y=330)
        self.bt_stop=Button(frame1, text='Stop', command=self.stop_graph_b)
        self.bt_stop.place(x=240,y=330)
        self.bt_savedata=Button(frame2, text='Save Data', command=self.save_b)
        self.bt_savedata.place(x=100,y=10)
        self.bt_desconectar=Button(frame1, text='Disconect', command=self.desconectar_b)
        #self.bt_desconectar.pack(padx=4,expand=1)
        self.bt_select=Button(frame1, text='Select Pot Value', command=self.select_b)
        self.bt_select.place(x=165,y=210)
        self.pot_value=Scale(frame1,to=100,from_=1,orient='horizontal')
        self.pot_value.place(x=160,y=240)
        self.bt_auto=Button(frame1, text='Automatic Calibration', command=self.automatic_b)
        self.bt_auto.place(x=310,y=240)
        Label(frame2,text='Participant No.:').place(x=200,y=50)
        #self.participant=Combobox(frame2,values=self.participant_list,state='readonly',textvariable=self.participant_text,width=10)
        self.participant=Entry(frame2,textvariable=self.participant_text)
        self.participant.place(x=200,y=75)
        Label(frame2,text='Type of Socket:').place(x=150,y=115)
        self.socket=Combobox(frame2,values=self.socket_list,state='readonly',textvariable=self.socket_text,width=13)
        self.socket.place(x=140,y=140)
        Label(frame2,text='Repetition No.:').place(x=255,y=115)
        self.repetition=Combobox(frame2,values=self.repetition_list,state='readonly',textvariable=self.repetition_text,width=10)
        self.repetition.place(x=255,y=140)
        self.bt_plot=Button(frame1, text='Plot', command=self.plot_b)
        self.bt_plot.place(x=230,y=410)
        self.bt_filter=Button(frame1, text='Filter', command=self.filter_b)
        self.bt_filter.place(x=150,y=410)
        self.bt_filter=Button(frame1, text='Delta', command=self.delta_b)
        self.bt_filter.place(x=310,y=410)
        
        self.progress_bar=Progressbar(frame1,orient='horizontal',length=200, variable=self.datos_arduino.progress, maximum=200)
        self.progress_bar.place(x=150,y=370)
        
        logo=(Image.open('logo.png'))
        resized_image= logo.resize((320,150), Image.ANTIALIAS)
        self.new_image= ImageTk.PhotoImage(resized_image)
        self.image=Label(frame3, image=self.new_image)
        self.image.pack()
        