import random
r = random.randint(1, 100)
count = 0
while True:
	num = input('請輸入1~100之間的數字: ')
	num = int(num)
	count = count + 1
	if num == r:
		print('恭喜猜對了')
		print('你已經猜了:',count , '次')
		break
	elif num < r:
		print('你猜的數字比答案小')
	else:
		print('你猜的數字比答案大')
	print('你已經猜了:',count , '次')

