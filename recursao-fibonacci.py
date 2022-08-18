def fibRec(n):
    if n == 1:
        return 'a'
    elif n <= 0:
        return 'b'
    else:
        return fibRec(n - 1) + fibRec(n - 2)

n = int(input())
print(fibRec(n))