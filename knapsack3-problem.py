dp = [[]]
def knapsack(totalW , weight , value):
    global dp
    dp = [[-1 for x in range(len(weight)+1)] for x in range(totalW+1)]

    for i in range(totalW+1):          # capacity
        for j in range(len(weight)+1): # items
            if i == 0 or j == 0:
                dp[i][j] = 0
                continue

            if weight[j-1] > i:
                dp[i][j] = dp[i][j-1]
                continue

            dp[i][j] = max(dp[i][j-1], value[j-1] + dp[i - weight[j-1]][j-1])

    return dp[totalW][len(weight)]

weight = [1,2,3]
value = [6,10,12]
targetW = 5
print(knapsack(targetW , weight , value))  # Expected output: 22