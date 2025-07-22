def find_combinations(coins, amount):
    coins.sort() # 確保硬幣按升序排列
    result = []
    
    def backtrack(remaining, index, current_combination):
        if remaining == 0:
            result.append(current_combination.copy())
            return
        if index >= len(coins):
            return
        
        coin = coins[index]
        max_count = remaining // coin
        
        for count in range(0, max_count + 1):
            current_combination.append(count)
            backtrack(remaining - count * coin, index + 1, current_combination)
            current_combination.pop()
    
    backtrack(amount, 0, [])
    return result

n_and_coins = list(map(int, input().split()))
n = n_and_coins[0]
coins = n_and_coins[1:n+1]
p = n_and_coins[-1]

combinations = find_combinations(coins, p)

combinations.sort(key=lambda x: tuple(-val for val in x))  # 按幣值數量降序排列

for combo in combinations:
    print(f"({','.join(map(str, combo))})")