# BMI problem
# bisect
import bisect
n = int(input())
#breakpoint
breakpoints = [18.5,24,28]
result = ["體重過輕","正常","體重過重","肥胖",]
for _ in range(n):
    bmi = float(input())
    print(result[bisect.bisect_right(breakpoints,bmi)]) #bisect 要用()呼叫
    