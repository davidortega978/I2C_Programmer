import os
import tkinter as tk
from tkinter import ttk

def agregar_texto(texto):
    cuadro_texto.config(state="normal")
    cuadro_texto.insert("end", texto + "\n")
    cuadro_texto.config(state="disabled")
    cuadro_texto.see(tk.END)  # Mueve el scroll al final del texto

def load_config():
    config_selected = combobox.get()
    if config_selected:
        agregar_texto(f"Se ha cargado la configuración {config_selected}")
    else:
        agregar_texto("No se ha seleccionado ninguna configuración")

def btn1_click():
    agregar_texto("Botón 1 presionado")
    load_config()

def btn2_click():
    agregar_texto("Botón 2 presionado")

def btn3_click():
    cuadro_texto_centro.delete("1.0", tk.END)
    agregar_texto("Script cleared...")

def btn4_click():
    cuadro_texto.config(state="normal")
    cuadro_texto.delete("1.0", tk.END)
    cuadro_texto.config(state="disabled")
    agregar_texto("Log cleared...")


def incluir_script():
    seleccionado = listbox.curselection()
    if seleccionado:
        script_seleccionado = listbox.get(seleccionado)
        ruta_script = os.path.join(carpeta_scripts, script_seleccionado)
        
        try:
            with open(ruta_script, "r") as script:
                contenido = script.read()
        
            cuadro_texto_centro.insert("end", contenido + "\n")
            cuadro_texto.see(tk.END)  # Mueve el scroll al final del texto
        except Exception as e:
            agregar_texto(f"Error al cargar el script: {e}")
    else:
        agregar_texto("Ningún script seleccionado")


# Crear una instancia de Tkinter
ventana = tk.Tk()
ventana.geometry("800x600")
ventana.title("I2C Programmer")

# Crear un Notebook (pestañas)
pestanas = ttk.Notebook(ventana)

# Crear pestañas
pestana1 = ttk.Frame(pestanas)
pestana2 = ttk.Frame(pestanas)

# Agregar pestañas al Notebook
pestanas.add(pestana1, text='Pestaña 1')
pestanas.add(pestana2, text='Pestaña 2')

# Añadir Notebook a la ventana
pestanas.pack(expand=1, fill="both")

# Crear un frame para la parte inferior de la pestaña1
frame_inferior = ttk.Frame(pestana1)
frame_inferior.pack(side="bottom", fill="both", expand=True)

# Crear un cuadro de texto en el frame inferior de la pestaña1
cuadro_texto = tk.Text(frame_inferior, height=10, state="normal")
cuadro_texto.pack(side="bottom", fill="x", expand=False)


# Crear tres frames en la pestaña1: izquierda, centro y derecha
frame_izquierda = ttk.Frame(pestana1, borderwidth=2, relief="solid")
frame_izquierda.pack(side="left", fill="both", expand=False)

# Crear etiqueta select:
label_select = tk.Label(frame_izquierda, text = "Select I2C Script:")
label_select.grid(row = 0, column = 0, pady = 2)
#############################################################################################


# Obtener lista de archivos .txt en una carpeta específica
carpeta = r"\Users\david\Documents\i2c_Programmer"  # Usando una cadena sin procesar
archivos_txt = [archivo for archivo in os.listdir(carpeta) if archivo.endswith(".txt")]

# Agregar Combobox
combobox = ttk.Combobox(frame_izquierda, values=archivos_txt, state="readonly")
combobox.grid(row = 0, column = 1, pady = 2)




##################################################################################################


# Agregar botones en frame izquierda
btn1 = ttk.Button(frame_izquierda, text="Load Script", command=btn1_click)
btn1.grid(row = 1, column = 0, ipadx = 80, columnspan = 2)

btn2 = ttk.Button(frame_izquierda, text="Save Script", command=btn2_click)
btn2.grid(row = 2, column = 0, ipadx = 80, columnspan = 2)

btn3 = ttk.Button(frame_izquierda, text="Clear Script", command=btn3_click)
btn3.grid(row = 3, column = 0, ipadx = 80, columnspan = 2)

btn4 = ttk.Button(frame_izquierda, text="Clear log", command=btn4_click)
btn4.grid(row = 4, column = 0, ipadx = 80, columnspan = 2)



# Crear un frame para la parte superior de la pestaña1
frame_centro = ttk.Frame(pestana1, borderwidth=2, relief="solid")
frame_centro.pack(side="left", fill="both", expand=True)

label_centro = tk.Label(frame_centro, text="Frame Centro - Script details")
label_centro.pack()

# Agregar un cuadro de texto editable con una barra de desplazamiento vertical en el frame centro
scrollbar = tk.Scrollbar(frame_centro)
scrollbar.pack(side="right", fill="y")

cuadro_texto_centro = tk.Text(frame_centro, yscrollcommand=scrollbar.set, width=10)
cuadro_texto_centro.pack(side="left", fill="both", padx=2, pady=2, expand=True)

scrollbar.config(command=cuadro_texto_centro.yview)

# Crear un frame para la parte superior de la pestaña1
frame_derecha = ttk.Frame(pestana1, borderwidth=2, relief="solid")
frame_derecha.pack(side="left", fill="both", expand=True)

label_derecha = tk.Label(frame_derecha, text="Frame Derecha - I2C scripts")
label_derecha.pack()

# Agregar un Listbox en el frame derecha
listbox = tk.Listbox(frame_derecha)
listbox.pack(side="top", fill="both", padx=2, pady=2, expand=True)

# Agregar elementos-scripts al Listbox (opcional) (borrar mas tarde)
#for item in range(10):
    #listbox.insert("end", f"Script {item+1}")

#######################################################################################

# Carpeta donde se encuentran los scripts .txt
carpeta_scripts = r"C:\Users\david\Documents\i2c_Programmer\Listado de Scripts"

# Obtener lista de archivos .txt en la carpeta
scripts_txt = [script for script in os.listdir(carpeta_scripts) if script.endswith(".txt")]

# Agregar archivos al Listbox
for script in scripts_txt:
    listbox.insert("end", script)

######################################################################################

# Crear un botón "Incluir elemento" en el frame derecha
btn_incluir = ttk.Button(frame_derecha, text="Incluir script", command=incluir_script)
btn_incluir.pack(side="bottom", padx=5, pady=5)




# Ejecutar el bucle principal de la ventana
ventana.mainloop()
