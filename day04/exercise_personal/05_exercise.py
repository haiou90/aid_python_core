import random

random_number = random.randint(1,100)
count = 0
while True:
    count += 1
    guess = int(input("请猜"))
    if guess == random_number:
        print("猜对了,猜了"+ str(count) + "次")
        break
    elif guess < random_number:
        print("猜小了")
    else:
        print("猜大了")