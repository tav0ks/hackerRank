#https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
print([[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1)if a + b + c != n])