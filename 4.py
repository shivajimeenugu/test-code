#Question -4 Soluction
matrix = []

for i in range(256):
    row = list(map(int,input().split()))
    matrix.append(row)

rowLength = len(matrix)
colLength = len(matrix[0])
t,l,r,btm = 256,256,0,0

for i in range(0,rowLength):
    init = 0
    while(init < colLength):
        if (matrix[i][init] == 0):
            l = min(l,init)
            break
        init+=1
    
    end = colLength - 1
    while(end >=0 ):
        if(matrix[i][end] == 0):
            r = max(end,r)
            break
        end -= 1

    t_init = 0
    while(t_init < rowLength):
        if (matrix[t_init][i] == 0):
            t = min(t,t_init)
            break
        t_init+=1

    btm_end = rowLength - 1
    while(btm_end >= 0):
        if (matrix[btm_end][i] == 0):
            btm = max(btm,btm_end)
            break
        btm_end-=1

print((t,l),(t,r),(btm,l),(btm,r))