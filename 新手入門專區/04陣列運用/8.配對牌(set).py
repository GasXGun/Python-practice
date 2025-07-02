n = int(input())
qing_cards = list(map(int, input().split()))
other_players = [list(map(int, input().split())) for _ in range(n)]

# 收集所有其他玩家的牌
all_other_cards = []
for player in other_players:
    all_other_cards.extend(player)

# 找出青青可以丟出的牌(在其他玩家中也出現過的牌)
# 使用集合來提高查找效率
discardable = set(qing_cards) & set(all_other_cards)

print(len(discardable))