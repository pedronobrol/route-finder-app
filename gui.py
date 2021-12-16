import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import  *
from graph import Graph
import textwrap

from route_finder import get_adjacent_list

#Lista com estaciones
data = get_adjacent_list()
stations = list(data[1].keys())
lines = get_adjacent_list()[2]

#Crerar ventana principal
root = tk.Tk()
root.geometry('1000x1000')
root.title('Route Finder')

#Input origen
origin_label = ttk.Label(text='Origen', font='Courier')
origin_label.pack(fill=tk.X, padx=5, pady=5)

selected_origin = tk.StringVar()
origin_combo = ttk.Combobox(root, textvariable=selected_origin)

origin_combo['values'] = stations

# Evitar escritura en el input
origin_combo['state'] = 'readonly'
origin_combo.pack(fill=tk.X, padx=5, pady=5)

#Input destino
destination_label = ttk.Label(text='Detino', font='Courier')
destination_label.pack(fill=tk.X, padx=5, pady=5)

selected_destination = tk.StringVar()
destination_combo = ttk.Combobox(root, textvariable=selected_destination)

destination_combo['values'] = stations
# Evitar escritura en el input
destination_combo['state'] = 'readonly'
destination_combo.pack(fill=tk.X, padx=5, pady=5)

# Cerrar ventana
def close():
   root.quit()
# Enseñar resultado
def show_optimal_route() -> None:
    """ Enseñar la ruta optima"""
    search_text = ''

    if origin_combo.get() and destination_combo.get():
        origin = origin_combo.get()
        destination = destination_combo.get()

        adjacent_list, stations, lines = get_adjacent_list()

        graph = Graph(adjacent_list, stations, lines)

        result = graph.a_star_search(origin, destination)

        for station in result:
            search_text += f'{station} - '
        search_text = textwrap.fill(search_text, width=90)

        search_result.configure(text=f'{search_text}', fg='#222')
    else:
        search_result.configure(text=f'Es necesario seleccionar una estación', fg='#f22')

# Crear botón
ttk.Button(root, text= "Calcular ruta",width= 20, command= show_optimal_route).pack(pady=20)


# Enseñar resultado
label=Label(root, text="Resultado:", font=("Courier 16 bold"))
label.pack()
search_result=Label(root, text="", font=("Courier 13 bold"))
search_result.pack()

ttk.Button(root, text= "Salir",width= 20, command= close).pack(pady=5)

root.mainloop()