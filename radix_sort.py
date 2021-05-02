from lista_duplamente_ligada import ListaDuplamenteLigada


def __get_numero_digitos(A):
    m = 0
    for item in A:
        m = max(m, item)
    return len(str(m))


def flatten(lista):
    nova_lista = []
    for sub_lista in lista:
        nova_lista += sub_lista
    return nova_lista


def juntar_listas_ligadas(vetor):
    veto = []
    for lista in vetor:
        if lista.quantidade > 0:
            veto.append(lista.retorna_vetor())
    return flatten(veto)


def cria_array_de_lista():
    vetor_digitos = []
    for i in range(10):
        vetor_digitos.append(ListaDuplamenteLigada())
    return vetor_digitos


def radix(A):
    num_digits = __get_numero_digitos(A)
    for digit in range(0, num_digits):
        B = cria_array_de_lista()
        for item in A:
            num = item // 10 ** digit % 10
            B[num].inserir_no_fim(item)
        A = juntar_listas_ligadas(B)
    return A
