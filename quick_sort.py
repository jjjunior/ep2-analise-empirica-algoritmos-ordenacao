"""
Ipt - Instituto de Pesquisas Tecnológicas
Professor: Prof. Dr. Eng. Eduardo Takeo Ueda

Curso: Mestrado Profissional em Computação Aplicada
Disciplina: Estrutura de Dados e Análise de Algoritmos

Aluno: João José Maranhão Junior

Exercicio: Localizar a distancia entre o par de pontos mais proximos

"""


# Classe responsável por ordenar um array com o algoritmos QuickSort
# o parâmetro array contendo os pontos a serem ordenados
# o parametro criterio_ordenacao escolhe um atributo da classe para
# realizar a ordenacao.
# Python program for implementation of Quicksort Sort

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
