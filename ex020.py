from random import shuffle
a1 = str(input('Digite o 1º aluno: '))
a2 = str(input('Digite o 2º aluno: '))
a3 = str(input('Digite o 3º aluno: '))
a4 = str(input('Digite o 4º aluno: '))
lista = [a1,a2,a3,a4]
shuffle(lista)
print ('A ordem de apresentação dos trabalhos será {}:'.format(lista))