import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from uniform_distribution import uniform_distribution
from exponential_distribution import exponential_distribution
import distribution_generator as dg

# Crear la ventana principal
window = tk.Tk()

# Configurar la ventana principal
window.title("Generador de Distribuciones")
window.geometry("300x400")

# Variable para almacenar la opción seleccionada
distribution_choice = tk.IntVar()

# Función para mostrar la segunda vista con los campos de entrada
def show_input_fields():
    choice = distribution_choice.get()

    # Ocultar la primera vista
    frame_choice.pack_forget()

    # Mostrar la segunda vista
    if choice == 1:
        frame_uniform_input.pack()
    elif choice == 2:
        frame_exponential_input.pack()
    elif choice == 3:
        frame_normal_input.pack()

# Función para generar el gráfico de la distribución seleccionada
def generate_distribution():
    choice = distribution_choice.get()

    if choice == 1:
        a = float(entry_a.get())
        b = float(entry_b.get())
        x = float(entry_x.get()) 
        probability = uniform_distribution(a, b, x)  # Llama a uniform_distribution con los tres argumentos
        print("La probabilidad en x es:", probability)
        dg.plot_uniform_distribution(a, b)
    elif choice == 2:
        lambd = float(entry_lambda.get())
        dg.plot_exponential_distribution(lambd)
    elif choice == 3:
        mu = float(entry_mu.get())
        sigma = float(entry_sigma.get())
        dg.plot_normal_distribution(mu, sigma)


        # Mostrar tabla de Gauss
        table_window = tk.Toplevel(window)
        table_window.title("Tabla de Gauss")
        table_frame = tk.Frame(table_window)
        table_frame.pack()

        table_label = tk.Label(table_frame, text="Tabla de Gauss")
        table_label.pack()

        # Crear una tabla de etiquetas para mostrar los valores de Z y probabilidad
        z_values = dg.get_z_values()
        prob_values = dg.get_probability_values()

        for i in range(len(z_values)):
            z_label = tk.Label(table_frame, text=f"Z = {z_values[i]:.2f}")
            z_label.grid(row=i+1, column=0, padx=10, pady=5)

            prob_label = tk.Label(table_frame, text=f"P = {prob_values[i]*100:.2f}%")
            prob_label.grid(row=i+1, column=1, padx=10, pady=5)

# Función para retroceder a la primera vista y seleccionar una nueva distribución
def go_back():
    # Borrar los campos de entrada
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_lambda.delete(0, tk.END)
    entry_mu.delete(0, tk.END)
    entry_sigma.delete(0, tk.END)

    # Ocultar la segunda vista
    frame_uniform_input.pack_forget()
    frame_exponential_input.pack_forget()
    frame_normal_input.pack_forget()

    # Mostrar la primera vista
    frame_choice.pack()

# Crear los frames para las vistas
frame_choice = tk.Frame(window)

# Etiqueta y botones para la selección de distribución
label_choice = tk.Label(frame_choice, text="Selecciona una distribución:")
label_choice.pack()

radio_uniform = tk.Radiobutton(frame_choice, text="Uniforme", variable=distribution_choice, value=1)
radio_uniform.pack()

radio_exponential = tk.Radiobutton(frame_choice, text="Exponencial", variable=distribution_choice, value=2)
radio_exponential.pack()

radio_normal = tk.Radiobutton(frame_choice, text="Normal", variable=distribution_choice, value=3)
radio_normal.pack()

button_next = tk.Button(frame_choice, text="Siguiente", command=show_input_fields)
button_next.pack()

# Frames para los campos de entrada de cada distribución
frame_uniform_input = tk.Frame(window)

label_uniform_input = tk.Label(frame_uniform_input, text="Distribución Uniforme")
label_uniform_input.pack()

label_a = tk.Label(frame_uniform_input, text="Valor mínimo:")
label_a.pack()
entry_a = tk.Entry(frame_uniform_input)
entry_a.pack()

label_b = tk.Label(frame_uniform_input, text="Valor máximo:")
label_b.pack()
entry_b = tk.Entry(frame_uniform_input)
entry_b.pack()

label_x = tk.Label(frame_uniform_input, text="Valor x:")
label_x.pack()
entry_x = tk.Entry(frame_uniform_input)
entry_x.pack()

button_plot_uniform = tk.Button(frame_uniform_input, text="Generar gráfico", command=generate_distribution)
button_plot_uniform.pack()

button_back = tk.Button(frame_uniform_input, text="Atrás", command=go_back)
button_back.pack()

frame_exponential_input = tk.Frame(window)

label_exponential_input = tk.Label(frame_exponential_input, text="Distribución Exponencial")
label_exponential_input.pack()

label_lambda = tk.Label(frame_exponential_input, text="Parámetro lambda:")
label_lambda.pack()
entry_lambda = tk.Entry(frame_exponential_input)
entry_lambda.pack()

button_plot_exponential = tk.Button(frame_exponential_input, text="Generar gráfico", command=generate_distribution)
button_plot_exponential.pack()

button_back = tk.Button(frame_exponential_input, text="Atrás", command=go_back)
button_back.pack()

frame_normal_input = tk.Frame(window)

label_normal_input = tk.Label(frame_normal_input, text="Distribución Normal")
label_normal_input.pack()

label_mu = tk.Label(frame_normal_input, text="Media:")
label_mu.pack()
entry_mu = tk.Entry(frame_normal_input)
entry_mu.pack()

label_sigma = tk.Label(frame_normal_input, text="Desviación estándar:")
label_sigma.pack()
entry_sigma = tk.Entry(frame_normal_input)
entry_sigma.pack()

button_plot_normal = tk.Button(frame_normal_input, text="Generar gráfico", command=generate_distribution)
button_plot_normal.pack()

button_back = tk.Button(frame_normal_input, text="Atrás", command=go_back)
button_back.pack()

# Frame para mostrar el gráfico
frame_plot = tk.Frame(window)

plot_label = tk.Label(frame_plot)
plot_label.pack()

# Mostrar la primera vista
frame_choice.pack()

# Iniciar el bucle de la interfaz gráfica
window.mainloop()
