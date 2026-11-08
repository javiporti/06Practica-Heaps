import heapq

def top_k(datos:list, k:int):
    #NOTA!: Usar heapq para insertar elementos en "top_k" sin tener que mirar todos los nodos -> mas barato!
    #-------------------------------------------------------------
    if k < 0: raise ValueError("Intentando hacer top_k de una k menor a 0!")
    if not datos or k == 0: return []
    
    #k > 0 y hay datos:
    top_k = []
    for e in datos:
        if len(top_k) < k: 
            heapq.heappush(top_k, e)
            
        elif e > top_k[0]:                # top_k lleno -> sacamos el elemento menor de top_k y 
            heapq.heapreplace(top_k, e)   # reorganiza bajando.     
    #Ordenamos top_k de mayor a menor y la devolvemos:
    top_k.sort(reverse=True)
    return top_k    
        
             
                
            
    