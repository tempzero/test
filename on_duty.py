#_*_ coding:utf-8 _*_
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def zhiban(m,d,j,dmax):
	day_week = {
		1:'周一',
		2:'周二',
		3:'周三',
		4:'周四',
		5:'周五',
		6:'周六★',
		7:'周日★',
	}
	print m,'月值班安排：'
	while d <= dmax:
		print d,":",day_week[j]
		d += 3
		j += 3
		if j > 7:
			j = j - 7
	print '\n'
if __name__ == "__main__":
	zhiban(3,18,6,31)
	zhiban(4,2,7,30)
	
