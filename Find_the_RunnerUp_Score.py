#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
arr.sort(reverse = True)
for i in arr:
    if i < arr[0]:
        print(i)
        break