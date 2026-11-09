class Nodo:                                   # solo si NO viene en el código base
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der
#-----------------------------------------------#

#----------- EJERCICIO 1 -----------------------------------------------------------------#
def construirbst(valores:list):
    raiz = None       
    lista = []
    for e in valores:
        raiz = insertar(raiz, e)
        #Si devolvieramos una lista:
        #lista = insertar(lista, e) -> vamos a dar una version con esta posibilidad tambien.
    return raiz #TO CONFIRMAR MAÑANA EN EL EXAMEN -> devolver una lista o la raiz...?



def insertar(raiz:Nodo, valor:int): #insertar -> subir
    if raiz is None: 
        return Nodo(valor)
    
    #Ya existe arbol:
    if valor >= raiz.valor: #bajar por la derecha
        if raiz.der is None: raiz.der = Nodo(valor)
        else:    #si está ocupado seguimos bajando
            insertar(raiz.der, valor)
            
    else: #bajar por la izquierda
        if raiz.izq is None: raiz.izq = Nodo(valor)
        else:       #si está ocupado seguimos bajando
            insertar(raiz.izq, valor)    
            
    return raiz

#================== COSTES ===============================================================#
#insertar -> O(h) ; siendo h la altura
#construir:
#Mejor caso (lista equilibrada) -> O(n log n)  ; Peor caso (lista ordenada) -> O(n^2)

#----------- EJERCICIO 2 -----------------------------------------------------------------#
def kmenores(raiz:Nodo, k:int):
    if k < 0: raise ValueError("La k no puede ser menor a 0!")
    if raiz is None or k == 0: return []
    #----- k > 0 -> Recorremos "inorder" iterativo -----------------------------------------------# 
    pila, res = [], []
    actual = raiz
    
    while (actual is not None or pila) and len(res) < k: #actual puede ser None y la pila puede estar vacia al principio
        while actual is not None:
            pila.append(actual)
            actual = actual.izq
        #actual es None:
        actual = pila.pop()        #backtracking 
        res.append(actual.valor)    #y metemos ese nodo en res
        actual = actual.der

    return res    
        
#=========== COSTES ============#
# kmenores : 
# Tiempo: O(k + h)      // Memoria: O(h)
# Mejor caso (árbol equilibrado): O(log n + k). Peor caso (cadena, h = n-1): O(n).
