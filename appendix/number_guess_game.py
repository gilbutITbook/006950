import random

rand_num = random.randint(1, 9)
print("Computer : {}".format(rand_num))

player_num = int(input("Make a guess(1~9) : "))
print("Player : {}".format(player_num))

if rand_num == player_num:
    print("You win!")
else:
    print("You lose!")

#3-2절 삼항 연산자
#print("You win!" if rand_num == player_num else "You lose!")
