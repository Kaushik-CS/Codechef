// Problem: IPLTRSH
// Platform: codechef
// Language: Python3​
// Verdict: Accepted
// URL: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/IPLTRSH
// Solved on: 2026-11-24T09:02:59.738Z

# cook your dish here

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(max(0, n - m))
