# -*- coding: utf-8 -*-
"""Ćwiczenie2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TMgSHzol-uxzgbdw8HKnsoNzII4jjd6D

# Nowa sekcja

# Nowa sekcja

Zadanie 1 (7 pkt) 

Korzystając z poniższego kodu oraz pliku president_heights.csv utwórz tablicę zawierającą wzrost prezydentów USA.
"""

import pandas as pd
import numpy as np

data = pd.read_csv("president_heights.csv")
heights = np.array(data['height(cm)'])

average_heights = np.mean(heights)
print("Mean height:", average_heights)

standard_deviation_heights = np.std(heights)
print("Standard deviation:",standard_deviation_heights) 

min_height = np.amin(heights)
print("Minimum height:    ",min_height) 

max_height = np.amax(heights)
print("Maximum height:    ",max_height)

percentile_25th_heights = np.percentile(heights, 25)
print("25th percentile:   ",percentile_25th_heights) 

percentile_75th_heights = np.percentile(heights, 75)
print("75th percentile:   ",percentile_75th_heights) 

median_heights = np.median(heights)
print("Median:            ",median_heights)

"""Zadanie 2 (4 pkt) 

Wgraj dane z pliku Zadanie_2.csv. 

-Znajdź wektory własne, oraz wartości własne dla zawartej w pliku macierzy 

-Oblicz macierz odwrotną dla macierzy z pliku 
"""

data = np.genfromtxt('Zadanie_2.csv', delimiter = ';')
eigenvalues, eigenvectors = np.linalg.eig(data)
print("Wektory własne:", eigenvectors)
print("Wartości własne:", eigenvalues)

inv_data = np.linalg.inv(data)
print("Macierz odwrotna:", inv_data)

"""Zadanie 3 (8 pkt) 

Plik Seattle2014.csv zawiera informacje o rocznych opadach w Seattle w 2014. Wykorzystaj kod poniżej aby wczytać plik. 
"""

rainfall = pd.read_csv('Seattle2014.csv')['PRCP'].values
inches = rainfall/254.0
inchesArray = np.array(inches)

nie_padalo = np.sum(inchesArray == 0)
print("Number days without rain:      ",nie_padalo)

padalo = np.sum(inchesArray > 0)
print("Number days with rain:         ",padalo)

spadlo_powyzej_05_cala = np.sum(inchesArray > 0.5)
print("Days with more than 0.5 inches:",spadlo_powyzej_05_cala) 

spadlo_ponizej_02_cala_ale_padalo = np.sum((inchesArray < 0.2) & (inchesArray > 0))
print("Rainy days with < 0.2 inches  :",spadlo_ponizej_02_cala_ale_padalo) 

mediana_opadow_w_deszczowe_dni = np.median(inchesArray[inchesArray>0])
print("Median precip on rainy days in 2014 (inches):",mediana_opadow_w_deszczowe_dni) 

opady_latem_indences = np.arange(172, 262)
opady_latem = inchesArray[opady_latem_indences]
mediana_opadow_latem = np.median(opady_latem)
print("Median precip on summer days in 2014 (inches):",mediana_opadow_latem) 

maksymalne_opady_latem = np.amax(opady_latem)
print("Maximum precip on summer days in 2014 (inches):",maksymalne_opady_latem)

opady_rok_indences = np.arange(0,365)
opady_nie_latem_indences = np.setdiff1d(opady_rok_indences, opady_latem_indences)
opady_nie_latem = inchesArray[opady_nie_latem_indences]
maksymalne_opady_nie_latem = np.amax(opady_nie_latem)
print("Maximum precip on non-summer days in 2014 (inches):",maksymalne_opady_nie_latem)

"""Zadanie 4 (5 pkt) 

Dane są dwa wektory A i B.  

A = [0,3,2,5] 

B = [0,3,1,4] 


Wykonaj następujące operacje: 

    Dodaj A i B 

    Odejmij B od A 

    Pomnóż wektor A przez skalar a=4 

    Oblicz iloczyn skalarny wektorów A i B 

    Znajdź długość wektora B 

Te operacje można wykonać „ręcznie” w Pythonie, ale postaraj się znaleźć odpowiednie funkcje NumPy. 
"""

A=[0,3,2,5]

B=[0,3,1,4] 

wektorA = np.array(A);
wektorB = np.array(B);
print("Wektor A: {x}".format(x = wektorA))
print("Wektor B: {x}".format(x = wektorB))

sumaWektorow = np.add(wektorA, wektorB);
print("Suma wektorów A i B to {x}".format(x = sumaWektorow))

roznicaWektorow = np.subtract(wektorB, wektorA);
print("Różnica wektorów B i A to {x}".format(x = roznicaWektorow))

a = 4
iloczynPrzezSkalar = np.multiply(wektorA, a);
print("Iloczyn wektora A przez skalar a=4 to {x}".format(x = iloczynPrzezSkalar))

iloczynWektorow = np.multiply(wektorA, wektorB);
print("Iloczyn skalarny wektorów A i B to {x}".format(x = iloczynWektorow))

dlugoscWektora = np.linalg.norm(wektorB)
print("Dlugosc wektora B to {x}".format(x = dlugoscWektora))