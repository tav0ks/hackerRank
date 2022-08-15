#https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    nums =student_marks[query_name]
        
    result = (nums[0] + nums[1] + nums[2])/3
    
    print("{:.2f}".format(result))