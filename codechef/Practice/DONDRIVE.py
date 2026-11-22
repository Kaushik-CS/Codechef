// Problem: DONDRIVE
// Platform: codechef
// Language: Python3​
// Verdict: Accepted
// URL: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DONDRIVE
// Solved on: 2026-11-22T04:19:10.583Z

# cook your dish here

T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    print(N - X)
