import random
l = random.randint(20, 100)
if l % 2 <> 0:
	l += 1
n = random.randint(2, 10)
if n % 2 == 0:
	n += 1
s = 'Welcome'
print l, n
print '*' * l
for i in xrange(1, n):
	if i == (n + 1) / 2:
		print '*' +  ' ' * ((l-len(s))/2-1) + s + ' ' * ((l-len(s))/2)  + '*' #, i
		print '*' + ' '*(l-2) + '*'
	else:
		print '*' + ' '*(l-2) + '*'
print '*' * l
