from tkinter import * 
#Importar libreria matplotlib para mostrar gráficos de la contabilizacion de predicción
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from pandas import DataFrame

root = Tk()
#root.configure(background='black')
root.geometry('500x400')
root.title("Formulario Proyecto final")

framecontenedor = Frame(width="700", height="130", bg="#284469")
framecontenedor.pack(side="top", anchor='n', padx=1, pady=1)
#yanezj25@hotmail.com

A = 0
B = 0
C = 0

def procesar():
	global A
	global B
	global C
	
	x1 = entry_clasea.get()
	x2 = entry_claseb.get()
	x3 = entry_clasec.get()

	A = int(int(x1) + A)
	B = int(int(x2) + B)
	C = int(int(x3) + C)
	
	actualizarGraficoBarras();

def actualizarGraficoBarras():
	global A
	global B
	global C
	
	global barras
	barras.clear()
	#crear dataframe
	Data1 = {'Animales': ['A','B','C'], 'Cantidad': [A, B, C]}
	df1 = DataFrame(Data1, columns= ['Animales', 'Cantidad'])
	df1 = df1[['Animales', 'Cantidad']].groupby('Animales').sum()
	#Agregar data al grafico de barras	
	df1.plot(kind='bar', legend=True, ax=barras)
	barras.set_title('Zoologico')
	bar1.draw()


#-------- Sección Número 1
label_clasea = Label(framecontenedor, text="Leones(A):",width=20,font=("bold", 10),fg="#ffffff", bg="#284469")
label_clasea.place(x=20,y=8)

entry_clasea = Entry(framecontenedor)
entry_clasea.place(x=140,y=10)

#-------- Sección Número 2
label_claseb = Label(framecontenedor, text="Tortugas(B):",width=20,font=("bold", 10),fg="#ffffff", bg="#284469")
label_claseb.place(x=20,y=40)

entry_claseb = Entry(framecontenedor)
entry_claseb.place(x=140,y=40)

#-------- Sección Número 3
label_clasec = Label(framecontenedor, text="Osos(C):",width=20,font=("bold", 10),fg="#ffffff", bg="#284469")
label_clasec.place(x=20,y=66)

entry_clasec = Entry(framecontenedor)
entry_clasec.place(x=140,y=70)

#------- Sección Botón
Button(framecontenedor, text='Asignar', width=20, bg='brown', fg='white', command=procesar).place(x=120,y=105)

#------- Sección Gráficos
framegraficos = Frame(bg="#949292", width="550", height="820")
framegraficos.pack (side="bottom", anchor='n',padx=1,pady=1)

#Gráfico 
#valores iniciales para el gráfico de barras:
Data1 = {'Animales': ['A','B','C'], 'Cantidad': [0,0,0]}
df1 = DataFrame(Data1, columns= ['Animales', 'Cantidad'])
df1 = df1[['Animales', 'Cantidad']].groupby('Animales').sum()

#Crear Gráfico de barras:
grafico1 = plt.Figure(figsize=(8,7), dpi=50)
barras = grafico1.add_subplot(111)
bar1 = FigureCanvasTkAgg(grafico1, framegraficos)
bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
df1.plot(kind='bar', legend=True, ax=barras)
barras.set_title('Zoologico')



root.resizable(0,0)
root.mainloop()