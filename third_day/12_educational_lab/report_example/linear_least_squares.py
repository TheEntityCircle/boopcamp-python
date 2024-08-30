import numpy as np


def lin_ls(x, y):
    """
    Eng:
        Returns coefficients b, k and their standard errors s_k, s_b
    from linear approximation (using least squares) y = k * x + b to
    given points (x, y).
    Rus:
        Возвращает коэффициенты b, k и их погрешности s_b, s_k при
    линейной аппроксимации y = k * x + b методом МНК по введённым точкам (х, у).
    Parameters
    ----------
    x : numpy.ndarray
        Numpy array with x coordinates of points.

    y : numpy.ndarray
        Numpy array with y coordinates of points. Vectors x and y must be the same length.

    Returns
    -------
    out : tuple
        (k, s_k, b, s_b)
    """
    def lin_ls(x, y):
        xy = np.mean(x * y)
        x1y = np.mean(x) * np.mean(y)
        x2 = np.mean(x * x)
        x12 = np.mean(x) ** 2
        y2 = np.mean(y * y)
        y12 = np.mean(y) ** 2
        k = (xy - x1y) / (x2 - x12)
        b = np.mean(y) - k * np.mean(x)
        s_k = np.sqrt(1 / x.size) * np.sqrt((y2 - y12) / (x2 - x12) - k ** 2)
        s_b = s_k * np.sqrt(x2 - x12)
        return k, s_k, b, s_b
