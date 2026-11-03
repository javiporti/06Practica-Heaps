import heapq


def top_k(datos, k):
    if k < 0: raise IndexError("No tiene sentido hayar el top {k}")
    if k == 0:return []

    #tenemos un k mayor que 0:
    mejores = []
    for x in datos:
        if len(mejores) <= k:
            heapq.heappush(mejores, x)
        if x > mejores[0]: #insertamos por el final o por el principio?
            heapq.heapreplace(mejores, x)
            # heapq.heappop(mejoress)
            # heapq.heappush()

    #ordenamos de mayor a menor el top-k:
    mejores.sort(reverse = True)
    return mejores

