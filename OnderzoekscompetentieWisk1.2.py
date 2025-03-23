import numpy as np
import matplotlib.pyplot as plt

bars_bovensommen = []
bars_ondersommen = []
width = []

def f(x):
    return np.exp(-2 * x)

# Exacte waarde van de integraal ∫ e^(-2x) dx van 0 tot 1
exacte_waarde = (-1/2) * (np.exp(-2*1) - np.exp(-2*0))

def Riemann(n, onder, boven):
    delta_x = ((boven - onder) / n)
    oppervlakte_boven = 0
    oppervlakte_onder = 0
    for i in range(n):
        basis = delta_x
        breedte = onder + (delta_x * (i)) + delta_x / 2
        f_max = max(f(onder + delta_x * i), f(onder + delta_x * (i + 1)))
        width.append(breedte)
        bars_bovensommen.append(f_max)
        oppervlakte_boven += basis * f_max
        f_min = min(f(onder + delta_x * i), f(onder + delta_x * (i + 1)))
        oppervlakte_onder += basis * f_min
        bars_ondersommen.append(f_min)

    print("Oppervlakte bovensom:", oppervlakte_boven)
    print("Oppervlakte ondersom:", oppervlakte_onder)

    # Relatieve fout berekening
    fout_bovensom = abs((exacte_waarde - oppervlakte_boven) / exacte_waarde) * 100
    fout_ondersom = abs((exacte_waarde - oppervlakte_onder) / exacte_waarde) * 100

    print(f"Relatieve fout bovensom: {fout_bovensom:.4f}%")
    print(f"Relatieve fout ondersom: {fout_ondersom:.4f}%\n")

    x_value = np.linspace(onder - 1, boven + 1, 1000)
    y_value = f(x_value)

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(121, aspect="equal")
    ax1.grid(True)
    ax1.bar(width, bars_bovensommen, delta_x, color="r", alpha=1, label='bovensommen')
    ax1.bar(width, bars_ondersommen, delta_x, color='g', alpha=1, label="ondersommen")
    ax1.plot(x_value, y_value, label="function f")
    ax1.legend()

    plt.show()

Riemann(10, 0, 1)

def Trapeziummethode(n, ondergrens, bovengrens):
    deltaX = (bovengrens - ondergrens) / n
    x_values = np.linspace(ondergrens, bovengrens, n + 1)
    totaal = sum(2 * f(x) for x in x_values[1:-1]) + f(x_values[0]) + f(x_values[-1])
    uitkomst = (deltaX / 2) * totaal  # Definitieve waarde

    print("Uitkomst integraal met Trapeziummethode:", uitkomst)

    # Relatieve fout berekening
    fout_trapezium = abs((exacte_waarde - uitkomst) / exacte_waarde) * 100
    print(f"Relatieve fout trapezium: {fout_trapezium:.4f}%\n")

    # Plot de functie en trapezia
    x_plot = np.linspace(ondergrens, bovengrens, 1000)
    y_plot = f(x_plot)

    plt.plot(x_plot, y_plot, label="f(x)", color='blue')

    for i in range(n):
        x0 = x_values[i]
        x1 = x_values[i + 1]
        y0 = f(x0)
        y1 = f(x1)

        plt.plot([x0, x0, x1, x1], [0, y0, y1, 0], 'r')
        plt.fill_between([x0, x1], [y0, y1], alpha=0.3, color='red')

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.title("Trapeziummethode")
    plt.grid()
    plt.show()

Trapeziummethode(10, 0, 1)