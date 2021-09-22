def knapSack(W, wt, val, n): 
    t=range(W+1)
    u = range(n+1)
    K = [[0 for x in t] for x in u] 
    P = [[0 for x in t] for x in u]  
    C = [[0 for x in t] for x in u] 

    for i in u: 
        for w in t: 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                a= val[i-1] + K[i-1][w-wt[i-1]]
                b=  K[i-1][w]

                if(a>b):
                    K[i][w]= a
                    C[i][w] = 1+ C[i-1][w - wt[i-1]]
                    P[i][w] = wt[i-1] + P[i-1][w - wt[i-1]]
                else:
                    K[i][w]=b
                    C[i][w] = C[i-1][w]
                    P[i][w] = P[i-1][w]


            else: 
                K[i][w] = K[i-1][w] 
                C[i][w] = C[i-1][w]
                P[i][w] = P[i-1][w]
    print("%d brinquedos" % K[n][W])
    print("Peso: %d kg" % P[n][W])
    print("sobra(m) %d pacote(s)" % (n-C[n][W]))
    print()            

n = int(input())
for i in range(n):
        pac = int(input())
        qtd = []
        peso = [] 
        for j in range(pac):
            data = input().split(" ")
            qtd.append(int(data[0]))
            peso.append(int(data[1]))
        knapSack(50, peso, qtd, len(peso))