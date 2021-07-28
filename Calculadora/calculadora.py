# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 17:40:28 2021

@author: CristianH
"""

import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfilename


class Aplicacion_Calculadora(tk.Frame):

    operador = ''
    resultado = 0
    numeros = [str(i) for i in range(1, 10)]
    caracteres = ['+', '-', '*', '=', '/']
    # unimos caracteres y numeros
    numeros.insert(3, caracteres[0])
    numeros.insert(7, caracteres[1])
    numeros.insert(11, caracteres[2])
    numeros.insert(14, caracteres[3])
    numeros.insert(17, '0')
    numeros.insert(20, caracteres[4])
    termino=False

    def __init__(self, main_window):
        super().__init__(main_window)
        self.main_window = main_window
        self.texto = tk.StringVar()
        self.texto.set('0')
        main_window.resizable(0, 0)
        main_window.title("Calculadora")
        main_window.geometry("305x300")
        main_window.configure(bg='azure4')
        self.menuPrincipal()

    def menuPrincipal(self):
        # menu principal
        menu_principal = tk.Menu(self.main_window)
        self.main_window.config(menu=menu_principal)

        # opciones menu
        sub_menu_file = tk.Menu(self.main_window, tearoff=0)
        menu_principal.add_cascade(
            label="Archivo", menu=sub_menu_file, underline=0)

        # opciones submenu
        sub_menu_file.add_command(label="Abrir..", underline=0,
                                  accelerator="Ctrl-A", command=self.onAbrir)
        # agrega separador
        sub_menu_file.add_separator()
        sub_menu_file.add_command(label="Guardar", underline=0,
                                  accelerator="Ctrl-G", command=self.onGuardar)
        sub_menu_file.add_command(label="Salir", underline=0,
                                  accelerator="Ctrl-Q", command=self.onSalir)
        self.cargarInput()

    def cargarInput(self):
        # input entrada numeros.
        inputVentana = tk.Entry(self.main_window, state="readonly", textvariable=self.texto, font=(
            'Calculator', 20, 'bold'), width=17, bd=20, insertwidth=4, bg="powder blue", justify=tk.RIGHT).place(x=20, y=10)

        # Frame para los botones
        self.frame1 = tk.Frame(self.main_window, bg="silver",
                               width=250, height=200, pady=2, padx=2)

        # ubicamos el frame
        self.frame1.place(x=4, y=108)

        # Listener ventanas
        self.main_window.bind_all("<Control-q>", self.onSalir)
        self.main_window.bind_all("<Control-a>", self.onAbrir)
        self.main_window.bind_all("<Control-g>", self.onGuardar)
        self.crearBotones()

    def crearBotones(self):
        for numero in Aplicacion_Calculadora.numeros:
            botonesApp = BotonCalculadora(container=self.frame1, texto=numero)
        
        self.asignadoEventos(botonesApp.getBotonesArray())

    def asignadoEventos(self, botones):
        # for i in range(0,len(self.botones)):
        #     if self.botones[i]['text'].isnumeric():
        #         # print('is numeric')
        #         # print(self.botones[i]['text'])
        #         ch=self.botones[i].cget('text')
        #         print(ch)
        #         self.botones[i].bind("<Button-1>", lambda x:onInput(7))
        #     else:
        #         # print('is caracter')
        #         self.botones[i].bind("<Button-1>", lambda x:onOperador(self.botones[i]['text']))

        botones[0].bind("<Button-1>", lambda x: self.onInput(1))
        botones[1].bind("<Button-1>", lambda x: self.onInput(2))
        botones[2].bind("<Button-1>", lambda x: self.onInput(3))
        botones[3].bind("<Button-1>", lambda x: self.onOperador('+'))

        botones[4].bind("<Button-1>", lambda x: self.onInput(4))
        botones[5].bind("<Button-1>", lambda x: self.onInput(5))
        botones[6].bind("<Button-1>", lambda x: self.onInput(6))
        botones[7].bind("<Button-1>", lambda x: self.onOperador('-'))

        botones[8].bind("<Button-1>", lambda x: self.onInput(7))
        botones[9].bind("<Button-1>", lambda x: self.onInput(8))
        botones[10].bind("<Button-1>", lambda x: self.onInput(9))
        botones[11].bind("<Button-1>", lambda x: self.onOperador('*'))
        botones[12].bind("<Button-1>", self.onResultado)

        botones[14].bind("<Button-1>", lambda x: self.onOperador('/'))
        botones[13].bind("<Button-1>", lambda x: self.onInput(0))
        
        
        # Organizando los ultimos botones
        botones[12].grid(row=4, column=0, sticky=tk.N +
                              tk.E+tk.S+tk.W, padx=(2, 5), pady=(2, 2))
        botones[14].grid(row=4, column=1, columnspan=2,
                              sticky=tk.N+tk.E+tk.S+tk.W, padx=(2, 5), pady=(2, 2))
        botones[13].grid(row=4, column=3, sticky=tk.N +
                              tk.E+tk.S+tk.W, padx=(2, 5), pady=(2, 2))

    def onSalir(self, event=None):
        salir = messagebox.askquestion(
            "Desea salir?", "Seguro desea terminar el programa.")
        if salir == 'yes':
            ventana.destroy()

    def onGuardar(self, event=None):
        archivoFile = asksaveasfile(mode="w", initialfile='Untitled.txt',
                                    defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if archivoFile is None:
            return
        else:
            # datos=inputVentana.cget(textvariable)
            archivoFile.write(self.texto.get())
            archivoFile.close()

    def onAbrir(self, event=None):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        # abrimos el cuadro de dialogo
        openFile = askopenfilename(filetypes=filetypes)
        # read the text file and show its content on the Text
        self.texto.set(openFile.readlines())

    def onOperador(self, operador):

        Aplicacion_Calculadora.operacion = str(operador)
        Aplicacion_Calculadora.valor1 = self.texto.get()
        self.texto.set('')

    def onResultado(self, event=None):

        self.termino = False
        try:
            op = str(Aplicacion_Calculadora.valor1) + \
                str(Aplicacion_Calculadora.operacion)+str(self.texto.get())
            self.resultado = str(eval(op))
            self.texto.set('')
            self.mostrarResultado(self.resultado)
            self.resultado = 0

        except ZeroDivisionError as e:
            self.texto.set('Error')

    def onInput(self, valor):
        if self.termino:
            self.limpiarPantalla()
            self.termino=False
        
        if self.texto.get() == '0':
            self.texto.set('')
            self.texto.set(self.texto.get()+str(valor))
        else:
            self.texto.set(self.texto.get()+str(valor))

    def limpiarPantalla(self):
        self.resultado = 0
        self.texto.set('0')
        self.operacion = ''
        self.termino = False

    def mostrarResultado(self, valor):
        self.texto.set(valor)
        self.termino = True


class BotonCalculadora():
    # Cofiguracion propiedad botones
    botonWidth = 8
    botonHeight = 2
    botones = []

    def __init__(self, **options):

        self.contenedor = options['container']
        self.texto = options['texto']
        self.boton = tk.Button(self.contenedor, text=self.texto, width=self.botonWidth,
                               height=self.botonHeight, activebackground="CadetBlue2")
        self.botones.append(self.boton)

        if len(self.botones) == 15:
            self.organizarBotonesGrid()

    def organizarBotonesGrid(self):
        global contadorBotones
        contadorBotones = 0
        for i in range(3):
            for j in range(4):
                self.botones[contadorBotones].grid(
                    row=i, column=j, sticky=tk.N+tk.E+tk.S+tk.W, padx=(2, 5), pady=(2, 2))
                contadorBotones += 1


    def getBotonesArray(self):
        return self.botones

    def __str__(self):
        return "boton"+contadorBotones


ventana = tk.Tk()
app = Aplicacion_Calculadora(ventana)
app.mainloop()
