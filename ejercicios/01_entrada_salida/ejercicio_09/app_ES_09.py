import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Dante
apellido: Diaz
---
Ejercicio: entrada_salida_09
---
Enunciado:
Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txtSueldo y txtIncremento), 
transformarlos en números y mostrar el importe de sueldo actualizado con el incremento porcentual utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Sueldo")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_sueldo = customtkinter.CTkEntry(master=self)
        self.txt_sueldo.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="% de Incremento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_incremento = customtkinter.CTkEntry(master=self)
        self.txt_incremento.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        sueldo = int((self.txt_sueldo.get()))
        incremento = int(self.txt_incremento.get())

        aumento = sueldo * incremento / 100

        sueldo_final = aumento + sueldo 

        alert(title="Sueldo actualizado", message= f"Su sueldo es {sueldo_final}")
       
       
        # precio = 1000
        
        # 1.10 EL 1 REPRESENTA EL 100% Y EL 10 EL AUMENTO

        # regla de 3 corta
        # porcentaje = precio * 0.10
        
        # expresion larga
        # aumento = precio * 10 / 100

        
        # precio_final = precio + aumento

        # forma corta si quiero solo el precio final, regla de 3 mas aumento
        # precio_final = precio * 1.10
        
        # precio con descuento forma RAPIDA
        # precio_final = precio * 0.90

       
        

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()