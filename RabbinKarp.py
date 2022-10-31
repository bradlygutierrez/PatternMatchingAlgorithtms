#Hash Roling Algotrithm 
#This algorithm offers an eficency of O(m+n) in the most of the cases and O(m*n) in the worst cases
#This consist in hashing a pattern and a text using a base and a prime number 
#The chain will be: S(base)pow(m-1) where m= lenght of pattern 
#For this method will use a comparaison with a windows with the same lenght of the pattern, equeals to Brute force method

def rabin_karp(s,p):
    b= 26
    q=101
    #Here the b= base and q=prime number
    n = len(s)
    m = len(p)
    h = 1
    hashP = 0
    hashS = 0
    
    for i in range(m-1):
        h = (h*b)%q
    
    #Hash of the paterrn and first windws
    for i in range(m):
        hashP=(b*hashP + ord(p[i])) % q
        hashS = (b*hashS + ord(s[i])) % q
    
    
    for i in range(n-m+1):
        if hashS == hashP:
            flag = True
            for j in range(m-1):
                if(p[j] != s[i+j]):
                    break
            if flag: print("Match at index: ", i)
        if i < n-m:
          hashS = (b*(hashS-ord(s[i])*h + ord(s[i+m]))) % q
        if(hashS < 0):
            hashS += q

rabin_karp("Asdadadasdasdasdasdas", "dad")
    

