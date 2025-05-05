import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


bars_bovensommen = []
bars_ondersommen = []
width = []

tekenLorensCurve = True

def f(x):
    return np.exp(-2 * x)

# Exacte waarde van de integraal ∫ e^(-2x) dx van 0 tot 1
#exacte_waarde = (-1/2) * (np.exp(-2*1) - np.exp(-2*0))
exacte_waarde =0.43

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

#Riemann(10, 0, 1)

def Trapeziummethode(n, ondergrens, bovengrens):
    deltaX = (bovengrens - ondergrens) / n
    x_values = np.linspace(ondergrens, bovengrens, n + 1)
    totaal = sum(2 * f(x) for x in x_values[1:-1]) + f(x_values[0]) + f(x_values[-1])
    uitkomst = (deltaX / 2) * totaal  # Definitieve waarde

    print("Uitkomst integraal met Trapeziummethode:", uitkomst)

    # Plot de functie en trapezia
    x_plot = np.linspace(ondergrens, bovengrens, 1000)
    y_plot = f(x_plot)

    plt.figure(figsize=(6, 6))
    plt.plot(x_plot, y_plot, label="f(x)", color='blue')  # De kromme

    if tekenLorensCurve == True:
        # Plot Lorenz-curve
        x_plot = np.linspace(0, 1, 1000)
        y_plot = f(x_plot)
        plt.plot(x_plot, y_plot, label="Lorenz-curve", color='blue')

        # Plot perfecte gelijkheid (y = x)
        plt.plot([0, 1], [0, 1], label="Volledige gelijkheid", linestyle='--', color='gray')

        # Teken trapezia tussen de lijnen: y = x en y = f(x)
        for i in range(n):
            x0 = x_values[i]
            x1 = x_values[i + 1]
            y0 = f(x0)
            y1 = f(x1)

            # Punten van het trapezium: (x0, x0), (x1, x1), (x1, y1), (x0, y0)
            plt.fill(
                [x0, x1, x1, x0],
                [x0, x1, y1, y0],
                color='red',
                alpha=0.3,
                edgecolor='red'
            )
    else:
        for i in range(n):
            x0 = x_values[i]
            x1 = x_values[i + 1]
            y0 = f(x0)
            y1 = f(x1)

            # Hier tekenen we het trapezium met rode lijntjes
            plt.plot([x0, x0], [0, y0], 'r')  # linkerlijn
            plt.plot([x1, x1], [0, y1], 'r')  # rechterlijn
            plt.plot([x0, x1], [y0, y1], 'r')  # schuine lijn bovenaan

            # En we vullen het trapezium rood in
            plt.fill_between([x0, x1], [y0, y1], color='red', alpha=0.3)

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.title("Trapeziummethode met zichtbare trapezia")
    plt.grid(True)
    plt.axis('equal')
    plt.show()

    return uitkomst


#Trapeziummethode(10, 0, 1)


#Opdracht 2 deelopdracht 3
data = np.array([[0,13,24,22,14,8,6,4,3,2,1,3],[0,1.4,11.2,15.8,14.3,11,8.9,7.4,6,4.6,3.5,16]])


#trapeziummethode gebruiken om de ginicoefficient te berkenen
def bereken_gini_met_trapezium(data, n=100):
    # Stap 1: Normaliseer de data naar cumulatieve verhoudingen
    cumul_x = np.cumsum(data[0])
    cumul_y = np.cumsum(data[1])
    cumul_x = cumul_x / cumul_x[-1]
    cumul_y = cumul_y / cumul_y[-1]

    # Stap 2: Maak van deze discrete punten een vloeiende functie f(x) met interpolatie => een soort onzichtbare brug maken tussen bestaande data-punten, zodat je ook waarden tussen de punten kunt opvragen.
    global f  # Belangrijk! f moet globaal zijn => trapeziummethode moet eraan kunnen
    f = interp1d(cumul_x, cumul_y, kind='linear', fill_value="extrapolate")

    # Stap 3: Oppervlak onder de Lorenz-curve berekenen
    oppervlakte = Trapeziummethode(n, 0, 1)

    # Stap 4: Bereken de Gini-coëfficiënt
    gini = 1 - 2 * oppervlakte
    print(f"Gini-coëfficiënt: {gini}")

    if tekenLorensCurve != True:
        # Alles plotten
        plt.figure(figsize=(6, 6))  # Maak een vierkant figuur
        plt.plot(cumul_x, cumul_y, label='Lorenz-curve', color='blue')  # De echte verdeling van het inkomen
        plt.plot([0, 1], [0, 1], label='Volledige gelijkheid', linestyle='--', color='gray')  # De lijn als iedereen evenveel zou hebben
        plt.fill_between(cumul_x, cumul_y, cumul_x, color='red', alpha=0.3)  # Kleur het gebied tussen de lijnen (de ongelijkheid)

        #Labels, titel, legende instellen
        plt.xlabel("Cumulatief aandeel bevolking")
        plt.ylabel("Cumulatief aandeel inkomen")
        plt.title("Lorenz-curve en Gini-coëfficiënt")
        plt.legend()
        plt.grid(True)
        plt.axis('equal')  # Zorg dat de x- en y-as even lang zijn
        plt.show()

bereken_gini_met_trapezium(data)
