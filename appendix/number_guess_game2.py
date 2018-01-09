import random

result = [None, None, None]

for i in range(3):
    rand_num = random.randint(1, 9) 
    #print("com : ", rand_num)
    
    player_num = input("Make a guess(1~9) : ")
    
    while not player_num.isdigit():
        print("Must be an integer from 1 to 9")
        player_num = input("Make a guess(1~9) : ")

    player_num = int(player_num)
    
    if rand_num == player_num:
        result[i] = "player"
    else:
        result[i] = "computer"
        
#print(result)

print("player : {}, computer : {}".format(
    result.count("player"),
    result.count("computer")))

if result.count("player") >=2:
    print("You win!")
else:
    print("You lose!")
    





