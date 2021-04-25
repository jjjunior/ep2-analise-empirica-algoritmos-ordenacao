from lista_duplamente_ligada import ListaDuplamenteLigada


# get number of digits in largest item
def __get_num_digits(A):
    m = 0
    for item in A:
        m = max(m, item)
    return len(str(m))

def flatten(lista):
    """
    Flatten a list of lists.
    Usage: flatten([[list a], [list b], ...])
    Output: [elements of list a, elements of list b]
    """
    nova_lista = []
    for sub_lista in lista:
        nova_lista += sub_lista
    return nova_lista


def juntar_listas_ligadas(vetor):
    veto = []
    for lista in vetor:
        if lista.quantidade > 0:
            veto.append(lista.retorna_vetor())
    # print('Vetor de Lista:', flatten(veto))
    return flatten(veto)


def cria_vetor_de_lista():
    vetor_digitos = []
    for i in range(10):
        vetor_digitos.append(ListaDuplamenteLigada())
    return vetor_digitos


def radix(A):
    num_digits = __get_num_digits(A)
    for digit in range(0, num_digits):
        B = cria_vetor_de_lista()
        for item in A:
            # num is the bucket number that the item will be put into
            num = item // 10 ** digit % 10
            B[num].inserir_no_fim(item)
        A = juntar_listas_ligadas(B)
    return A

# def main():
#     A = [55, 45, 3, 289,36,77,23,10,11,47,61,86,99,101,374, 213, 1, 288, 53, 2, 7]
#     A = radix(A)
#     print(A)

# B = [i for i in range(1000000)]
# shuffle(B)
# B = radix(B)
# print(B[:6], B[-6:])


# main()
