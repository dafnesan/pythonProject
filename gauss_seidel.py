import numpy as np

array = np.array([[9, 2, -1], [7, 8, 5], [3, 4, -10]], dtype="float32")
results = np.array([-2, 3, 6], dtype="float32")
iteration_limit = 100
tolerance_percentage = 1.0

def process(array, results, iteration_limit: int, tolerance_percentage: float):
    """
    Calcula los valores de las incognitas de un sistema de ecuaciones de n x n con el método de Gauss-Seidel

    :param array: Array que contiene los coeficientes del sistema de ecuaciones
    :param results: Array que contiene los resultados de ecuaciones
    :param iteration_limit: Número máximo de iteraciones que se realizarán en caso de no alcanzar el porcentaje de tolerancia de error
    :param tolerance_percentage: Porcentaje de tolerancia de error
    :return: Numpy array que contiene los valores de las incognitas
    """
    xs = np.zeros(len(array)).astype("float32")
    errors = np.zeros(len(array)).astype("float32")

    iteration = 0

    while True:

        ant = np.copy(xs)

        #Ciclo para alcular los valores de x
        for row in range(len(array)):
            result = 0
            for column in range(len(array)):
                if column != row:
                    result -= array[row][column] * xs[column]
            xs[row] = (result + results[row]) / array[row][row]

        #Ciclo para calcular el error aproximado
        for e in range(len(xs)):
            errors[e] = abs(((xs[row] - ant[row]) / xs[row]) * 100.0)

        iteration += 1

        #Determina si el mayor error aproximado de las icognitas esta por debajo del procentaje de tolerancia de error
        if np.amax(np.absolute(errors)) < tolerance_percentage:
            print(f"Se alcanzó el porcentaje de tolerancia en la iteración: {iteration}")
            print_1d_array(xs)
            return xs

        # Determina si se alcanzó el límite de iteraciones
        if iteration == iteration_limit:
            print("Se alcanzó el límite de iteraciones")
            print_1d_array(xs)
            return xs

def print_1d_array(array):
    for a in array:
        print(a, end=", ")

process(array, results, iteration_limit, tolerance_percentage)