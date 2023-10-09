def tribonacci(num):

    dp = [0] * num
    dp[0] = dp[1] = 0
    dp[2] = 1
 
    for i in range(3,num) :
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
 
    for i in range(0,num) :
        print(dp[i] , " ", end="")
         
 
# Driver code
num = 5
tribonacci(num)