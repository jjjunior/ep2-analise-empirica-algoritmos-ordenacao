from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

from quick_sort import quickSort
from radix_sort import radix


def printTime(tempo_total, nome_metodo):
    if int(tempo_total.total_seconds()) < 1:
        print("Tempo total %s : %.3f ms" % (nome_metodo, 1000 * tempo_total.total_seconds()))
    elif 1 <= int(tempo_total.total_seconds()) < 60:
        print("Tempo total %s : %.3f s" % (nome_metodo, tempo_total.total_seconds()))
    elif int(tempo_total.total_seconds()) >= 60:
        print("Tempo total %s : %.3f m" % (nome_metodo, tempo_total.total_seconds() / 60))


if __name__ == '__main__':

    range_numeros = 100
    tamanho_lista = 10
    tempos_radix = []
    tempos_quick = []
    tamanhos_lista = []

    while tamanho_lista <= 10000:
        tamanhos_lista.append(str(tamanho_lista))
        print("Criando Array de Tamanho: ", tamanho_lista)
        lista = np.random.randint(range_numeros, size=tamanho_lista)

        inicio = datetime.now()
        result = radix(lista)
        fim = datetime.now()
        delta_radix = fim - inicio
        printTime(delta_radix, "Radix Sort")
        result = []
        tempos_radix.append(round(delta_radix.total_seconds(), 4))

        inicio = datetime.now()
        quickSort(lista, 0, len(lista) - 1)
        fim = datetime.now()
        delta_quick = fim - inicio
        printTime(delta_quick, "Quick Sort")
        lista = []
        tempos_quick.append(round(delta_quick.total_seconds(), 4))

        tamanho_lista = tamanho_lista * 2
        range_numeros = range_numeros * 2
        print(tempos_radix)
        print(tempos_quick)

    x = np.arange(len(tamanhos_lista))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, tempos_radix, width, label='RadixSort',color='b')
    rects2 = ax.bar(x + width / 2, tempos_quick, width, label='QuickSort',color='c')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Tempo em segundos')
    ax.set_xlabel('Tamanho lista em unidades')
    ax.set_title('Comparaçao dos Métodos de Ordenação')
    ax.set_xticks(x)
    ax.set_xticklabels(tamanhos_lista)
    ax.legend()

    # ax.bar_label(rects1)
    # ax.bar_label(rects2)

    # fig2 = plt.figure(constrained_layout=True)
    # spec2 = gridspec.GridSpec(ncols=2, nrows=1, figure=fig)
    # f2_ax1 = fig2.add_subplot(spec2[0, 0])
    # f2_ax2 = fig2.add_subplot(spec2[0, 1])
    # fig2.add_subplot()
    plt.show()

    plt.plot(tempos_radix, color='b')
    plt.plot(tempos_quick, color='c')
    plt.show()

    # fig = plt.figure()
    #
    # names = tamanhos_lista
    # values = tempos_radix
    # values_2 = tempos_quick
    #
    # ax = fig.add_subplot(211)
    # ax2 = fig.add_subplot(212)
    # ax.set_title('Comparação RadixSort x QuickSort')
    #
    # ax.bar(names, values, color='goldenrod')
    # ax2.bar(names, values_2, color='mediumorchid')
    # plt.xlabel("Qt Elementos")
    # plt.ylabel("Tempo (s))")
    # plt.show()
    #
    # # output_notebook(notebook_type='jupyter')
    # x = tempos_radix
    # y = tempos_quick
    #
    # p = figure()
    #
    # p.circle(x, y, size=12, color='blue', legend_label='radix')
    #
    # p.line(x, y, color='red', legend_label='line red')
    #
    # p.triangle(y, x, color='green', size=12, legend_label='quick')
    #
    # p.line(y, x, color='black', legend_label='line black')
    #
    # show(p)
