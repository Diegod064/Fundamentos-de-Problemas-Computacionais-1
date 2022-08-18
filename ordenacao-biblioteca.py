def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return alist

def quicksort(v):
    if len(v) <=1:
        return v
    less, equal, greater = [], [], []
    f = []
    for i in range(len(v)):
        f.append(Livro.getNome(v[i]))
    pivot = f[0]
    for x in range(len(v)):
        if f[x] < pivot:
            less.append(v[x])
        elif f[x] == pivot:
            equal.append(v[x])
        else:
            greater.append(v[x])
    return quicksort(less) + equal + quicksort(greater)

class Livro:
    codigo = None
    nome = None
    autor = None
    __qtdeAlugueis = 0

    def __init__(self, codigo, nome, autor):
        self.codigo = codigo
        self.nome = nome
        self.autor = autor

    def incrementaAluguel(self):
        self.__qtdeAlugueis += 1

    def getQtdeAlugueis(self):
        return self.__qtdeAlugueis

    def getNome(self):
        return self.nome


class Biblioteca:
    alugados = []
    disponiveis = []

    def inserir(self, livro):
        self.disponiveis.append(livro)

    def alugar(self, livro):
        ok = True
        mensagem = None
        if livro in self.disponiveis:
            for i in self.disponiveis:
                if i == livro:
                    i.incrementaAluguel()
                    self.alugados.append(i)
                    self.disponiveis.remove(i)
                    break
        elif livro in self.alugados:
            ok = False
            mensagem = "O livro ja esta alugado, infelizmente voce nao podera alugar"
        else:
            ok = False
            mensagem = "O livro nao existe"
        return (ok, mensagem)

    def devolver(self, codLivro):
        ok = True
        mensagem = None
        for livro in self.alugados:
            if livro.codigo == codLivro:
                self.disponiveis.append(livro)
                self.alugados.remove(livro)
                break
        else:
            ok = False
            mensagem = "O livro nao esta alugado"
        return (ok, mensagem)

    def livroMaisAlugado(self):
        ok = True
        mensagem = None
        maior = 0
        nome = None
        for livro in self.disponiveis:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        for livro in self.alugados:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        if maior == 0:
            ok = False
            mensagem = "Nenhum livro foi alugado ainda"
        else:
            mensagem = "O livro mais alugado e: %s (%d alugueis)" % (nome, maior)
            return (ok, mensagem)

    def getDisponiveis(self): #retorna disponiveis em ordem
        odisp = quicksort(self.disponiveis)
        self.disponiveis = odisp
        return odisp

    def getAlugados(self): #retorna alugados em ordem
        oalug = quicksort(self.alugados)
        self.alugados = oalug
        return oalug

    def livrosOrdenadosPeloNome(self):
        if len(self.disponiveis) == 0:
            self.todos = self.alugados
        elif len(self.alugados) == 0:
            self.todos = self.disponiveis
        else:
            somalivros = self.getDisponiveis() + self.getAlugados()
            todoslivros = mergeSort(somalivros)
            self.todos = todoslivros
        return self.todos


ent = input().split(',')
ql = int(ent[0]) #quantidade de livros

l1 = Livro(ent[1], ent[2], ent[3])
l2 = Livro(ent[4], ent[5], ent[6])
l3 = Livro(ent[7], ent[8], ent[9])
b = Biblioteca()

livros = [l1, l2, l3]
for i in range(len(livros)):
    b.inserir(livros[i])

for l in b.getDisponiveis():
    print(l.codigo, end=' ')




