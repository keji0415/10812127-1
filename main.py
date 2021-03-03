
from myMath import myStatistics

print('請輸入五個數值')
x = []
for i in range(5):
    j = input('%s %d %s' % ('第', i+1, '個:'))
    x.append(int(j))

print(myStatistics.myMean(x))