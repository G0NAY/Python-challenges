lista = []
k = 0
print("Pasos:\n1.-Ingresar elementos a una lista (2 como minimo)\n2.-ingrese un numero de validación\n3.-Mostrar resultado (True or False si la suma de dos elementos de la lista es igual al numero proporcionado)\n")

count = 0
i=0
while count == 0:
    opcion = int(input("Ingrese elemento: "))
    lista.append(opcion)

    print(opcion,'agreagdo a lista\n')
    print('Lista:',lista,'\n')

    if i > 0:
        j = 0
        while j == 0:
            agregar = str(input('Desea agregar otro elemento a la lista? (Y/N): '))
            if agregar.lower() == 'y' or agregar.lower() == 'n':
                if agregar.lower() == 'y':
                    j = 1
                else:
                    j = 1
                    count = 1
            else:
                print('Entrada no valida')
    i += 1
    ##<>
i=0
while i == 0:
    try:
        k = int(input("Ingrese un numero para validacion: "))
        i = 1
    except:
        print('Elemento no valido, debe de ingresar un entero')


elements = len(lista)
print('Son ',elements,' elementos en la lista:', lista)
print('K es igua a: ', k)

i=0
sumas = []
for item in lista:
    for it in lista:
        ##print(it,'+',item,'=',it+item)
        suma = it+item
        if suma == k:
            sum = str(it)+'+'+str(item)+'='+str(it+item)
            sumas.append(sum)
    ##print(lista[i+1])
    i += 1

if len(sumas) != 0:
    print(True)
    print(sumas)
else:
    print(False)
