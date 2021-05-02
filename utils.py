import platform
import subprocess


def printTime(tempo_total, nome_metodo):
    if int(tempo_total.total_seconds()) < 1:
        print("Tempo total %s : %.3f ms" % (nome_metodo, 1000 * tempo_total.total_seconds()))
    elif 1 <= int(tempo_total.total_seconds()) < 60:
        print("Tempo total %s : %.3f s" % (nome_metodo, tempo_total.total_seconds()))
    elif int(tempo_total.total_seconds()) >= 60:
        print("Tempo total %s : %.3f m" % (nome_metodo, tempo_total.total_seconds() / 60))


def limpa_terminal():
    command = "cls" if platform.system().lower() == "windows" else "clear"
    return subprocess.call(command) == 0


def limit_intancia(tamanho_lista, aumento_lista, instancias):
    n = 1
    while n < instancias:
        tamanho_lista = tamanho_lista * aumento_lista
        n = n + 1
    return tamanho_lista
