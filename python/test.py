#MAP APLICA UNA FUNCIÓN A UNA LISTA!
#map(f, lista, lista)
#-------- LEER, CALCULAR Y ESCRIBIR --------------#
#OBJETIVO: SABER HACERNOS TEXT DE COSAS
# 2
# 3
# 1 2 3
# 2
# 1 9

#CASO 1: Nos dan T casos:

#CASO 2: Nos dan T casos:

#CASO 3: EOF:

#Nota: Si le pasamos un archivo .txt nos ahorramos tener que estar pegado a la terminal como un negro
while True:
    try:
        n = int(input())
        lista = list()
    except: 
        break
#cat .\test.txt | python test.py        // pipeline