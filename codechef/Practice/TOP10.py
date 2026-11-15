// Problem: TOP10
// Platform: codechef
// Language: Python3​
// Verdict: Accepted
// URL: https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TOP10
// Solved on: 2026-11-15T05:25:29.140Z

# cook your dish here

T = int(input())

for _ in range(T):
    X = int(input())

    if X <= 10:
        print("YES")
    else:
        print("NO")
