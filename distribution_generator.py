import matplotlib.pyplot as plt
import numpy as np
from uniform_distribution import uniform_distribution
from exponential_distribution import exponential_distribution
import normal_distribution
from scipy.stats import norm

# Gráfico de la distribución uniforme
def plot_uniform_distribution(a, b):
    x_values = np.linspace(a, b, 1000)
    y_values = np.full_like(x_values, 1 / (b - a))

    step = (b - a) / 1000

    x = a
    while x <= b:
        x_values = np.append(x_values, x)
        y_values = np.append(y_values, 1 / (b - a))
        x += step

    # Graficar la distribución uniforme
    plt.plot(x_values, y_values)
    plt.xlabel('Valores')
    plt.ylabel('Probabilidad')
    plt.title('Distribución Uniforme')

    # Agregar líneas verticales en los límites de la distribución
    plt.axvline(a, color='red', linestyle='--', label='Valor mínimo')
    plt.axvline(b, color='blue', linestyle='--', label='Valor máximo')

     # Agregar texto de la probabilidad en x
    prob_x = 1 / (b - a)
    plt.text((a + b) / 2, prob_x, f'Probabilidad en x: {prob_x}', ha='center', va='bottom')

    plt.legend()
    plt.grid(True)
    plt.show()

# Gráfico de la distribución exponencial
def plot_exponential_distribution(lambd):
    x_values = np.linspace(0, 10, 1000)
    y_values = lambd * np.exp(-lambd * x_values)

    plt.plot(x_values, y_values)
    plt.xlabel('Valores')
    plt.ylabel('Probabilidad')
    plt.title('Distribución Exponencial')

    # Ajustar el rango del eje y
    plt.ylim(0, max(y_values) * 1.1)

    # Calcular medidas estadísticas
    expected_value = 1 / lambd
    variance = 1 / (lambd**2)
    std_deviation = np.sqrt(variance)

     # Mostrar medidas estadísticas en la gráfica
    plt.text(0.5, max(y_values) * 0.8, f"Valor esperado: {expected_value:.2f}", ha='left', va='center')
    plt.text(0.5, max(y_values) * 0.7, f"Varianza: {variance:.2f}", ha='left', va='center')
    plt.text(0.5, max(y_values) * 0.6, f"Desviación estándar: {std_deviation:.2f}", ha='left', va='center')

    plt.grid(True)
    plt.show()

# Gráfico de la distribución normal
def plot_normal_distribution(mu, sigma):
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 100)
    y = norm.pdf(x, mu, sigma)

    plt.plot(x, y)
    plt.xlabel("Valores")
    plt.ylabel("Densidad de Probabilidad")
    plt.title("Distribución Normal")
    plt.grid(True)

    z_values = np.linspace(-3, 3, 7)
    prob_values = norm.cdf(z_values, mu, sigma)

    for i in range(len(z_values)):
        plt.text(mu + z_values[i] * sigma, norm.pdf(mu + z_values[i] * sigma, mu, sigma),
                 f"Z = {z_values[i]:.2f}\nP = {prob_values[i]*100:.2f}%", ha='center', va='bottom')

    plt.show()