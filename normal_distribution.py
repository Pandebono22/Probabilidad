import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_normal_distribution(mu, sigma):
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
    y = norm.pdf(x, mu, sigma)

    plt.plot(x, y, label='Distribución Normal')
    plt.xlabel('Valores')
    plt.ylabel('Probabilidad')
    plt.title('Distribución Normal')
    plt.grid(True)

    # Calcular los valores de Z y probabilidad
    z_values = np.linspace(-3, 3, 7)
    prob_values = norm.cdf(z_values, mu, sigma)

    # Mostrar los valores de Z y probabilidad en el gráfico
    for i in range(len(z_values)):
        plt.text(mu + z_values[i] * sigma, norm.pdf(mu + z_values[i] * sigma, mu, sigma),
                 f"Z = {z_values[i]:.2f}\nP = {prob_values[i]*100:.2f}%", ha='center', va='bottom')

    plt.legend()
    plt.show()
