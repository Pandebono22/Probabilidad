def uniform_distribution(a, b, x):
    """
    Función de distribución uniforme.

    Args:
        a (float): Valor mínimo.
        b (float): Valor máximo.
        x (float): Valor a evaluar.

    Returns:
        float: Probabilidad en el valor x.
    """
    if x >= a and x <= b:
        return 1 / (b - a)
    else:
        return 0