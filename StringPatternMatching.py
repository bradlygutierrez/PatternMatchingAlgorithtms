import random
def busquedaLineal(lista,  objetivo):
    match = False
    
    for elemento in lista: 
        if elemento == objetivo: 
            match = True
            break
    
    return match

if __name__ == '__main__':
    tamList = int(input("De que tamaño será la lista? "))
    objetivo = int(input('Qué numero quieres encontrar? '))

    lista = [random.randint(0,100) for i in range(tamList)]
    encontrado = busquedaLineal(lista,objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"Esta" if encontrado else "no esta"} en la lista')