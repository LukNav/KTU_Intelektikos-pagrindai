import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
# import seaborn as sns
import numpy as np
from utils import *

tolydiniaiAtributai = ['Year', 'Engine Cylinders', 'Engine Displacement', 'City MPG', 'Highway MPG', 'Annual Fuel Cost', 'Tailpipe CO2 in Grams/Mile']
kategoriniaiAtributai = ['Drive', 'Transmission', 'Turbocharger', 'Supercharger', 'Fuel Type']

def main():
    data = readData("autodata_custom.csv")
    data.sort_values(by='Year')

    dataTolydiniu=data[tolydiniaiAtributai]
    dataKategoriniu=data[kategoriniaiAtributai]
    # print("2. Tolydieji. Bendras reiksmiu skaicius:\n",rastiAtributuSkaiciu(dataTolydiniu),"\n")
    # print("2. Tolydieji. Trukstamu reiksmiu procentas:\n", rastiTrukstamuAtributuProcenta(dataTolydiniu),"\n")
    # print("2. Tolydieji. Kardinalumai:\n", rastiAtributuKardinalumus(dataTolydiniu),"\n")
    # print("2. Tolydieji. Minimalios reiksmes:\n", rastiMin(dataTolydiniu),"\n")
    # print("2. Tolydieji. Maksimalios reiksmes:\n", rastiMax(dataTolydiniu),"\n")
    # print("2. Tolydieji. 1 ir 3 kvartiliai:\n", rastiKvartilius(dataTolydiniu),"\n")
    # print("2. Tolydieji. Vidurkiai:\n", rastiVidurkius(dataTolydiniu),"\n")
    # print("2. Tolydieji. Medianos:\n", rastiMedianas(dataTolydiniu),"\n")
    # print("2. Tolydieji. Standartiniai nuokrypiai:\n", rastiStandartiniusNuokrypius(dataTolydiniu),"\n")

    # print("3. Kategoriniai. Bendras reiksmiu skaicius:\n", rastiAtributuSkaiciu(dataKategoriniu),"\n")
    # print("3. Kategoriniai. Trukstamu reiksmiu procentas:\n", rastiTrukstamuAtributuProcenta(dataKategoriniu),"\n")
    # print("3. Kategoriniai. Kardinalumai:\n", rastiAtributuKardinalumus(dataKategoriniu),"\n")
    # # print("3. Kategoriniai. Rasti modas:\n", rastiModas(dataKategoriniu),"\n")
    # # # print("2. xxxxxxxxxxxxxx:\n", xxxxx(dataTolydiniu),"\n")
    # # print("3. Kategoriniai. Modu kiekis:\,",rastiModosDaznumus(dataKategoriniu),'\n')
    # print("3. Kategoriniai. Modos procentine reiksme:\n", rastiModuDaznumuProcentus(dataKategoriniu),'\n')
    # # print("3. Kategoriniai. Antros modos:\n",rastiAntraModa(dataKategoriniu),'\n')
    # print("3. Kategoriniai. Antros modos dažnumai:\n",rastiAntrosModosDaznumus(dataKategoriniu),'\n')
    # print("3. Kategoriniai. Antros modos procentine reiksme:\n", rastiAntruModuDaznumuProcentus(dataKategoriniu),'\n')
    # print("4. Rekomanduojamas histogramos stulpelių sk:\n", np.add(1,3.22*np.log(rastiAtributuSkaiciu(data))),'\n')
    
    data.dropna()
    # dataTolydiniu_Atfiltruota= salintiOutliers(dataTolydiniu)
    # print("5. Šalinam outliars. Pašalinta atributų:\n", rastiAtributuSkaiciu(dataTolydiniu)-rastiAtributuSkaiciu(dataTolydiniu_Atfiltruota),'\n')
    # print("9. Normalizacija:\n",normalize(dataTolydiniu),'\n')
    # plot(data)
    
    findCorreleation(dataTolydiniu)
    

if __name__ == "__main__":
    main()