import random
r = random.randint(1, 100)
while True:
	num = input('請輸入1~100之間的數字: ')
	num = int(num)
	if num == r:
		print('恭喜猜對了')
		break
	elif num < r:
		print('你猜的數字比答案小')
	else:
		print('你猜的數字比答案大')

