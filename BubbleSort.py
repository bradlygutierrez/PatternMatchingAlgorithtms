import tabnanny


v = [3,4,5,2,1,23,2,5,2,3,52,12,0]
print(v)

i = 0
tam = len(v)


while(i < tam - 1):
    j = i+1
    while(j < tam):
        if (v[j] < v[i]):
            aux = v[i]
            v[i] = v[j]
            v[j] = aux
        j +=1
    i+=1
print(sorted(v))
print(v)

    #for i in range (n-1):
        #for j in range(0, n-i-1)
