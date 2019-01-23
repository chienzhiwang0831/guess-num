import random
start = int(input('請輸入開始值: '))
end = int(input('請輸入開尾值:'))

r = random.randint(start, end)
count = 0

while True:
	answer = int(input('請猜一個數字: '))
	count += 1
	if answer == r:
		print('恭喜你猜對了!')
		print('總供猜了', count,'次')
		break
	elif answer < r:
		print('比答案小')
	elif answer > r:
		print('比答案大')
		

