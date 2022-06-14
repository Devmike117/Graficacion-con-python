# ---------------------------
# Desarrollador: Mike Gabriel
# ---------------------------

# ⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀ ⣀⣀⣤⣤⣤⣀⡀
# ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀
# ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆ 
# ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆
# ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
# ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠸⣼⡿
# ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉
# ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
# ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿
# ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇
# ⠀⠀ ⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠇
# ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
# ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

# -------------------------------
# Implementación de las librerias
# -------------------------------

from tkinter import Tk, Frame,Button
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ----------------------------------------------------------
# creamos las propiedades de la ventana donde sera ejecutado
# ----------------------------------------------------------

ventana = Tk()
ventana.geometry('1100x500')
ventana.wm_title('UwU')
ventana.minsize(width=1100,height=500)

frame = Frame(ventana,  bg='blue')
frame.grid(column=0,row=0, sticky='nsew')

# ---------------------
# Datos de las graficas
# ---------------------

nombres = ['talvez', 'nel', 'si', 'tiene novio','nose']
colores = ['blue','red','green','magenta', 'black']
tamaño = [10, 25, 15, 20, 16]

fig, axs = plt.subplots(1,3 , dpi=80, figsize=(14, 6), 
	sharey=True, facecolor='#FF5733')

# -----------------------
# Editar estilo de titulo
# -----------------------

fig.suptitle('Probabilidad de que ella me ame',color='white',size=16, family="Kawaii Stitch")

# ----------------------------------------------
# color de borde = 'negro', ancho de línea = 1.2
# ----------------------------------------------

axs[0].bar(nombres, tamaño, color = colores)   
axs[1].scatter(nombres, tamaño, color = colores)
axs[2].plot(nombres, tamaño, color = 'm')


# ---------------------------------
# Crea el area de dibujo en Tkinter
# ---------------------------------

canvas = FigureCanvasTkAgg(fig, master = frame)  
canvas.draw()
canvas.get_tk_widget().grid(column=0, row=0)

# --------------
# cerrar ventana
# --------------
ventana.mainloop()
