def knapsack(W, n, arr):
    arr.sort(key = lambda x:  x[1]/x[0], reverse= True)

    profit=0
    for item in arr:
        if item[0]<=W:
            W-=item[0]
            profit+=item[1]
        else:
            profit+=item[1]*W/item[0]
            break
    return profit

W = int(input("Maximum capcity: "))
n = int(input("Total Weight: "))




arr = []
for i in range(n):
    wt, val = map(int, input("Enter Weight and Value").split())
    arr.append((wt, val))
print(knapsack(W, n, arr))