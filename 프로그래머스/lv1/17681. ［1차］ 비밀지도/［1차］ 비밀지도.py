def solution(n, arr1, arr2):
    answer = ["".join(map(lambda x: "#" if x == "1" else " ", bin(arr1[i] | arr2[i])[2:])) for i in range(n)]
    return list(map(lambda x: " " * (n - len(x)) + x, answer))