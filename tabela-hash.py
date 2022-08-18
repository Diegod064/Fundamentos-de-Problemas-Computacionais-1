#CHAVE elemento a ser inserido ou buscado
#QTDE_CONTAINERS é a quantidade de containers
#TAM_CONTAINER é o tamanho de cada container
#n = TAM_CONTAINER * QTDE_CONTAINERS tamanho total da lista
#QTDE_INSERCOES quantidade de chaves a serem inseridas na tabela hash
#para descobrir container CHAVE % QTDE_CONTAINERS

ent = [int(ent) for ent in input().split()]
QTDE_CONTAINERS = 0
TAM_CONTAINER = 0
QTDE_INSERCOES = 0
chaves = []
busca = []
th = []
contador = 0

for i in range(len(ent)):
    if i == 0:
        QTDE_CONTAINERS = ent[i]
    elif i == 1:
        TAM_CONTAINER = ent[i]
    elif i == 2:
        QTDE_INSERCOES = ent[i]
    elif i < (QTDE_INSERCOES + 3):
        chaves.append(ent[i])
    else:
        busca.append(ent[i])

n = QTDE_CONTAINERS * TAM_CONTAINER

while contador < n:
    for i in range(len(chaves)):
        c = chaves[i] % QTDE_CONTAINERS
        ic = c * TAM_CONTAINER
        if contador == ic:
            th.append(chaves[i])
    if contador < len(th):
        contador += 1
    else:
        th.append('none')
        contador += 1

for i in range(len(busca)):
    c = busca[i] % QTDE_CONTAINERS
    ic = c * TAM_CONTAINER
    a = 0  #numero de operações
    for k in range(TAM_CONTAINER):
        if th[ic] == 'none':
            a = 1
        elif busca[i] == th[ic + k]:
            a += k + 1

    if a == 0: #se a == 0 então o container ja está cheio
        a = TAM_CONTAINER
    print(a,'', end='')


