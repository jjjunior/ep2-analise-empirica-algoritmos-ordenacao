import subprocess
import webbrowser

import matplotlib.pyplot as plt
import numpy as np
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def plotar_barras(tamanhos_lista, tempos_radix, tempos_quick):
    x = np.arange(len(tamanhos_lista))
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, tempos_radix, width, label='RadixSort', color='b')
    rects2 = ax.bar(x + width / 2, tempos_quick, width, label='QuickSort', color='c')

    ax.set_ylabel('Tempo em segundos')
    ax.set_xlabel('Tamanho lista em potencia de 10')
    ax.set_title('Comparaçao dos Métodos de Ordenação')
    ax.ticklabel_format(style='sci', axis='x', scilimits=(-3, 3), useOffset=True, useMathText=True)
    ax.legend()
    plt.savefig('1.png', dpi=85)
    plt.show()


def plotar_minimos_quadrados(tamanhos_lista, tempos_radix, tempos_quick):
    tamanhos_array = np.array(tamanhos_lista)
    p1 = np.polyfit(tamanhos_array, tempos_radix, 1, )
    p2 = np.polyfit(tamanhos_array, tempos_quick, 1)

    fig = plt.figure()
    ax = fig.subplots()

    ax.plot(tamanhos_array, tempos_radix, 'o', label='RadixSort', color='b')
    ax.plot(tamanhos_array, np.polyval(p1, tamanhos_array), 'b--')

    ax.plot(tamanhos_array, tempos_quick, 'o', label='QuickSort', color='c')
    ax.plot(tamanhos_array, np.polyval(p2, tamanhos_array), 'c--')

    ax.set_ylabel('Tempo em segundos')
    ax.set_xlabel('Tamanho lista em unidades')

    ax.legend()

    plt.savefig('2.png', dpi=85)
    plt.show()


def junta_graficos():
    path = 'report.pdf'
    c = canvas.Canvas(path, pagesize=letter)
    c.drawImage('2.png', 0, 0)
    c.drawImage('1.png', 0, 400)
    c.save()
