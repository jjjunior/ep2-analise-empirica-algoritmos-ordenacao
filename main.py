import random
from timeit import default_timer as timer

from quick_sort import quickSort
from radix_sort import radix

if __name__ == '__main__':

    range_numeros = 100
    tamanho_lista = 10
    while(tamanho_lista <= 1000000):
        lista = random.sample(range(range_numeros),  tamanho_lista)

        # print(lista)
        inicio = timer()
        iniciar = inicio
        result = radix(lista)
        fim = timer()
        print("Tamanho da Lista: ", tamanho_lista )
        print("Tempo total Radix Sort : %.1f ms" % (100000 * (fim - iniciar)))
        # print(result)

        lista1 = random.sample(range(range_numeros),  tamanho_lista)
        # print(lista1)
        n = len(lista1)
        inicio = timer()
        iniciar = inicio
        quickSort(lista1, 0, n - 1)
        fim = timer()
        print("Tempo total Quick Sort : %.1f ms" % (100000 * (fim - iniciar)))
        # print(lista1)
        tamanho_lista = tamanho_lista * 10
        range_numeros = range_numeros * 10
