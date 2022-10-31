
v = []
tam = int(input("Cuantos elementos tiene el array?: "))

def agregarElementos():
    for i in range(tam):
        a = input("Ingrese el valor: ")
        v.append(a)

def ordenar(v):
    for i in range (tam ):
        for j in range (i + 1,tam ):
            if (v[j] < v[i]):
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
    print(v)
    
agregarElementos()
ordenar(v)


