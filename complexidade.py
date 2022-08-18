ent = input().split()

soma = 0
#MEM = 10
#IO = 30
#PROCSUM = 1
#PROCMUlt = 10
#LOOP

for i in range(1, len(ent)):
    if ent[i] == "LOOP":
        sloop = 0
        c = int(ent[i + 1])
        while ent[i] != "FIMLOOP":
            if ent[i] == "MEM":
                sloop += 10
                ent[i] = "0"
                i += 1
            elif ent[i] == "IO":
                sloop += 30
                ent[i] = "0"
                i += 1
            elif ent[i] == "PROCSUM":
                sloop += 1
                ent[i] = "0"
                i += 1
            elif ent[i] == "PROCMULT":
                sloop += 10
                ent[i] = "0"
                i += 1
            else:
                i += 1
        soma += sloop*c
    elif ent[i] == "MEM":
        soma += 10
    elif ent[i] == "IO":
        soma += 30
    elif ent[i] == "PROCSUM":
        soma += 1
    elif ent[i] == "PROCMULT":
        soma += 10

    elif ent[i] == "FIM":
        print(soma)
    else:
        i += 1
            

