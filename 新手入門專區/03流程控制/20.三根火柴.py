a, b, c = sorted(map(int, input().split()))  # 先排序，方便檢查三角形條件

# 先檢查是否能構成三角形
if a + b <= c:
    print("Not Triangle")
else:
    # 計算平方
    a_sq = a ** 2
    b_sq = b ** 2
    c_sq = c ** 2

    # 判斷三角形類型
    if a_sq + b_sq == c_sq:
        print("Right Triangle")
    elif a_sq + b_sq < c_sq:
        print("Obtuse Triangle")
    else:  # a_sq + b_sq > c_sq
        print("Acute Triangle")