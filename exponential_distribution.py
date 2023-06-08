def exponential_distribution(lambd, beta, x):
    """
    Función de distribución exponencial con parámetro adicional.

    Args:
        lambd (float): Parámetro lambda.
        beta (float): Parámetro adicional.
        x (float): Valor a evaluar.

    Returns:
        float: Probabilidad en el valor x.
    """
    if x >= 0:
        return lambd * pow(2.71828, -lambd * x) + beta
    else:
        return 0