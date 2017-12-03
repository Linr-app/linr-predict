import random

str1 = "["
str2 = "["
rangeNum = 2000

for x in range(0, 5):
	for y in range(0, rangeNum):
		b = random.randrange(480, 1200)
		c = random.randrange(300, 900)
		str1 = str1 + "["+ str(x)+", "+str(b)+"]"
		str2 = str2 + str(c)
		if (y < (rangeNum-1) or x < 4):
			str1 = str1 +", "
			str2 = str2 +", "
		
	
str1 = str1 +"], "
str2 = str2 +"]"
str3 = str1+str2
strFinal = "reg.partial_fit("+str3+")"
f = open('instancia.py', 'w')
f2 = open('caso.txt', 'w')


f2.write(strFinal)
f.write("from sklearn import linear_model\nreg = linear_model.SGDRegressor()\n"+strFinal+"\nprint(reg.predict([[3, 3]]))\nprint('Coef:', reg.coef_)\nprint(reg.predict([[3, 3], [13, 5]]))\nprint('Coef:', reg.coef_)")


