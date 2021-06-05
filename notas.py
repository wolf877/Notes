import time as tm 
import numpy as np
import os

while True:
    try:
        NL=int(input('Numero de avaliações: '))
        break
    except ValueError:
        print('Use um numero inteiro')
        continue

while True:
    try:
        AL=int(input('Numero de Alunos: '))
        break
    except ValueError:
        print('Use um numero inteiro')
        continue

A=AL+1
N=NL+1
array1 = []
Notas = []
for j in range(1,N):
    for i in range(1,A):
        array1.append(float(input('Nota dos alunos {1} na {0}° avaliação = '.format(j, i))))
    Notas.append(array1)
    print(' ')
    array1 = []
#print(Notas)

a=np.array(Notas)
print(a)

while True:
    try:
        M=float(input('Qual a media de aprovação? '))
        break
    except ValueError:
        print('Use um numero')

while True:
    while True:
        try:
            i=int(input('Numero do aluno que deseja saber a media? '))
            n=i-1
            b=a[:,n]
            b1=[]
            for item in b:
                b1.append(float(item))
            media = sum(b1)/len(b1)
            #print(type(b))
            #print(type(b1))
            break
        except (ValueError, IndexError):
            print('use um numero valido')
    if media>=M:
        print(media)
        print('ALUNO APROVADO')
        print('As notas foram: {}'.format(b1))
    elif media<=M:
        print('A media é {:.2f}'.format(media))
        print('ALUNO NÃO APROVADO')
        print('As notas foram: {}'.format(b1))
    while True:
        Again=input('Deseja a media de outro aluno? ') 
        if Again =='Sim' or Again == 'sim':
            break
        elif Again =='Não' or Again == 'não':
            break
        else:
            print('Responda Sim ou Não')
            continue
    if Again =='Sim' or Again == 'sim':
        continue
    elif Again =='Não' or Again == 'não':
        break
print('fim')
os.system('pause')


    


