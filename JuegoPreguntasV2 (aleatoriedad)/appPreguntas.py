# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 19:35:27 2021

@author: CristianH
"""

import tkinter as tk
from tkinter import Message
from tkinter import messagebox
from random import choice, sample

class AplicacionPreguntas(tk.Frame):

    __Preguntas = (
        {'pregunta': '¿Cuál es el nombre del río más largo del mundo?', 'opciones': [
            'a) Río Nilo', 'b) Rio Amazonas', 'c) Río Danubio', 'd) Rio popopuri'], 'respuesta': 1},
        {'pregunta': '¿Cuál es el océano más grande del mundo?', 'opciones': [
            'a) Océano Pacífico', 'b) Océano Índico', 'c) Océano Atlántico', 'd) Océano Artico'], 'respuesta': 0},
        {'pregunta': '¿Cuál es el país más grande del mundo?', 'opciones': [
            'a) China', 'b) Rusia', 'c) Alemania', 'd) Italia'], 'respuesta': 1},
        {'pregunta': '¿Cuál es el país que tiene forma de bota?', 'opciones': [
            'a) España', 'b) Honduras', 'c) Alemania', 'd) Italia'], 'respuesta': 3},
        {'pregunta': '¿Cuál es el país más poblado de la tierra?', 'opciones': [
            'a)  Estados Unidos', 'b) Rusia', 'c) China', 'd) Alemania'], 'respuesta': 2}
    )
    
   
    __preguntasAleatorias=sample([i for i in range(0,len(__Preguntas)-1)],len(__Preguntas)-1)
    
    
    
    __PreguntaActual = 0
    
    
    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.mensajeBienvenida = tk.StringVar()
        self.tituloPregunta = tk.StringVar()
        self.__PuntosBuenos=tk.IntVar(0)
        self.__PuntosMalos=tk.IntVar(0)
        self.radiosButton = tk.IntVar()
       
        self.mensajeBienvenida.set(
            'Bienvenido este es un juego para medir tus conocimientos generales')
        main_window.title("Quien quiere ser millonario")
        main_window.geometry('800x400')
        main_window.configure(bg='silver')
        self.configuracionApp()
        
    def configuracionApp(self):
        self.frameOpciones = tk.Frame(self.main_window, width=300, height=500,bg='silver',bd=2)
        self.frameResultado = tk.Frame(self.main_window, width=750, height=80,bg='silver')
        mensajeBuenos= tk.Message(self.frameResultado, text='Puntos Buenos',
                             width=700, bg='green', font=('Arial', 18, 'bold')).grid(row=0, column=0)
        mensajeMalos= tk.Message(self.frameResultado, text='Puntos Malos',
                             width=700, bg='red', font=('Arial', 18, 'bold')).grid(row=0, column=1)
        puntosBueno = tk.Message(self.frameResultado, textvariable=self.__PuntosBuenos,
                             width=700, bg='silver', font=('Arial', 18, 'bold')).grid(row=1, column=0)
        puntosMalos = tk.Message(self.frameResultado, textvariable=self.__PuntosMalos,
                             width=700, bg='silver', font=('Arial', 18, 'bold')).grid(row=1, column=1)
        self.frameResultado.place(x=20, y=309)
        self.frameOpciones.place(x=20, y=209)
        self.cargarMensajeBienvenida()

    def cargarMensajeBienvenida(self):
        mensaje = tk.Message(self.main_window, textvariable=self.mensajeBienvenida,
                             width=600, bg='silver', font=('Arial', 18, 'bold')).place(x=2, y=2)
        self.cargarTextoPregunta(
            AplicacionPreguntas.__Preguntas[AplicacionPreguntas.__PreguntaActual]['pregunta'])
        self.crearOpciones(
            AplicacionPreguntas.__Preguntas[AplicacionPreguntas.__PreguntaActual]['opciones'])
        
    def seleccionPreguntaAleatoria(self):
        OpcionPregunta=choice(AplicacionPreguntas.__preguntasAleatorias)
        indexOpcion=AplicacionPreguntas.__preguntasAleatorias.index(OpcionPregunta)
        del AplicacionPreguntas.__preguntasAleatorias[indexOpcion]

    def onSiguientePregunta(self, event=None):
        # Pregunta=iter(AplicacionPreguntas.__Preguntas)
        if AplicacionPreguntas.__PreguntaActual != len(AplicacionPreguntas.__Preguntas)-1:
            AplicacionPreguntas.__PreguntaActual += 1
            self.seleccionPreguntaAleatoria()
            self.cargarTextoPregunta(
                AplicacionPreguntas.__Preguntas[AplicacionPreguntas.__PreguntaActual]['pregunta'])
            self.crearOpciones(
                AplicacionPreguntas.__Preguntas[AplicacionPreguntas.__PreguntaActual]['opciones'])
            # self.botonSiguiente['state'] = tk.DISABLED

    def crearOpciones(self, opciones=['a)', 'b)', 'c)', 'd)']):
        contador = 0
        for row in range(2):
            for column in range(2):
                tk.Radiobutton(self.frameOpciones, text=opciones[contador], justify=tk.LEFT, width=25, font=(
                    'Tahoma', 18, 'italic'), state=tk.NORMAL,variable=self.radiosButton, value=contador, command=self.onVerificarRespuesta).grid(row=row, column=column)
                self.radiosButton.set(None)
                contador += 1
        

    def cargarTextoPregunta(self, textoPregunta):
        self.tituloPregunta.set(textoPregunta)
        mensajePregunta = tk.Message(self.main_window, textvariable=self.tituloPregunta,
                                     width=400, bg='silver', font=('Arial', 18, 'bold')).place(x=20, y=120)

    def onVerificarRespuesta(self, event=None):
        if str(AplicacionPreguntas.__Preguntas[AplicacionPreguntas.__PreguntaActual]['respuesta']) == str(self.radiosButton.get()):
            messagebox.showinfo("Correcto", "Haz seleccionado la respuesta correcta!")
            self.__PuntosBuenos.set(int(self.__PuntosBuenos.get())+1)
            self.onVerificaPuntaje()
           
        else:
            messagebox.showinfo("Incorrecto", "Lo sentimos esa no es la respuesta correcta!")
            self.__PuntosMalos.set(int(self.__PuntosMalos.get())+1)
            self.onVerificaPuntaje()
            
    def onVerificaPuntaje(self):
        if len(AplicacionPreguntas.__preguntasAleatorias) == 0:
            if self.__PuntosBuenos.get()> self.__PuntosMalos.get():
                messagebox.showinfo("Felicidades!!", "Haz ganado!")
            elif  self.__PuntosBuenos.get()==self.__PuntosMalos.get():
                 messagebox.showinfo("Upss!!!!", "Empate!")
            else:
                messagebox.showinfo("Lo sentimos !!", "Haz perdido!")
        else:
            self.onSiguientePregunta()

        

JuegoPreguntas = tk.Tk()
app = AplicacionPreguntas(JuegoPreguntas)
app.mainloop()
