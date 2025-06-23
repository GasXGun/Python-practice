import bisect
n = int(input())
breakpoints = [60, 70, 80, 90]
grades = ["不及格","丙等","乙等","甲等","優等"]

for _ in range(n):
    score = int(input())
    print(grades[bisect.bisect_right(breakpoints, score)])
#bisect_right:返回最右邊相等值的下一個位置/返回第一個大於該值的位置
