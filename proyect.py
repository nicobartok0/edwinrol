from tkinter import *
from tkinter import ttk
import tkinter as tk
import random
from tkinter import PhotoImage
from tkinter import messagebox
from PIL import Image, ImageTk


d = 0

class Aplicacion(ttk.Frame):
    
    
    def __init__(self, master=None):
        
        # - - Configuración de la ventana

        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.root = Toplevel()

        self.root.geometry('800x600')
        self.root.resizable(width=False, height=False)
        self.root.title('Jerarquía Table Manager Alpha 1.3')

        photo = PhotoImage(file = "dado.png")
        self.root.iconphoto(False, photo)

        # - - Configuración de los widgets

        #Nombres de personajes
        for i in range (8):
            name1 = tk.Text(self.root, height=1, width=10)
            sum = i * 50
            name1.place(x=20, y=60+sum)
            name1.insert(tk.END, "PERSONAJE")

        

        #Botón de salida
        self.salir= tk.Button(self.root,text='Salir', command=self.root.quit, height=2, width=5)
        self.salir.place(x= 20, y = 550)

        #Coeficiente de ataque entry
        self.ca_et = tk.Label(self.root, text="C. de Ataque")
        self.ca_et.place(x=150, y=10)
        c1 = tk.Entry(self.root)
        c2 = tk.Entry(self.root)
        c3 = tk.Entry(self.root)
        c4 = tk.Entry(self.root)
        c5 = tk.Entry(self.root)
        c6 = tk.Entry(self.root)
        c7 = tk.Entry(self.root)
        c8 = tk.Entry(self.root)
        c1.place(x=167, y=60, width=40)
        c2.place(x=167, y=110, width=40)
        c3.place(x=167, y=160, width=40)
        c4.place(x=167, y=210, width=40)
        c5.place(x=167, y=260, width=40)
        c6.place(x=167, y=310, width=40)
        c7.place(x=167, y=360, width=40)
        c8.place(x=167, y=410, width=40)




        #Coeficiente de defensa entry
        self.cd_et = tk.Label(self.root, text="C. de Defensa")
        self.cd_et.place(x=250, y=10)
        d1 = tk.Entry(self.root)
        d2 = tk.Entry(self.root)
        d3 = tk.Entry(self.root)
        d4 = tk.Entry(self.root)
        d5 = tk.Entry(self.root)
        d6 = tk.Entry(self.root)
        d7 = tk.Entry(self.root)
        d8 = tk.Entry(self.root)
        d1.place(x=267, y=60, width=40)
        d2.place(x=267, y=110, width=40)
        d3.place(x=267, y=160, width=40)
        d4.place(x=267, y=210, width=40)
        d5.place(x=267, y=260, width=40)
        d6.place(x=267, y=310, width=40)
        d7.place(x=267, y=360, width=40)
        d8.place(x=267, y=410, width=40)

        #Botón de caras actuales
        #tk.Label(self.root, text="Caras actuales").place(x=670, y=460)
        #dice = tk.Entry(self.root)
        #dice.place(x=650, y= 480)
        

        #"Dados" texto en pantalla
        tk.Label(self.root, text="Dados").place(x=375, y=460)
        dado_text1 = tk.Label(self.root, text= 0)
        dado_text1.place(x= 373, y= 480)
        dado_text2 = tk.Label(self.root, text= 0)
        dado_text2.place(x= 388, y= 480)  
        dado_text3 = tk.Label(self.root, text= 0)
        dado_text3.place(x= 403, y= 480)  
        dado_img = ImageTk.PhotoImage(Image.open("dado.png"))
        panel = tk.Label(self.root, image = dado_img)
        panel.place(x= 340,y= 470)    

        #Coeficiente enemigo
        self.ce_et = tk.Label(self.root, text="C. Enemigo")
        self.ce_et.place(x=480, y=10)
        ce1 = tk.Entry(self.root)
        ce2 = tk.Entry(self.root)
        ce3 = tk.Entry(self.root)
        ce4 = tk.Entry(self.root)
        ce5 = tk.Entry(self.root)
        ce6 = tk.Entry(self.root)
        ce7 = tk.Entry(self.root)
        ce8 = tk.Entry(self.root)
        ce1.place(x=497, y=60, width=40)
        ce2.place(x=497, y=110, width=40)
        ce3.place(x=497, y=160, width=40)
        ce4.place(x=497, y=210, width=40)
        ce5.place(x=497, y=260, width=40)
        ce6.place(x=497, y=310, width=40)
        ce7.place(x=497, y=360, width=40)
        ce8.place(x=497, y=410, width=40)

        #Resultados
        tk.Label(self.root, text= "Resultados").place(x= 680, y=10)
    
        res1 = tk.Label(self.root,text=0)
        res1.place(x= 703, y=60)
        
        res2 = tk.Label(self.root,text=0)
        res2.place(x= 703, y=110)
        
        res3 = tk.Label(self.root,text=0)
        res3.place(x= 703, y=160)
        
        res4 = tk.Label(self.root,text=0)
        res4.place(x= 703, y=210)
        
        res5 = tk.Label(self.root,text=0)
        res5.place(x= 703, y=260)
        
        res6 = tk.Label(self.root,text=0)
        res6.place(x= 703, y=310)
        
        res7 = tk.Label(self.root,text=0)
        res7.place(x= 703, y=360)
        
        res8 = tk.Label(self.root,text=0)
        res8.place(x= 703, y=410)

        #Bonificaciones de armadura
        tk.Label(self.root, text='Bonif.').place(x= 595, y=10)
        
        bon1 = ttk.Combobox(self.root, state='readonly')
        bon1.place(x=595,y=60)
        bon1.configure(width=4, height=4)
        bon1["values"] = [0, 10, 20, 30, 40]
        bon1.current(0)
        
        bon2 = ttk.Combobox(self.root, state='readonly')
        bon2.place(x=595,y=110)
        bon2.configure(width=4, height=4)
        bon2["values"] = [0, 10, 20, 30, 40]
        bon2.current(0)

        bon3 = ttk.Combobox(self.root, state='readonly')
        bon3.place(x=595,y=160)
        bon3.configure(width=4, height=4)
        bon3["values"] = [0, 10, 20, 30, 40]
        bon3.current(0)

        bon4 = ttk.Combobox(self.root, state='readonly')
        bon4.place(x=595,y=210)
        bon4.configure(width=4, height=4)
        bon4["values"] = [0, 10, 20, 30, 40]
        bon4.current(0)

        bon5 = ttk.Combobox(self.root, state='readonly')
        bon5.place(x=595,y=260)
        bon5.configure(width=4, height=4)
        bon5["values"] = [0, 10, 20, 30, 40]
        bon5.current(0)
        
        bon6 = ttk.Combobox(self.root, state='readonly')
        bon6.place(x=595,y=310)
        bon6.configure(width=4, height=4)
        bon6["values"] = [0, 10, 20, 30, 40]
        bon6.current(0)

        bon7 = ttk.Combobox(self.root, state='readonly')
        bon7.place(x=595,y=360)
        bon7.configure(width=4, height=4)
        bon7["values"] = [0, 10, 20, 30, 40]
        bon7.current(0)

        bon8 = ttk.Combobox(self.root, state='readonly')
        bon8.place(x=595,y=410)
        bon8.configure(width=4, height=4)
        bon8["values"] = [0, 10, 20, 30, 40]
        bon8.current(0)

        #Funciones de ATAQUE NORMAL
        def atk1():
            dado1 = random.randrange(1,7)
            dado2 = random.randrange(1,7)
            print(dado1)
            print(dado2)
            if c1.get() == '' or ce1.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_atk_1 = (dado1 + dado2 + int(c1.get())) - int(ce1.get())
            if int(bon1.get()) > 0:
                res_atk_1 = res_atk_1 - res_atk_1 * (int(bon1.get())/100)
            print("El resultado de la tirada: ", res_atk_1)
            res1.config(text=res_atk_1)
            dado_text1.config(text=dado1)
            dado_text2.config(text=dado2)
            dado_text3.config(text=0)
        
        def atk2():
            dado1 = random.randrange(1,7)
            dado2 = random.randrange(1,7)
            print(dado1)
            print(dado2)
            if c2.get() == '' or ce2.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_atk_2 = (dado1 + dado2 + int(c2.get())) - int(ce2.get())
            if int(bon2.get()) > 0:
                res_atk_2 = res_atk_2 - res_atk_2 * (int(bon2.get())/100)
            print("El resultado de la tirada: ", res_atk_2)
            res2.config(text=res_atk_2)
            dado_text1.config(text=dado1)
            dado_text2.config(text=dado2)
            dado_text3.config(text=0)
        
        def atk3():
            dado1 = random.randrange(1,7)
            dado2 = random.randrange(1,7)
            print(dado1)
            print(dado2)
            if c3.get() == '' or ce3.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_atk_3 = (dado1 + dado2 + int(c3.get())) - int(ce3.get())
            if int(bon3.get()) > 0:
                res_atk_3 = res_atk_3 - res_atk_3 * (int(bon3.get())/100)
            print("El resultado de la tirada: ", res_atk_3)
            res3.config(text=res_atk_3)
            dado_text1.config(text=dado1)
            dado_text2.config(text=dado2)
            dado_text3.config(text=0)
        
        def atk4():
            dado1 = random.randrange(1,7)
            dado2 = random.randrange(1,7)
            print(dado1)
            print(dado2)
            if c4.get() == '' or ce4.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_atk_4 = (dado1 + dado2 + int(c4.get())) - int(ce4.get())
            if int(bon4.get()) > 0:
                res_atk_4 = res_atk_4 - res_atk_4 * (int(bon4.get())/100)
            print("El resultado de la tirada: ", res_atk_4)
            res4.config(text=res_atk_4)
            dado_text1.config(text=dado1)
            dado_text2.config(text=dado2)
            dado_text3.config(text=0)

        def atk5():
            dado1 = random.randrange(1,7)
            dado2 = random.randrange(1,7)
            print(dado1)
            print(dado2)
            if c5.get() == '' or ce5.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_atk_5 = (dado1 + dado2 + int(c5.get())) - int(ce5.get())
            if int(bon5.get()) > 0:
                res_atk_5 = res_atk_5 - res_atk_5 * (int(bon5.get())/100)
            print("El resultado de la tirada: ", res_atk_5)
            res5.config(text=res_atk_5)
            dado_text1.config(text=dado1)
            dado_text2.config(text=dado2)
            dado_text3.config(text=0)
        
        def atk6():
            dado1 = random.randrange(1,7)
            dado2 = random.randrange(1,7)
            print(dado1)
            print(dado2)
            if c6.get() == '' or ce6.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_atk_6 = (dado1 + dado2 + int(c6.get())) - int(ce6.get())
            if int(bon6.get()) > 0:
                res_atk_6 = res_atk_6 - res_atk_6 * (int(bon6.get())/100)
            print("El resultado de la tirada: ", res_atk_6)
            res6.config(text=res_atk_6)
            dado_text1.config(text=dado1)
            dado_text2.config(text=dado2)
            dado_text3.config(text=0)
        
        def atk7():
            dado1 = random.randrange(1,7)
            dado2 = random.randrange(1,7)
            print(dado1)
            print(dado2)
            if c7.get() == '' or ce7.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_atk_7 = (dado1 + dado2 + int(c7.get())) - int(ce7.get())
            if int(bon7.get()) > 0:
                res_atk_7 = res_atk_7 - res_atk_7 * (int(bon7.get())/100)
            print("El resultado de la tirada: ", res_atk_7)
            res7.config(text=res_atk_7)
            dado_text1.config(text=dado1)
            dado_text2.config(text=dado2)
            dado_text3.config(text=0)

        def atk8():
            dado1 = random.randrange(1,7)
            dado2 = random.randrange(1,7)
            print(dado1)
            print(dado2)
            if c8.get() == '' or ce8.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_atk_8 = (dado1 + dado2 + int(c8.get())) - int(ce8.get())
            if int(bon8.get()) > 0:
                res_atk_8 = res_atk_8 - res_atk_8 * (int(bon8.get())/100)
            print("El resultado de la tirada: ", res_atk_8)
            res8.config(text=res_atk_8)
            dado_text1.config(text=dado1)
            dado_text2.config(text=dado2)
            dado_text3.config(text=0)


        #Funciones de DEFENSA
        def def1():
            dado1 = random.randrange(1,9)
            print(dado1)
            if d1.get() == '' or ce1.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_def_1 = int(ce1.get()) - (int(d1.get()) + dado1)
            if int(bon1.get()) > 0:
                res_def_1 = res_def_1 - res_def_1 * (int(bon1.get())/100)
            print("El resultado de la tirada: ", res_def_1)
            res1.config(text=res_def_1)
            dado_text1.config(text=dado1)
            dado_text2.config(text=0)
            dado_text3.config(text=0)

        def def2():
            dado1 = random.randrange(1,9)
            print(dado1)
            if d2.get() == '' or ce2.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_def_2 = int(ce2.get()) - (int(d2.get()) + dado1)
            if int(bon2.get()) > 0:
                res_def_2 = res_def_2 - res_def_2 * (int(bon2.get())/100)
            print("El resultado de la tirada: ",  res_def_2)
            res2.config(text= res_def_2)
            dado_text1.config(text=dado1)
            dado_text2.config(text=0)
            dado_text3.config(text=0)

        def def3():
            dado1 = random.randrange(1,9)
            print(dado1)
            if d3.get() == '' or ce3.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_def_3 = int(ce3.get()) - (int(d3.get()) + dado1)
            if int(bon3.get()) > 0:
                res_def_3 = res_def_3 - res_def_3 * (int(bon3.get())/100)
            print("El resultado de la tirada: ", res_def_3)
            res3.config(text=res_def_3)
            dado_text1.config(text=dado1)
            dado_text2.config(text=0)
            dado_text3.config(text=0)

        def def4():
            dado1 = random.randrange(1,9)
            print(dado1)
            if d4.get() == '' or ce4.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_def_4 = int(ce4.get()) - (int(d4.get()) + dado1)
            if int(bon1.get()) > 0:
                res_def_4 = res_def_4 - res_def_4 * (int(bon4.get())/100)
            print("El resultado de la tirada: ", res_def_4)
            res4.config(text=res_def_4)
            dado_text1.config(text=dado1)
            dado_text2.config(text=0)
            dado_text3.config(text=0)

        def def5():
            dado1 = random.randrange(1,9)
            print(dado1)
            if d5.get() == '' or ce5.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_def_5 = int(ce5.get()) - (int(d5.get()) + dado1)
            if int(bon5.get()) > 0:
                res_def_5 = res_def_5 - res_def_5 * (int(bon5.get())/100)
            print("El resultado de la tirada: ", res_def_5)
            res5.config(text=res_def_5)
            dado_text1.config(text=dado1)
            dado_text2.config(text=0)
            dado_text3.config(text=0)

        def def6():
            dado1 = random.randrange(1,9)
            print(dado1)
            if d6.get() == '' or ce6.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_def_6 = int(ce6.get()) - (int(d6.get()) + dado1)
            if int(bon6.get()) > 0:
                res_def_6 = res_def_6 - res_def_6 * (int(bon6.get())/100)
            print("El resultado de la tirada: ", res_def_6)
            res6.config(text=res_def_6)
            dado_text1.config(text=dado1)
            dado_text2.config(text=0)
            dado_text3.config(text=0)

        def def7():
            dado1 = random.randrange(1,9)
            print(dado1)
            if d7.get() == '' or ce7.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_def_7 = int(ce7.get()) - (int(d7.get()) + dado1)
            if int(bon7.get()) > 0:
                res_def_7 = res_def_7 - res_def_7 * (int(bon7.get())/100)
            print("El resultado de la tirada: ", res_def_7)
            res7.config(text=res_def_7)
            dado_text1.config(text=dado1)
            dado_text2.config(text=0)
            dado_text3.config(text=0)

        def def8():
            dado1 = random.randrange(1,9)
            print(dado1)
            if d8.get() == '' or ce8.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_def_8 = int(ce8.get()) - (int(d8.get()) + dado1)
            if int(bon8.get()) > 0:
                res_def_8 = res_def_8 - res_def_8 * (int(bon8.get())/100)
            print("El resultado de la tirada: ", res_def_8)
            res8.config(text=res_def_8)
            dado_text1.config(text=dado1)
            dado_text2.config(text=0)
            dado_text3.config(text=0)

        #Funciones de ATAQUE MÁGICO
        def matk1():
            dado1 = random.randrange(1,7)
            dado2 = random.randrange(1,7)
            dado3 = random.randrange(1,7)
            print(dado1)
            print(dado2)
            print(dado3)
            if c1.get() == '' or ce1.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_matk_1 = (dado1 + dado2 + dado3 + int(c1.get())) - int(ce1.get())
            if int(bon1.get()) > 0:
                res_matk_1 = res_matk_1 - res_matk_1 * (int(bon1.get())/100)
            
            print("El resultado de la tirada: ", res_matk_1)
            res1.config(text=res_matk_1)
            dado_text1.config(text=dado1)
            dado_text2.config(text=dado2)
            dado_text3.config(text=dado3)

        def matk2():
            dado1 = random.randrange(1,7)
            dado2 = random.randrange(1,7)
            dado3 = random.randrange(1,7)
            print(dado1)
            print(dado2)
            print(dado3)
            if c2.get() == '' or ce2.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_matk_2= (dado1 + dado2 + dado3 + int(c2.get())) - int(ce2.get())
            if int(bon2.get()) > 0:
                res_matk_2 = res_matk_2 - res_matk_2 * (int(bon2.get())/100)
            
            print("El resultado de la tirada: ", res_matk_2)
            res1.config(text=res_matk_2)
            dado_text1.config(text=dado1)
            dado_text2.config(text=dado2)
            dado_text3.config(text=dado3)

        def matk3():
            dado1 = random.randrange(1,7)
            dado2 = random.randrange(1,7)
            dado3 = random.randrange(1,7)
            print(dado1)
            print(dado2)
            print(dado3)
            if c3.get() == '' or ce3.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_matk_3 = (dado1 + dado2 + dado3 + int(c3.get())) - int(ce3.get())
            if int(bon3.get()) > 0:
                res_matk_3 = res_matk_3 - res_matk_3 * (int(bon3.get())/100)
            
            print("El resultado de la tirada: ", res_matk_3)
            res1.config(text=res_matk_3)
            dado_text1.config(text=dado1)
            dado_text2.config(text=dado2)
            dado_text3.config(text=dado3)
            
        def matk4():
            dado1 = random.randrange(1,7)
            dado2 = random.randrange(1,7)
            dado3 = random.randrange(1,7)
            print(dado1)
            print(dado2)
            print(dado3)
            if c4.get() == '' or ce4.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_matk_4 = (dado1 + dado2 + dado3 + int(c4.get())) - int(ce4.get())
            if int(bon4.get()) > 0:
                res_matk_4 = res_matk_4 - res_matk_4 * (int(bon4.get())/100)
            
            print("El resultado de la tirada: ", res_matk_4)
            res1.config(text=res_matk_4)
            dado_text1.config(text=dado1)
            dado_text2.config(text=dado2)
            dado_text3.config(text=dado3)

        def matk5():
            dado1 = random.randrange(1,7)
            dado2 = random.randrange(1,7)
            dado3 = random.randrange(1,7)
            print(dado1)
            print(dado2)
            print(dado3)
            if c5.get() == '' or ce5.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_matk_5 = (dado1 + dado2 + dado3 + int(c5.get())) - int(ce5.get())
            if int(bon5.get()) > 0:
                res_matk_5 = res_matk_5 - res_matk_5 * (int(bon5.get())/100)
            
            print("El resultado de la tirada: ", res_matk_5)
            res1.config(text=res_matk_5)
            dado_text1.config(text=dado1)
            dado_text2.config(text=dado2)
            dado_text3.config(text=dado3)

        def matk6():
            dado1 = random.randrange(1,7)
            dado2 = random.randrange(1,7)
            dado3 = random.randrange(1,7)
            print(dado1)
            print(dado2)
            print(dado3)
            if c6.get() == '' or ce6.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_matk_6 = (dado1 + dado2 + dado3 + int(c6.get())) - int(ce6.get())
            if int(bon6.get()) > 0:
                res_matk_6 = res_matk_6 - res_matk_6 * (int(bon6.get())/100)
            
            print("El resultado de la tirada: ", res_matk_6)
            res1.config(text=res_matk_6)
            dado_text1.config(text=dado1)
            dado_text2.config(text=dado2)
            dado_text3.config(text=dado3)

        def matk7():
            dado1 = random.randrange(1,7)
            dado2 = random.randrange(1,7)
            dado3 = random.randrange(1,7)
            print(dado1)
            print(dado2)
            print(dado3)
            if c7.get() == '' or ce7.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_matk_7 = (dado1 + dado2 + dado3 + int(c7.get())) - int(ce7.get())
            if int(bon7.get()) > 0:
                res_matk_7 = res_matk_7 - res_matk_7 * (int(bon7.get())/100)
            
            print("El resultado de la tirada: ", res_matk_7)
            res1.config(text=res_matk_7)
            dado_text1.config(text=dado1)
            dado_text2.config(text=dado2)
            dado_text3.config(text=dado3)

        def matk8():
            dado1 = random.randrange(1,7)
            dado2 = random.randrange(1,7)
            dado3 = random.randrange(1,7)
            print(dado1)
            print(dado2)
            print(dado3)
            if c8.get() == '' or ce8.get() == '':
                messagebox.showerror(message='Falta uno o más valores para ingresar.', title='Error de datos.')
            res_matk_8 = (dado1 + dado2 + dado3 + int(c8.get())) - int(ce8.get())
            if int(bon8.get()) > 0:
                res_matk_8 = res_matk_8 - res_matk_8 * (int(bon8.get())/100)
            
            print("El resultado de la tirada: ", res_matk_8)
            res1.config(text=res_matk_8)
            dado_text1.config(text=dado1)
            dado_text2.config(text=dado2)
            dado_text3.config(text=dado3)


        #Botones de ataque
        img_atk = PhotoImage(file='attack.png')
        self.atk_button1 = tk.Button(self.root, image=img_atk, command=atk1).place(x=340, y=60)
        self.atk_button2 = tk.Button(self.root, image=img_atk, command=atk2).place(x=340, y=110)
        self.atk_button3 = tk.Button(self.root, image=img_atk, command=atk3).place(x=340, y=160)
        self.atk_button4 = tk.Button(self.root, image=img_atk, command=atk4).place(x=340, y=210)
        self.atk_button5 = tk.Button(self.root, image=img_atk, command=atk5).place(x=340, y=260)
        self.atk_button6 = tk.Button(self.root, image=img_atk, command=atk6).place(x=340, y=310)
        self.atk_button7 = tk.Button(self.root, image=img_atk, command=atk7).place(x=340, y=360)
        self.atk_button8 = tk.Button(self.root, image=img_atk, command=atk8).place(x=340, y=410)

        #Botones de defensa
        img_def = PhotoImage(file='deffense.png')
        self.atk_button1 = tk.Button(self.root, image=img_def, command=def1).place(x=380, y=60)
        self.atk_button2 = tk.Button(self.root, image=img_def, command=def2).place(x=380, y=110)
        self.atk_button3 = tk.Button(self.root, image=img_def, command=def3).place(x=380, y=160)
        self.atk_button4 = tk.Button(self.root, image=img_def, command=def4).place(x=380, y=210)
        self.atk_button5 = tk.Button(self.root, image=img_def, command=def5).place(x=380, y=260)
        self.atk_button6 = tk.Button(self.root, image=img_def, command=def6).place(x=380, y=310)
        self.atk_button7 = tk.Button(self.root, image=img_def, command=def7).place(x=380, y=360)
        self.atk_button8 = tk.Button(self.root, image=img_def, command=def8).place(x=380, y=410)

        #Botones de ataque mágico
        img_matk = PhotoImage(file='magic_attack.png')
        self.matk_button1 = tk.Button(self.root, image=img_matk,command=matk1).place(x=420, y=60)
        self.matk_button2 = tk.Button(self.root, image=img_matk,command=matk2).place(x=420, y=110)
        self.matk_button3 = tk.Button(self.root, image=img_matk,command=matk3).place(x=420, y=160)
        self.matk_button4 = tk.Button(self.root, image=img_matk,command=matk4).place(x=420, y=210)
        self.matk_button5 = tk.Button(self.root, image=img_matk,command=matk5).place(x=420, y=260)
        self.matk_button6 = tk.Button(self.root, image=img_matk,command=matk6).place(x=420, y=310)
        self.matk_button7 = tk.Button(self.root, image=img_matk,command=matk7).place(x=420, y=360)
        self.matk_button8 = tk.Button(self.root, image=img_matk,command=matk8).place(x=420, y=410)

        
        
        
        
        
            



        #- - Mainloop

        self.root.mainloop()
    
    
        



def main():
    mi_app = Aplicacion()
    return 0


if __name__ == '__main__':
    main()