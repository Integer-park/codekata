def solution(n):
    total = 0
    for i in range(0, n + 1, 2):
        total += i

    answer = total
    return answer