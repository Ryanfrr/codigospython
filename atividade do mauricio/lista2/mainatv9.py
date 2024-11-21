def quick_sort(lista):
    pilha = [(0,len(lista)-1)]
    while pilha:
        inicio,fim = pilha.pop()
        if inicio<fim:
            pivot=partition(lista,inicio,fim)
            pilha.append((inicio,pivot-1))
            pilha.append((pivot+1,fim))
    return lista
def partition(lista,inicio,fim):
    pivot=lista[fim]
    i=inicio-1
    for j in range(inicio,fim):
        if lista[j]<=pivot:
            i+=1
            lista[i],lista[j]=lista[j],lista[i]
    lista[i+1],lista[fim]=lista[fim],lista[i+1]
    return i+1
