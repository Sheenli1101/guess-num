import random
start = int(input("請決定隨機數字範圍的開始值:"))
end   = int(input("請決定隨機數字範圍的結束值:"))
r = random.randint(start, end)
count = 0
while True:
	count = count + 1
	num = input("請輸入數字:")
	num = int(num)
	print("這是你猜的第", count, "次")		
	if num == r:
		print("你猜中了!")
		break
	elif num > r:
		print("比答案大")
	elif num < r:
		print("比答案小")
