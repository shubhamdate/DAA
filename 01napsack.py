def dpnapsack(W, n, wt, val):
    dp = [0 for x in range(W+1)]

    for i in range(1, n+1):
        for w in range(W, 0, -1):
            if wt[i-1]<=w:
                dp[w] = max(dp[w], dp[w-wt[i-1]+val[i-1]])
    return dp[W]

W = int(input("Maximum capcity: "))
n = int(input("Total Number of Weight: "))
wt = []
val = []
for i in range(n):
    wet, vall = map(int, input("Enter Weight and Value: ").split())
    wt.append(wet)
    val.append(vall)  
print(dpnapsack(W, n, wt, val))