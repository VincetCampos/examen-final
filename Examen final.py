from tkinter import *
from datetime import datetime, date, time, timedelta
import calendar


root=Tk()
root.title("Examen Final")


#Su función es de contar cuantos días viviendo
def fecha():
	try:
		fecha=Entry3.get() + "-" + Entry4.get() + "-" + Entry5.get()
		datetime.strptime(fecha, '%d-%m-%Y')
		print('fecha valida')
	except:
		print('Fecha inválida')
	fechaHoy=datetime.now().date()
	fechaNacimiento = date(int(Entry5.get()), int(Entry4.get()), int(Entry3.get()))
	delta = fechaHoy - fechaNacimiento
	Respuestas['text'] = "Usted nacio el " + fecha + " y ha vivido " + str(delta.days)

	#Su función es de convertir la fecha ingresada de enteros a binarios
def bina():
	# Convertir String a Integer
	numDia=int(Entry3.get())
	numMes=int(Entry4.get())
	numAnio=int(Entry5.get())
	listaDia = []
	listaMes = []
	listaAnio = []

        # Unimos el dia el mes y el anio
	stringFecha = Entry3.get() + "/" + Entry4.get() + "/" + Entry5.get()

	resultado = "Fecha " + stringFecha + " en binario "

	while numDia>=1:
		listaDia.insert(0,numDia%2)
		numDia = numDia // 2

	while numMes>=1:
		listaMes.insert(0,numMes%2)
		numMes = numMes // 2

	while numAnio>=1:
		listaAnio.insert(0,numAnio%2)
		numAnio = numAnio // 2

	resultado = resultado + "".join(str(i) for i in listaDia) + "/"
	resultado = resultado + "".join(str(i) for i in listaMes) + "/"
	resultado = resultado + "".join(str(i) for i in listaAnio)

	Respuestas["text"]=resultado
		
	#Su función es de ver si su nombre y apellido son par e impar
def par_impar():
	nom=len(Entry1.get())
	ape=len(Entry2.get())
	
	if nom%2==0 and ape%2 == 0:
		a="Tu nombre y apellido son pares"
		Respuestas['text']=a
	elif nom%2!=0 and ape%2 == 0:
			c="Tu nombre es impar y tu apellido es par"
			Respuestas['text']=c
	elif nom%2==0 and ape%2 != 0:
			d="Tu nombre es par y tu apellido es impar"
			Respuestas['text']=d
	else:
		b="tu nombre y apellido son impares"
		Respuestas["text"]=b
		

#def obtener_vocales(frase):




#su función es de escribir el su nombre al reves
def al_reves():
	ResNo=Entry1.get()
	ResAp=Entry2.get()
	Invertido1=''.join(reversed(ResNo))
	Invertido2=''.join(reversed(ResAp))
	Respuestas["text"]=Invertido2, Invertido1


#El titulo y los demas textos
Titulo = Label(root, text='Bienvenido', font=('Arial', 23))
Label1 = Label(root, text='Nombre')
Label2 = Label(root, text='Apellido')
Label3 = Label(root, text='Día')
Label4 = Label(root, text='Mes')
Label5 = Label(root, text='Año')
Respuestas = Label(root, text='Aca se verá el resultado de las funciones')

#Las entradas o inputs
Entry1 = Entry(root)
Entry1.focus()
Entry2 = Entry(root)
Entry3 = Entry(root)
Entry4 = Entry(root)
Entry5 = Entry(root)

#Los botones
var1 = Button(root, text='Variable 1', command= bina)
var2 = Button(root, text='Variable 2', command = fecha)
var3 = Button(root, text='Variable 3', command = par_impar)
var4 = Button(root, text='Variable 4')
var5 = Button(root, text='Variable 5', command = al_reves)


Titulo.grid(row=1,column=0, columnspan=4)

Label1.grid(row=3,column=0)
Entry1.grid(row=3,column=1, columnspan=4, sticky=W+E)


Label2.grid(row=4,column=0)
Entry2.grid(row=4,column=1, columnspan=4, sticky=W+E)

Label3.grid(row=5,column=0)
Entry3.grid(row=5,column=1, columnspan=4, sticky=W+E)

Label4.grid(row=6,column=0)
Entry4.grid(row=6,column=1, columnspan=4, sticky=W+E)

Label5.grid(row=7,column=0)
Entry5.grid(row=7,column=1, columnspan=4, sticky=W+E)

var1.grid(row=8,column=0, columnspan=1, sticky=E)
var2.grid(row=8,column=1, sticky=W+E)
var3.grid(row=8,column=2, sticky=W+E)
var4.grid(row=8,column=3, sticky=W+E)
var5.grid(row=8,column=4, sticky=W+E)

Respuestas.grid(row=10,column=0, columnspan=5)


root.mainloop()
