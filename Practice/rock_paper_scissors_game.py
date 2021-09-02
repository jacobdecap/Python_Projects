import random 

player = 0
cpu = 0

print('Three points win the game')

while player < 3 and cpu < 3:
    cpu_choice = random.choice(['rock','paper','scissors'])
    player_choice = input('Rock, Paper or scissors: ')
    
    print(f'The player chose ' + player_choice.lower() + ' and the CPU chose ' + cpu_choice)

    if player_choice.lower()== cpu_choice:
        print("Tie! No points!")
    else :
        if cpu_choice == 'paper' and player_choice.lower() == 'rock':
            cpu += 1
            print('CPU wins!')
            
        elif cpu_choice == 'paper' and player_choice.lower() == 'scissors':
            player += 1
            print('Player wins!')
        
        elif cpu_choice == 'rock' and player_choice.lower() == 'scissors':
            cpu += 1
            print('CPU wins!')

        elif cpu_choice == 'rock' and player_choice.lower() == 'paper':
            player += 1
            print('Player wins!')

        elif cpu_choice == 'scissors' and player_choice.lower() == 'paper':
            cpu += 1
            print('CPU wins!')
        
        elif cpu_choice == 'scissors' and player_choice.lower() == 'rock':
            player += 1
            print('Player wins!')
        else:
            print("You probably failed to input a correct string... Type rock, paper, or scissors!")
if player > cpu:
    print('Congrats Player, you have won the best of 3!')
else:
    print('Congrats CPU, you have won the best of 3!')



        
        


