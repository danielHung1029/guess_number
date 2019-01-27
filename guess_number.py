import random

start = input('請輸入隨機數字範圍最小值: ')
end = input('請輸入隨機數字範圍最大值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	num = input('請輸入數字: ')
	num = int(num)
	count = count + 1 #也可寫成 count += 1
	if num == r:
		print('恭喜猜對了')
		print('你已經猜了:',count , '次')
		break
	elif num < r:
		print('你猜的數字比答案小')
	else:
		print('你猜的數字比答案大')
	print('你已經猜了:',count , '次')

