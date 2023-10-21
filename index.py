def achar_elemento(elem, arr):
    achou = False
    cumprimento = len(arr)

    for i in range(cumprimento):
        if (arr[i] == elem):
            achou = True
        
    if(achou == True):
        print("O nome", elem, "foi encontrado no array.")
    else:
        print("O elemento", elem, "nao foi encontrado no array.")
            
            

nomes = ["Rafael", "Arturo", "Karen", "Julia", ]
achar_elemento("Arturo", nomes)
            

            
            
        