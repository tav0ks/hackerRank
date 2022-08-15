#https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
def weird(n):
        if (n % 2 == 0):
            if (n > 1 and n < 6) or n > 20:
                print('Not Weird')
            if (n > 5 and n < 21):
                print('Weird')
        else:
            print('Weird')    
            

weird(n)
        