import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

bars_bovensommen=[]
bars_ondersommen =[]
width = []

def f(x):
    return np.exp(-2*x)
 
def Riemann (n,onder,boven):
    delta_x  = ((boven - onder)/n)
    oppervlakte_boven = 0
    oppervlakte_onder = 0
    for i in range(n):
        #via onder en bovensom
        basis = delta_x
        breedte = onder + (delta_x*(i)) +delta_x/2
        f_max = max(f(onder + delta_x*i),f(onder + delta_x*(i+1)))
        width.append(breedte)
        bars_bovensommen.append(f_max)
        oppervlakte_boven += basis*f_max
        f_min = min(f(onder+delta_x*i),f(onder+delta_x*(i+1)))
        oppervlakte_onder += basis*f_min
        bars_ondersommen.append(f_min)
        
    print("oppervlakte bovensom")
    print(oppervlakte_boven)
    print("oppervlakte ondersom")
    print(oppervlakte_onder)
    x_value = np.linspace(onder-1,boven+1,1000)
    y_value = f(x_value)
    
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(121, aspect = "equal")
    ax1.grid(True)
    ax1.bar(width, bars_bovensommen,delta_x, color ="r", alpha = 1, label = 'bovensommen')
    ax1.bar(width, bars_ondersommen, delta_x, color = 'g', alpha = 1, label = "ondersommen")
    ax1.plot(x_value,y_value, label = "function f")
    ax1.legend()
    
    plt.show()

    
# Riemann(10,-1,4)

def Trapeziummethode(n, ondergrens , bovengrens):

    #delta x berekenen
    deltaX = (bovengrens - ondergrens) / n

    #Hier maken we een lijst van waarden tussen de ondergrens en bovengrens die gelijkt verdeeld zijn
    #We moeten hier n + 1 doen zodat de bovengrens ook in rekening wordt gebracht
    x_values = np.linspace(ondergrens, bovengrens, n + 1)

    #Hier gebeurt
    #1) we doen voor alle waarden behalve de eerste en de laatse de uitkomst * 2
    #2) we berekenen de definitieve waarde voor 1 en 2 en voegen die toe aan ons totaal
    #3) We nemen van de vorige 2 stappen de som
    totaal = sum(2 * f(x) for x in x_values[1:-1]) + f(x_values[0]) + f(x_values[-1])

    #Hier berekenen we de definitieve uitkomst van onze integraal en geven we die weer
    uitkomst = (deltaX / 2) * totaal  # Definitieve waarde
    print("Uitkomst integraal:", uitkomst)

    # Plot de functie en trapezia
    x_plot = np.linspace(ondergrens, bovengrens, 1000)
    y_plot = f(x_plot)

    plt.plot(x_plot, y_plot, label="f(x)", color='blue')

    for i in range(n):
        #X-waarden van de trapezia
        x0 = x_values[i]
        x1 = x_values[i + 1]

        #Y-waarden van de trapezia
        y0 = f(x0)
        y1 = f(x1)

        #hier plotten we de trapezium

        plt.plot([x0, x0, x1, x1], [0, y0, y1, 0], 'r')

        #Hier vullen we de trapezium met een kleur
        plt.fill_between([x0, x1], [y0, y1], alpha=0.3, color='red')

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.title("Trapeziummethode benadering")
    plt.grid()
    plt.show()



Trapeziummethode(10,0,1)


