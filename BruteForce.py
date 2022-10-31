
def bruteForceMethod(text, pattern):
    for i in range(len(text)):
        for j in range(len(pattern)):
            if i + j >= len(text):
                break
            if text[i+j] != pattern[j]:
                break
        else: 
            return True
    return False


#print(bruteForceMethod("Hola me llamo bradly", "bradly"))

def bruteForce(text, pattern):
    ls = len(text)
    lp = len(pattern)
    max = (ls - lp +1)

    for i in range(max-1):
        flag = True
        j = 0
        while(j < lp and flag == True):
            if(pattern[j] != text[j+i-1]):
                flag = False
            else:
                flag == True
            j += 1
        if flag == True:
            return i
    return 0



pattern = "culear"
text= "Duran me va a culear mañana"

print(bruteForce(text,pattern))

