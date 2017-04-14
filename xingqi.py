#coding=utf-8
year = 2017
y = year % 100
c = (year - y)/100 
m = 6
d = 1
w = y + (y/4 - (y/4*100 % 100)/100) + (c/4 - (c/4*10 % 10)/10) - 2*c + (26*(m+1)/10) + d - 1
print str(c)+str(y)+'.'+str(m)+'.'+str(d)
print w % 7
