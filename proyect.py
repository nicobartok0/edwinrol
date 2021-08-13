from tkinter import *
from tkinter import ttk
import tkinter as tk
import random

d = 0

class Aplicacion(Frame):
    
    
    def __init__(self, master=None):
        
        #Configuración de la ventana

        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.root = Tk()

        self.root.geometry('800x600')
        self.root.resizable(width=False, height=False)
        self.root.title('Programa de dados')

        #Configuración de los widgets

        #Nombres de personajes
        for i in range (8):
            name1 = tk.Text(self.root, height=1, width=10)
            sum = i * 50
            name1.place(x=20, y=20+sum)
            name1.insert(tk.END, "PERSONAJE")
        


        #mainloop

        self.root.mainloop()
    
    def dados():
        dado_valor = random.randrange(0,d)

def main():
    mi_app = Aplicacion()
    return 0


if __name__ == '__main__':
    main()