class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der


def espejo(raiz:Nodo): #-> CORRECT -> TO THINK...
    if raiz is None: return
    i = espejo(raiz.der)
    d = espejo(raiz.izq)
    nuevo = Nodo(raiz.valor, i, d)
    return nuevo


def son_espejo(a, b) -> bool:  #a y b son arboles
    if a is None and b is None: return True
    if (a is None and b is not None) or (a is not None and b is None): return False
    #------------ existen ambos arboles ---------------
    
    

def es_simetrico(raiz) -> bool: 
    if raiz is None: return True
    return son_espejo(raiz.izq, raiz.der)

def inorden(raiz):
    if raiz is None: return 
    
    
    return 