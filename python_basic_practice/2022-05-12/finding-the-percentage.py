if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marks = student_marks[query_name]
    total_marks = sum(marks)
    
    avg_marks = float(total_marks)/ len(marks)
    print("{:.2f}".format(avg_marks))
