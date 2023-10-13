numeros=[]
cantidad_numeros = int(input('ingrese la cantidad de numeros que desea agregar a la lista' ))
llenar_lista =[]
suma= 0
def sumar_pares(numeros):
    contador = 0
    while contador < cantidad_numeros:
        numeros.append(int(input('ingresa los numeros a la lista')))
        if numeros[contador] % 2 == 0:
            llenar_lista.append(numeros(contador))
            contador +=1

    suma = sum(llenar_lista)
    print(suma)

sumar_pares(numeros)
           

    
