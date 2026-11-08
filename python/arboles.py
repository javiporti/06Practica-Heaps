class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der


def espejo(raiz:Nodo):
    if raiz is None: return
    return Nodo(raiz.valor, espejo(raiz.der), espejo(raiz.izq))


def son_espejo(a, b):
    if a and b is None: return True #Hemos llegado a las hojas -> condicion de parada.
    if a is None or b is None: return False

    return(a.valor == b.valor and son_espejo(a.izq, b.der) and son_espejo(a.der, b.izq))

    #Hay que comprobar que para cada nodo de cada arbol su espejo es 


def es_simetrico(raiz): #Llama a espejo
    #Describir lo que esta pasando:
    if raiz is None: return True
    #TO-THINK



def inorden(raiz):
    salida = []
    def visitar(nodo):
        if nodo is not None:
            visitar(nodo.izq)
            salida.append(nodo.valor)
            visitar(nodo.der)
    visitar(raiz)
    return salida
