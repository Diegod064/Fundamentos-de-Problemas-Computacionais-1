ent = str(input())
pilha = []
x = 0
a = 0
f = 0
ci = 0
for elemento in ent:
    if elemento in "({[":
        pilha.append(elemento)
        a += 1
    elif elemento == ")":
        if len(pilha) > 0:
            f += 1
            x = pilha.pop()
            if x != "(":
                ci += 1
        else:
            ci += 1
    elif elemento == "}":
        if len(pilha) > 0:
            f += 1
            x = pilha.pop()
            if x != "{":
                ci += 1
        else:
            ci += 1
    elif elemento == "]":
        if len(pilha) > 0:
            f += 1
            x = pilha.pop()
            if x != "[":
                ci += 1
        else:
            ci += 1

if a != f or ci > 0:
    print('casamento imperfeito')
else:
    print('casamento perfeito')
