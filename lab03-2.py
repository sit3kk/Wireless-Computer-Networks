from math import factorial
import numpy as np
import matplotlib.pyplot as plt


# Ponownie używamy funkcji ErlangB, którą zdefiniowaliśmy wcześniej
def ErlangB(A, C):
    sum_ = 0
    for k in range(C + 1):
        mul = A**k / factorial(k)
        for i in range(k + 1, C + 1):
            mul *= i
        sum_ += mul

    P = 1 / sum_
    return P

# Definicja funkcji tworzącej ciąg geometryczny
def calculate_traffic_intensity(A1, A2, NA):
    q = (A2/A1)**(1/(NA-1))
    return [A1 * q**n for n in range(NA)]

# Funkcja obliczająca Prawdopodobieństwo blokady dla danych wartości A i C
def calculate_probabilities(A_values, C_values):
    probabilities = np.zeros((len(C_values), len(A_values)))
    for i, C in enumerate(C_values):
        for j, A in enumerate(A_values):
            probabilities[i, j] = ErlangB(A, C)
    return probabilities

# Definicja funkcji plotującej wykresy
def plot_probabilities(A_values, probabilities, C_values):
    for i, C in enumerate(C_values):
        plt.semilogy(A_values, probabilities[i], label=f'C={C}')
    plt.xlabel('Natężenie ruchu (erl)')
    plt.ylabel('Prawdopodobieństwo blokady (GOS)')
    plt.title('Liczba kanałów')
    plt.legend()
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.show()

# Dane wejściowe
A1 = 0.1
A2 = 100
NA = 1000
C_values = [1, 2, 20, 25, 5, 50, 6, 60, 10, 100]

# Obliczanie wartości A i prawdopodobieństw
A_values = calculate_traffic_intensity(A1, A2, NA)
probabilities = calculate_probabilities(A_values, C_values)

# Rysowanie wykresów
plot_probabilities(A_values, probabilities, C_values)
