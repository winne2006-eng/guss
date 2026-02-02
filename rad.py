import random
count = 0
valN = random.randint(1,100)
print(valN)

while True:
	count = count + 1
	gassNum = input("請輸入數字: ")
	gassNum = int(gassNum)
	#count = str(count)
	if gassNum == valN :
		print("猜對了")
		print("你猜了",count ,"次")
		break;
	else:
		if gassNum > valN :
			print("數字太大了...")
			print("你猜了",count ,"次")
		else:
			print("數字太小了....")
			print("你猜了",count ,"次")
			