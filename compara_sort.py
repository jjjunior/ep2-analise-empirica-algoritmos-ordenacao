from datetime import datetime

import numpy as np

from grafico import plotar_barras, plotar_minimos_quadrados, junta_graficos
from quick_sort import quickSort
from radix_sort import radix
from utils import printTime, limit_intancia


def compara_sort(tamanho_lista, instancias):
    range_numeros = tamanho_lista * 10
    aumento_lista = 10
    limite = limit_intancia(tamanho_lista, aumento_lista, instancias)

    tempos_radix = []
    tempos_quick = []
    tamanhos_lista = []

    while tamanho_lista <= limite:
        radix_quick_sort(range_numeros, tamanho_lista, tamanhos_lista, tempos_quick, tempos_radix)
        tamanho_lista = tamanho_lista * aumento_lista
        range_numeros = range_numeros * aumento_lista

    print(tamanhos_lista)
    plotar_barras(tamanhos_lista, tempos_radix, tempos_quick)
    plotar_minimos_quadrados(tamanhos_lista, tempos_radix, tempos_quick)
    junta_graficos()


def radix_quick_sort(range_numeros, tamanho_lista, tamanhos_lista, tempos_quick, tempos_radix):
    tamanhos_lista.append(int(tamanho_lista))
    print("Criando Array de Tamanho: ", tamanho_lista)
    lista = np.random.randint(range_numeros, size=tamanho_lista)

    inicio = datetime.now()
    result = radix(lista)
    fim = datetime.now()
    delta_radix = fim - inicio

    printTime(delta_radix, "Radix Sort")
    tempos_radix.append(round(delta_radix.total_seconds(), 3))
    result = []

    inicio = datetime.now()
    quickSort(lista, 0, len(lista) - 1)
    fim = datetime.now()
    delta_quick = fim - inicio

    printTime(delta_quick, "QuickSort")
    tempos_quick.append(round(delta_quick.total_seconds(), 3))
    lista = []
    print(tempos_radix)
    print(tempos_quick)


def radix_quick_sort_simples(tamanho_lista, print_array):
    print("Criando Array de Tamanho: ", tamanho_lista)
    lista = np.random.randint(tamanho_lista, size=tamanho_lista)
    if print_array:
        print('Lista Desordenada')
        print(lista)

    inicio = datetime.now()
    result = radix(lista)
    fim = datetime.now()
    delta_radix = fim - inicio

    if print_array:
        print('Lista Ordenada RadixSort')
        print(result)
    result = []

    inicio = datetime.now()
    quickSort(lista, 0, len(lista) - 1)
    fim = datetime.now()
    delta_quick = fim - inicio

    if print_array:
        print('Lista Ordenada QuickSort')
        print(lista)
    lista = []
    printTime(delta_radix, "RadixSort")
    printTime(delta_quick, "QuickSort")


