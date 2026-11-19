// Problem: DETSCORE
// Platform: codechef
// Language: Python3​
// Verdict: Accepted
// URL: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DETSCORE
// Solved on: 2026-11-19T07:44:09.186Z

# cook your dish here
t = int(input())

for _ in range(t):
    x, n = map(int, input().split())
    print((x // 10) * n)

