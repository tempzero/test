#coding:utf-8
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

day_week = {
    1: '周一',
    2: '周二',
    3: '周三',
    4: '周四',
    5: '周五',
    6: '周六 ★',
    7: '周日 ★',
}
month_day = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31,
}
#用户数据：
m = 4       #月
d = 26      #日
xq = 3      #星期
dmax = month_day[m]     #最大天数

while m<13:
    dmax = month_day[m]
    print m,d,day_week[xq]
    d += 3
    xq += 3
    if xq > 7:
        xq = xq - 7
    if d > dmax:
        dmax = month_day[m]
        m += 1
        d = abs(dmax - d)
