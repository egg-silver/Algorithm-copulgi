import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k, w = input().rstrip().split()
    k = int(k)
    li = dict()
    for i in range(len(w) - k + 1):
        word = w[i:i + k]  # 문자열을 주어진 길이만큼 앞에서부터 자르기