import matplotlib.pyplot as plt
import numpy as np
import json
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import statistics
from collections import Counter 
from tkinter.filedialog import askopenfilenames
import itertools
class Data_Processing():
    def __init__(self,*args):
        super().__init__(*args)
        pass
    
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
    
    def auto_label2(self,grupos,spacing=5):
        for i in grupos:
            y_value = i.get_height()
            x_value = i.get_x() + i.get_width() / 2
            space = spacing
            va = 'bottom'
            if y_value < 0:
                space =space * (-1)
                va = 'top'
            label = "{}".format(y_value)
            axx1.annotate(
                label,                      # Use `label` as label
                (x_value, y_value),         # Place label at end of the bar
                xytext=(0, space),          # Vertically shift label by `space`
                textcoords="offset points", # Interpret `xytext` as offset in points
                ha='center',                # Horizontally center label
                size=15,
                va=va)                      # Vertically align label differently for
                                        # positive and negative values. 
                
    def auto_label(self,grupos,spacing=5):
        for i in grupos:
            y_value = i.get_height()
            x_value = i.get_x() + i.get_width() / 2
            space = spacing
            va = 'bottom'
            if y_value < 0:
                space =space * (-1)
                va = 'top'
            label = "{}".format(y_value)
            axx.annotate(
                label,                      # Use `label` as label
                (x_value, y_value),         # Place label at end of the bar
                xytext=(0, space),          # Vertically shift label by `space`
                textcoords="offset points", # Interpret `xytext` as offset in points
                ha='center',                # Horizontally center label
                size=15,
                va=va)                      # Vertically align label differently for
                                        # positive and negative values.
                
    def Plot_sensors(self,Prueba):
        #df = pd.read_csv ('M15S1R1M1')
        #Prueba="M10S1R1"
        file_names_tuple = askopenfilenames()
        file_names=list(file_names_tuple)
        file_names_m=[]
        m1=file_names[0]
        m2=file_names[4]
        m3=file_names[8]
        file_names_m.append(m1)
        file_names_m.append(m2)
        file_names_m.append(m3)
        del file_names[0]
        del file_names[3]
        del file_names[6]
        Participant=m1[-14:-5]
        if Participant[0]=="M":
            socket=Participant[4]
            Participant=Participant[1:3]
        else:
            socket=Participant[4]
            Participant=Participant[2]

            
        S0={}
        S1={}
        S2={}
        S3={}
        S4={}
        S5={}
        mean0=[]
        mean1=[]
        mean2=[]
        mean3=[]
        mean4=[]
        mean5=[]
        ys0d1=[]
        ys0d2=[]
        ys0d3=[]
        proms0=[]
        ys1d1=[]
        ys1d2=[]
        ys1d3=[]
        proms1=[]
        ys2d1=[]
        ys2d2=[]
        ys2d3=[]
        proms2=[]
        ys3d1=[]
        ys3d2=[]
        ys3d3=[]
        proms3=[]
        ys4d1=[]
        ys4d2=[]
        ys4d3=[]
        proms4=[]
        ys5d1=[]
        ys5d2=[]
        ys5d3=[]
        proms5=[]
        Time={}
        time0list=[]
        time1list=[]
        time2list=[]
        time3list=[]
        time4list=[]
        time5list=[]
        datoss0d=[]
        datoss1d=[]
        datoss2d=[]
        datoss3d=[]
        datoss4d=[]
        datoss5d=[]
        SD=[]
        index=-1
        index2=-1
        for j in range(1,4,1):
            suma=0
            for i in range(1,4,1):
                #Prompt=Prueba+"M"+ str(i) + "D" + str(j)+".json"
                if i==1:
                    index=-1+j
                elif i==2:
                    index=2+j
                elif i==3:
                    index=5+j
                name=str(file_names[index])
                data=pd.read_json (name)
                S0[i,j]=(data['sensor_0'])
                S1[i,j]=(data['sensor_1'])
                S2[i,j]=(data['sensor_2'])
                S3[i,j]=(data['sensor_3'])
                S4[i,j]=(data['sensor_4'])
                S5[i,j]=(data['sensor_5'])
                Time[i,j]=(data['time'])

                consultas0=S0[i,j]
                myListS0 = consultas0.items()
                x, s0 = zip(*myListS0)
                means0 =statistics.mean(s0)
                mean0.append(means0)
                datoss0d.append(s0)
                ys0=len(s0)

                consultas1=S1[i,j]
                myListS1 = consultas1.items()
                x, s1 = zip(*myListS1)
                means1 = statistics.mean(s1)
                mean1.append(means1)
                datoss1d.append(s1)
                ys1=len(s1)

                consultas2=S2[i,j]
                myListS2 = consultas2.items()
                x, s2 = zip(*myListS2)
                means2 = statistics.mean(s2)
                mean2.append(means2)
                datoss2d.append(s2)
                ys2=len(s2)

                consultas3=S3[i,j]
                myListS3 = consultas3.items()
                x, s3 = zip(*myListS3)
                means3 = statistics.mean(s3)
                mean3.append(means3)
                datoss3d.append(s3)
                ys3=len(s3)

                consultas4=S4[i,j]
                myListS4 = consultas4.items()
                x, s4 = zip(*myListS4)
                means4 = statistics.mean(s4)
                mean4.append(means4)
                datoss4d.append(s4)
                ys4=len(s4)

                consultas5=S5[i,j]
                myListS5 = consultas5.items()
                x, s5 = zip(*myListS5)
                means5 = statistics.mean(s5)
                mean5.append(means5)
                datoss5d.append(s5)
                ys5=len(s5)
                      


        s0d1=statistics.mean(mean0[0:3])
        st_dev_s0 = statistics.stdev(itertools.chain(*datoss0d[0:3]))
        #print("La desviación estándar de S0 es " + str(st_dev_s0))
        SD.append(st_dev_s0)
        s0d2=statistics.mean(mean0[3:6])
        s0d3=statistics.mean(mean0[6:9])

        s1d1=statistics.mean(mean1[0:3])
        st_dev_s1 = statistics.stdev(itertools.chain(*datoss1d[0:3]))
        #print("La desviación estándar de S1 es " + str(st_dev_s1))
        SD.append(st_dev_s1)
        s1d2=statistics.mean(mean1[3:6])
        s1d3=statistics.mean(mean1[6:9])

        s2d1=statistics.mean(mean2[0:3])
        st_dev_s2 = statistics.stdev(itertools.chain(*datoss2d[0:3]))
        #print("La desviación estándar de S2 es " + str(st_dev_s2))
        SD.append(st_dev_s2)
        s2d2=statistics.mean(mean2[3:6])
        s2d3=statistics.mean(mean2[6:9])

        s3d1=statistics.mean(mean3[0:3])
        st_dev_s3 = statistics.stdev(itertools.chain(*datoss3d[0:3]))
        #print("La desviación estándar de S3 es " + str(st_dev_s3))
        SD.append(st_dev_s3)
        s3d2=statistics.mean(mean3[3:6])
        s3d3=statistics.mean(mean3[6:9])

        s4d1=statistics.mean(mean4[0:3])
        st_dev_s4 = statistics.stdev(itertools.chain(*datoss4d[0:3]))
        #print("La desviación estándar de S4 es " + str(st_dev_s4))
        SD.append(st_dev_s4)
        s4d2=statistics.mean(mean4[3:6])
        s4d3=statistics.mean(mean4[6:9])

        s5d1=statistics.mean(mean5[0:3])
        st_dev_s5 = statistics.stdev(itertools.chain(*datoss5d[0:3]))
        #print("La desviación estándar de S5 es " + str(st_dev_s5))
        SD.append(st_dev_s5)
        s5d2=statistics.mean(mean5[3:6])
        s5d3=statistics.mean(mean5[6:9])

        data = pd.DataFrame({s0d1,s1d1,s2d1,s3d1,s4d1,s5d1}, index=('PT', 'FH','AMT','ADT','PPW','PDW'))
        total = data.sum(axis=1)
        
        fig, axx = plt.subplots()
        
        axx.set_title("Means and standard deviation M"+Participant +"S"+socket+".pdf", size=15)
        colorbars = ['darkred', 'dimgray', 'silver', 'goldenrod', 'steelblue',
                            'forestgreen']
        axx.bar(total.index, total, yerr = SD, error_kw = {'ecolor' : '0.2', 'capsize' :6}, alpha=0.7, label = 'First', color = colorbars) 
        axx.set_ylabel('Bits',size=20)
        plt.savefig("Sensors_stdev_M"+Participant +"S"+socket+".pdf")
        #plt.show()

        xs0d1=np.ones(ys0)
        ys0d1=s0d1*xs0d1
        proms0.extend(ys0d1)
        xs0d2=np.ones(ys0)
        ys0d2=s0d2*xs0d2
        proms0.extend(ys0d2)
        xs0d3=np.ones(ys0)
        ys0d3=s0d3*xs0d3
        proms0.extend(ys0d3)
        time0=0
        for m in range(0,len(proms0),1):
            time0=time0+(90/(len(proms0)))
            time0list.append(time0)
            m+=1


        xs1d1=np.ones(ys1)
        ys1d1=s1d1*xs1d1
        proms1.extend(ys1d1)
        xs1d2=np.ones(ys1)
        ys1d2=s1d2*xs1d2
        proms1.extend(ys1d2)
        xs1d3=np.ones(ys1)
        ys1d3=s1d3*xs1d3
        proms1.extend(ys1d3)
        time1=0
        for m in range(0,len(proms1),1):
            time1=time1+(90/(len(proms1)))
            time1list.append(time1)
            m+=1

        xs2d1=np.ones(ys2)
        ys2d1=s2d1*xs2d1
        proms2.extend(ys2d1)
        xs2d2=np.ones(ys2)
        ys2d2=s2d2*xs2d2
        proms2.extend(ys2d2)
        xs2d3=np.ones(ys2)
        ys2d3=s2d3*xs2d3
        proms2.extend(ys2d3)
        time2=0
        for m in range(0,len(proms2),1):
            time2=time2+(90/(len(proms2)))
            time2list.append(time2)
            m+=1

        xs3d1=np.ones(ys3)
        ys3d1=s3d1*xs3d1
        proms3.extend(ys3d1)
        xs3d2=np.ones(ys3)
        ys3d2=s3d2*xs3d2
        proms3.extend(ys3d2)
        xs3d3=np.ones(ys3)
        ys3d3=s3d3*xs3d3
        proms3.extend(ys3d3)
        time3=0
        for m in range(0,len(proms3),1):
            time3=time3+(90/(len(proms3)))
            time3list.append(time3)
            m+=1

        xs4d1=np.ones(ys4)
        ys4d1=s4d1*xs4d1
        proms4.extend(ys4d1)
        xs4d2=np.ones(ys4)
        ys4d2=s4d2*xs4d2
        proms4.extend(ys4d2)
        xs4d3=np.ones(ys4)
        ys4d3=s4d3*xs4d3
        proms4.extend(ys4d3)
        time4=0
        for m in range(0,len(proms4),1):
            time4=time4+(90/(len(proms4)))
            time4list.append(time4)
            m+=1

        xs5d1=np.ones(ys5)
        ys5d1=s5d1*xs5d1
        proms5.extend(ys5d1)
        xs5d2=np.ones(ys5)
        ys5d2=s5d2*xs5d2
        proms5.extend(ys5d2)
        xs5d3=np.ones(ys5)
        ys5d3=s5d3*xs5d3
        proms5.extend(ys5d3)
        time5=0
        for m in range(0,len(proms5),1):
            time5=time5+(90/(len(proms5)))
            time5list.append(time5)
            m+=1

        fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(nrows=2, ncols=3,
                                    figsize=(20,10))
        for i in range(1,4,1):
            index2=index2+1
            name=str(file_names_m[index2])
            data=pd.read_json(name)
            time0=data['time']
            ax1.plot(data['time'],data['sensor_0'],label ="M"+ str(i))  
            ax1.legend(loc = "lower right") 
            ax1.set_ylabel('Bits')
            ax1.set_title('Patellar tendon'+ " "+"M"+Participant+"S"+socket+"R1",size=15)
            ax2.plot(data['time'],data['sensor_1'],label ="M"+ str(i)) 
            ax2.legend(loc = "lower right")
            ax2.set_ylabel('Bits')
            ax2.set_title('Fibular head'+ " "+"M"+Participant+"S"+socket+"R1",size=15)
            ax3.plot(data['time'],data['sensor_2'],label ="M"+ str(i)) 
            ax3.legend(loc = "lower right")
            ax3.set_ylabel('Bits')
            ax3.set_title('Anterior mid tibia'+ " "+"M"+Participant+"S"+socket+"R1",size=15)
            ax4.plot(data['time'],data['sensor_3'],label ="M"+ str(i)) 
            ax4.legend(loc = "lower right")
            ax4.set_ylabel('Bits')
            ax4.set_title('Anterior distal tibia'+ " "+"M"+Participant+"S"+socket+"R1",size=15)
            ax5.plot(data['time'],data['sensor_4'],label ="M"+ str(i)) 
            ax5.legend(loc = "lower right")
            ax5.set_ylabel('Bits')
            ax5.set_title('Posterior proximal wall'+ " "+"M"+Participant+"S"+socket+"R1",size=15)
            ax6.plot(data['time'],data['sensor_5'],label ="M"+ str(i)) 
            ax6.legend(loc = "lower right")
            ax6.set_ylabel('Bits')
            ax6.set_title('Posterior distal wall'+ " "+"M"+Participant+"S"+socket+"R1",size=15)
       
        ax1.plot(time0list, proms0,label ="Mean") 
        ax1.legend(loc = "lower right")
        ax1.set_xlabel('Time(s)')
        ax2.plot(time1list,proms1,label ="Mean") 
        ax2.legend(loc = "lower right")
        ax2.set_xlabel('Time(s)')
        ax3.plot(time2list,proms2,label ="Mean")
        ax3.legend(loc = "lower right")
        ax3.set_xlabel('Time(s)')
        ax4.plot(time3list,proms3,label ="Mean")
        ax4.legend(loc = "lower right")
        ax4.set_xlabel('Time(s)')
        ax5.plot(time4list,proms4,label ="Mean")
        ax5.legend(loc = "lower right")
        ax5.set_xlabel('Time(s)')
        ax6.plot(time5list,proms5,label ="Mean") 
        ax6.legend(loc = "lower right")
        ax6.set_xlabel('time (s) \n *Note: Vertical axes are scaled and translated according to data')

        plt.savefig("Sensors_plot M"+Participant +"S"+socket+".pdf") 
        maximum0=max(s0d1,s0d3)
        maximum1=max(s1d1,s1d3)
        maximum2=max(s2d1,s2d3)
        maximum3=max(s3d1,s3d3)
        maximum4=max(s4d1,s4d3)
        maximum5=max(s5d1,s5d3)

        d1_d3 = {'Maximos':[maximum0, maximum1, maximum2, maximum3, maximum4, maximum5]}
        df = pd.DataFrame(d1_d3,columns=['Maximos'])
        df.to_csv("d1d3_M"+Participant +"S"+socket+".csv")

        d2={'Valores':[s0d2,s1d2,s2d2,s3d2,s4d2,s5d2]}
        df2 = pd.DataFrame(d2,columns=['Valores'])
        df2.to_csv("d2_M"+Participant +"S"+socket+".csv")
        
    def Plot_Delta(self):  
        Participant="M6"
        file_names_tuple = askopenfilenames()
        file_names=list(file_names_tuple)
        m1=file_names[0]
        Participant=m1[-11:-6]
        print(Participant)
        if Participant[0]=="M":
            socket=Participant[4]
            Participant=Participant[1:3]
        else:
            socket=Participant[4]
            Participant=Participant[2]
    
    
        arrayDelta=[]
        leers1=pd.read_csv(file_names[0])
        array1=np.array(leers1)
        leers2=pd.read_csv(file_names[1])
        array2=np.array(leers2)
        arrayDelta2=[]
        leers3=pd.read_csv(file_names[2])
        array3=np.array(leers3)
        leers4=pd.read_csv(file_names[3])
        array4=np.array(leers4)
        x=['PT', 'FH','AMT','ADT','PPW','PDW']
        for i in range (0,6,1):
            Delta=array1[i,1]-array2[i,1]
            Delta=int(round(Delta,0))
            arrayDelta.append(Delta)
            Delta2=array3[i,1]-array4[i,1]
            Delta2=int(round(Delta2,0))
            arrayDelta2.append(Delta2)

        fig, (axx, axx1) = plt.subplots(nrows=1, ncols=2, figsize=(20,10) )   
        a=axx.bar(x,arrayDelta, color=['darkred', 'dimgray', 'silver', 'goldenrod', 'steelblue',
                            'forestgreen'])
        axx.set_title("Delta bar in prosthesis", size=25)
        axx.set_ylabel("Bits")
        axx.yaxis.label.set_size(20)
        axx.tick_params(axis='x', labelsize=14)
        axx.tick_params(axis='y', labelsize=15)
        for i in a:
            y_value = i.get_height()
            x_value = i.get_x() + i.get_width() / 2
            space = 5
            va = 'bottom'
            if y_value < 0:
                space =space * (-1)
                va = 'top'
            label = "{}".format(y_value)
            axx.annotate(
                label,                      # Use `label` as label
                (x_value, y_value),         # Place label at end of the bar
                xytext=(0, space),          # Vertically shift label by `space`
                textcoords="offset points", # Interpret `xytext` as offset in points
                ha='center',                # Horizontally center label
                size=15,
                va=va)                      # Vertically align label differently for
                                        # positive and negative values.

        a1=axx1.bar(x,arrayDelta2, color=['darkred', 'dimgray', 'silver', 'goldenrod', 'steelblue',
                            'forestgreen'])
        axx1.set_title("Delta bar in balanced weight", size=25)
        axx1.set_ylabel("Bits")
        axx1.yaxis.label.set_size(20)
        axx1.tick_params(axis='x', labelsize=14)
        axx1.tick_params(axis='y', labelsize=15)
        for i in a1:
            y_value = i.get_height()
            x_value = i.get_x() + i.get_width() / 2
            space = 5
            va = 'bottom'
            if y_value < 0:
                space =space * (-1)
                va = 'top'
            label = "{}".format(y_value)
            axx1.annotate(
                label,                      # Use `label` as label
                (x_value, y_value),         # Place label at end of the bar
                xytext=(0, space),          # Vertically shift label by `space`
                textcoords="offset points", # Interpret `xytext` as offset in points
                ha='center',                # Horizontally center label
                size=15,
                va=va)                      # Vertically align label differently for
                                        # positive and negative values. 
        plt.savefig("SensorsDeltaBar_M"+str(Participant)+".pdf") 
        
        
    def roll_M(self):
        roll=15
        data=pd.DataFrame()
        file_names_tuple = askopenfilenames()
        file_names=list(file_names_tuple)
        m1=file_names[0]
        index=-1
        index2=-1
        for y in range(1,4,1):
            for x in range(1,4,1):
                data=pd.DataFrame()
                #fullname= name+str(y)+'D'+str(x)+'.json'
                index=index+1
                name=str(file_names[index])
                Participant=name[-16:-5]
                if Participant[0]!="M":
                    Participant=Participant[1:]
                data1=pd.read_json(name)
                data['sensor_0']=data1[['sensor_0']]
                data['sensor_1']=data1[['sensor_1']]
                data['sensor_2']=data1[['sensor_2']]
                data['sensor_3']=data1[['sensor_3']]
                data['sensor_4']=data1[['sensor_4']]
                data['sensor_5']=data1[['sensor_5']]
                data['time']=data1[['time']]
                data=data.dropna()
                data['sensor_0']=data['sensor_0'].rolling(roll).mean()
                data['sensor_1']=data['sensor_1'].rolling(roll).mean()
                data['sensor_2']=data['sensor_2'].rolling(roll).mean()
                data['sensor_3']=data['sensor_3'].rolling(roll).mean()
                data['sensor_4']=data['sensor_4'].rolling(roll).mean()
                data['sensor_5']=data['sensor_5'].rolling(roll).mean()
                data['sensor_0']=pd.Series([round(val,0) for val in  data['sensor_0']])
                data['sensor_1']=pd.Series([round(val,0) for val in  data['sensor_1']])
                data['sensor_2']=pd.Series([round(val,0) for val in  data['sensor_2']])
                data['sensor_3']=pd.Series([round(val,0) for val in  data['sensor_3']])
                data['sensor_4']=pd.Series([round(val,0) for val in  data['sensor_4']])
                data['sensor_5']=pd.Series([round(val,0) for val in  data['sensor_5']])
                data=data.dropna()
                data['sensor_0'] = data['sensor_0'].astype(str)
                data['sensor_1'] = data['sensor_1'].astype(str)
                data['sensor_2'] = data['sensor_2'].astype(str)
                data['sensor_3'] = data['sensor_3'].astype(str)
                data['sensor_4'] = data['sensor_4'].astype(str)
                data['sensor_5'] = data['sensor_5'].astype(str)
                data.reset_index(drop=True,inplace=True)
                data['time']=data1[['time']]
                lista0=data['sensor_0'].values.tolist()
                lista1=data['sensor_1'].values.tolist()
                lista2=data['sensor_2'].values.tolist()
                lista3=data['sensor_3'].values.tolist()
                lista4=data['sensor_4'].values.tolist()
                lista5=data['sensor_5'].values.tolist()
                lista6=data['time'].values.tolist()
                dic={'sensor_0':lista0,'sensor_1':lista1,'sensor_2':lista2,'sensor_3':lista3,'sensor_4':lista4,'sensor_5':lista5,'time':lista6}
                self.saveDictionary(dic,Participant+".json")
        for y in range(1,4,1):
            data=pd.DataFrame()
            index2=index2+1
            name=str(file_names[index2])
            Participant=name[-16:-8]
            if Participant[0]!="M":
                Participant=Participant[1:]
            data1=pd.read_json (name)
            index2=index2+1
            name=str(file_names[index2])
            data2=pd.read_json (name)
            data2['time']=data2[['time']]+30
            index2=index2+1
            name=str(file_names[index2])
            data3=pd.read_json (name)
            data3['time']=data3[['time']]+60
            data=data1.append(data2)
            data.reset_index(drop=True,inplace=True)
            data=data.append(data3)
            data.reset_index(drop=True,inplace=True)
            data['sensor_0']=pd.Series([round(val,0) for val in  data['sensor_0']])
            data['sensor_1']=pd.Series([round(val,0) for val in  data['sensor_1']])
            data['sensor_2']=pd.Series([round(val,0) for val in  data['sensor_2']])
            data['sensor_3']=pd.Series([round(val,0) for val in  data['sensor_3']])
            data['sensor_4']=pd.Series([round(val,0) for val in  data['sensor_4']])
            data['sensor_5']=pd.Series([round(val,0) for val in  data['sensor_5']])
            data=data.dropna()
            data['sensor_0'] = data['sensor_0'].astype(str)
            data['sensor_1'] = data['sensor_1'].astype(str)
            data['sensor_2'] = data['sensor_2'].astype(str)
            data['sensor_3'] = data['sensor_3'].astype(str)
            data['sensor_4'] = data['sensor_4'].astype(str)
            data['sensor_5'] = data['sensor_5'].astype(str)
            lista0=data['sensor_0'].values.tolist()
            lista1=data['sensor_1'].values.tolist()
            lista2=data['sensor_2'].values.tolist()
            lista3=data['sensor_3'].values.tolist()
            lista4=data['sensor_4'].values.tolist()
            lista5=data['sensor_5'].values.tolist()
            lista6=data['time'].values.tolist()
            dic={'sensor_0':lista0,'sensor_1':lista1,'sensor_2':lista2,'sensor_3':lista3,'sensor_4':lista4,'sensor_5':lista5,'time':lista6}
            self.saveDictionary(dic,Participant+str(y)+".json") 
            

         
                
                
    