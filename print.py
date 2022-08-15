#https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
def numbers(n):
    aux = ''
    for i in range(n+1):
        if i == 0:
            aux = ''
        else: 
            aux = aux+str(i)
    
    print(aux)
    
numbers(n)