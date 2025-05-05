
# Onderzoeksopdracht wiskunde 2024-2025

In deze onderzoeksopdracht gaan we de nadruk leggen op integralen berekenen met behulp van de trapeziummethode. In deze readme zullen we de werkwijze van de code en onze gedachtengang uitleggen.



## Features

- Boven- en ondersom (Riemann)
- Trapeziummethode
- Berekening Gini-coëfficiënt

## Explanation
In dit onderdeel zullen we wat extra informatie geven over de werking van de code.

**Let op: De volgende onderdelen zijn nodig vooraleer je het programma kan uitvoeren: Numpy, Matplotlib en Scipy!**

### Algemene informatie
We gebruiken doorheen het programma een algemene functie f(x). Deze is cruciaal voor de rest van de code.

Er is een variabele 'tekenLorenzCurve', deze dient om het tekenen te beperken tot de trapeziummehtode of de lorenzcurve.

Voor het visueel weergeven gebruiken we telkens 'matplotlib.pyplot'.

### Riemann
We hebben aan dit onderdeel zelf niets moeten doen, want dit werd gegeven door de leerkracht. Deze code berekent de boven- en ondersom van een bepaalde functie, namelijk f(x).

We hebben ook een relatieve fout berekend voor dit onderdeel.

### Trapeziummethode
Voor dit onderdeel maken we gebruik van volgende functie: Trapeziummethode(n, ondergrens, bovengrens).

Voor deze opdracht hebben we gebruik gemaakt van de trapeziummethode, deze laat ons toe om de oppervlakte tussen de grafiek en de x-as te berekenen. Dit gebeurt met verschillende trapezia die gemaakt worden tussen de x-as en de grafiek.

Om deze functie uit te voeren geven we volgende zaken mee:
- n = aantal intervallen
- ondergrens = de ondergrens van de integraal
- bovengrens = de bovengrens van de integraal

### Berekenen van Gini-coëfficiënt
Voor dit onderdeel gebruiken we deze functie: bereken_gini_met_trapezium(data, n=100). De volgende zaken geven we mee:
- data = de losstaande data
- n = Aantal intervallen

We wouden er zeker van zijn dat de functie van de trapeziummethode volledig operationeel was in deze deelopdracht.

Om dit te bereiken moesten we bepaalde zaken gaan toepassen:
- We normaliseren de data naar de cumulatieve waarden.
- We gebruiken interpolatie om van de losstaande data een lineare functie, zo kunnen we de trapeziummethode gebruiken.

## Authors

- [@DaanHautekeete](https://github.com/DaanHautekeete)
- [@MasterOfTheIdiots](https://github.com/MasterOfTheIdiots)
- [@fcrnwl](https://github.com/fcrnwl)
