from utils import limpa_terminal
from compara_sort import compara_sort, radix_quick_sort_simples


def cabecalho(nlinhas):
    print("***" * nlinhas)
    print('''
    Ipt - Instituto de Pesquisas Tecnológicas
    Professor: Prof. Dr. Eng. Eduardo Takeo Ueda

    Curso: Mestrado Profissional em Computação Aplicada
    Disciplina: Estrutura de Dados e Análise de Algoritmos

    Aluno: João José Maranhão Junior
    Período: Primeiro Quadrimestre

    Exercicio Programa: Análise Empírica de Algoritmos de Ordenação
    ''')
    print("***" * nlinhas)


def menu():
    nlinhas = 50
    limpa_terminal()
    cabecalho(nlinhas)
    opcao = 0
    while opcao != 3:
        print('''\n\t[1] - Fazer os testes dos algoritmos de ordenaçao\n\t[2] - Simples execução\n\t[3] - Sair\n''')
        opcao = int(input("\tQual é a sua opção?"))
        if opcao == 1:
            tamanho_inicial_lista = int(input("\tTamanho inicial da Lista:"))
            qtd_instancias = int(input("\tQuantidade de Instancias:"))
            compara_sort(tamanho_inicial_lista, qtd_instancias)
            print("***" * nlinhas)
            print('Abra o arquivo report.pdf para ver o relatorio.')
        elif opcao == 2:
            tamanho_inicial_lista = int(input("\tTamanho da Lista:"))
            imprime_array = str(input("\tImprime Array?"))
            while imprime_array != "s" and imprime_array != "n":
                imprime_array = str(input("\tDigite s(sim) ou n(não)?"))
            if imprime_array == 's':
                radix_quick_sort_simples(tamanho_inicial_lista, True)
            else:
                radix_quick_sort_simples(tamanho_inicial_lista, False)
        elif opcao == 3:
            print("\tFinalizando programa !!")
        else:
            print("\tOpção inválida, Tente novamente")
        print("***" * nlinhas)


if __name__ == '__main__':
    menu()
