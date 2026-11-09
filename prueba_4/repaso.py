class Nodo:                                   
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der
#~-------------------------------------------------~#

def construirbst(valores:list):
    if len(valores) == 0:
        return 
    raiz = None
    for e in valores:
        raiz = insertar(raiz, e)
    
    return raiz
        
def insertar(raiz:Nodo, valor:int):
    if raiz is None: return Nodo(valor)
    #hay arbol:
    if valor < raiz.valor:  #a la izquierda
        raiz.izq = insertar(raiz.izq, valor)
        
    else: #a la izquierda
        raiz.der = insertar(raiz.der, valor)
            
    return raiz

#costes:
#peor caso: (lista ordenada) -> O(n^2) // mejor caso (lista orden repartido) -> O(n log n)
    
#=============== EJERCICIO 2 ===============
def kmenores(raiz: Nodo, k:int):    #inorden iterativo
    if k < 0: raise ValueError("No puede haber una k negativa!")
    if k == 0: return []
    # k > 0: recorremos el arbol en orden
    #inicializamos variables:
    pila, res = [], []
    actual = raiz
    while (actual is not None or pila) and len(res) < k:
        while actual is not None:
            pila.append(actual)
            actual = actual.izq
        #actual es None:
        actual = pila.pop()                    #backtracking
        res.append(actual.valor)                     #añadimos el ultimo nodo a 'res'
        actual = actual.der                    #vamos a la rama derecha (siguiente menor)
    return res
    
#costes:
#tiempo: O(k + h)       // memoria: O(h)