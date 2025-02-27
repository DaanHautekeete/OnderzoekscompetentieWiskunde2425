import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

bars_bovensommen=[]
bars_ondersommen =[]
width = []

def f(x):
    return -x**2 + 2*x + 10
 
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

    
Riemann(10,-1,4)