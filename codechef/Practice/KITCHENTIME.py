// Problem: KITCHENTIME
// Platform: codechef
// Language: Python3​
// Verdict: Accepted
// URL: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/KITCHENTIME
// Solved on: 2026-11-23T07:09:36.153Z


t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    print(y - x)
