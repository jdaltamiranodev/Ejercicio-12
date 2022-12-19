#Enunciado del ejercicio:

#Crea un script que le pida al usuario una lista de países
# (separados por comas). Éstos se deben almacenar en una lista.
# No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados
# alfabéticamente y separados por comas.

#paises = input("Introduzca una lista de paises separados por coma: ")
paises = 'Países Bajos,Senegal,Ecuador,Catar,Inglaterra,'\
         'Estados Unidos,Irán,Gales,Argentina,Polonia,México,'\
         'Arabia Saudí,Francia,Australia,Túnez,Dinamarca,'\
         'Japón,España,Alemania,Costa Rica,Marruecos,Croacia,'\
         'Bélgica,Canadá,Brasil,Suiza,Camerún,Serbia,Portugal,'\
         'República de Corea,Uruguay,Ghana,'\
         'Brasil,Francia,Irán,Costa Rica,Serbia'

lista_paises = []
lista_paises = paises.split(",")

print("\nLista desordenada:\n")

for i in range(len(lista_paises)):
    print("País " + str(i + 1) + ": " + str(lista_paises[i]))

lista_paises_ord = []
lista_paises_ord = list(set(lista_paises))
lista_paises_ord.sort()

print("\n\nLista ordenada:\n")

for i in range(len(lista_paises_ord)):
    print("País " + str(i + 1) + ": " + str(lista_paises_ord[i]))